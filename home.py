import streamlit as st
import time
import random
from datetime import datetime
from bot import query_lyzr_agent

# Page configuration
st.set_page_config(
    page_title="PolicyPal",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for orange and white theme
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #fff7ed 0%, #ffffff 100%);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(135deg, #ea580c 0%, #fb923c 100%);
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #ea580c 0%, #fb923c 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Chat message styling */
    .user-message {
        background: linear-gradient(135deg, #ea580c 0%, #fb923c 100%);
        color: white;
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        margin-left: 20%;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .bot-message {
        background: white;
        color: #1f2937;
        padding: 1rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        margin-right: 20%;
        border: 2px solid #fed7aa;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #ea580c 0%, #fb923c 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #c2410c 0%, #ea580c 100%);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border: 2px solid #fed7aa;
        border-radius: 8px;
        padding: 0.5rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ea580c;
        box-shadow: 0 0 0 2px rgba(234, 88, 12, 0.2);
    }
    
    /* Login form styling */
    .login-container {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border: 1px solid #fed7aa;
        max-width: 400px;
        margin: 0 auto;
    }
    
    .logo-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .logo {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #ea580c 0%, #fb923c 100%);
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        margin-bottom: 1rem;
    }
    
    /* Timestamp styling */
    .timestamp {
        font-size: 0.8rem;
        color: #6b7280;
        margin-top: 0.5rem;
    }
    
    /* Success message */
    .success-message {
        background: #d1fae5;
        color: #065f46;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #10b981;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'is_typing' not in st.session_state:
    st.session_state.is_typing = False


def login_page():
    """Display the login page (Sign Up removed, static credentials)"""
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("""
        <div class="login-container">
            <div class="logo-container">
                <div class="logo">💬</div>
                <h2 style="color: #1f2937; margin: 0;">PolicyPal</h2>
                <p style="color: #6b7280; margin: 0.5rem 0 0 0;">Sign in to start chatting with our PolicyPal</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Only Login tab (Sign Up removed)
        with st.form("login_form"):
            st.subheader("Sign In")
            email = st.text_input("Email", placeholder="Enter your email")
            password = st.text_input(
                "Password", type="password", placeholder="Enter your password")

            if st.form_submit_button("Sign In", use_container_width=True):
                # Static credentials check
                if email == "test_user" and password == "pass@123":
                    st.session_state.authenticated = True
                    st.session_state.username = email
                    st.session_state.messages = [{
                        'sender': 'bot',
                        'text': f"Hello {st.session_state.username}! I'm your PolicyPal. How can I help you today?",
                        'timestamp': datetime.now()
                    }]
                    st.rerun()
                else:
                    st.error("Invalid username or password. Please try again.")


def chat_interface():
    """Display the main chat interface"""

    # Sidebar
    with st.sidebar:
        st.markdown(f"""
        <div style="text-align: center; padding: 1rem; color: white;">
            <h2>PolicyPal</h2>
            <div style="background: rgba(255,255,255,0.2); padding: 1rem; border-radius: 10px; margin: 1rem 0;">
                <div style="width: 40px; height: 40px; background: white; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; color: #ea580c; font-weight: bold; margin-bottom: 0.5rem;">
                    {st.session_state.username[0].upper()}
                </div>
                <p style="margin: 0; font-weight: 600;">{st.session_state.username}</p>
                <p style="margin: 0; font-size: 0.9rem; opacity: 0.8;">Online</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        if st.button("🚪 Sign Out", use_container_width=True):
            st.session_state.authenticated = False
            st.session_state.username = ""
            st.session_state.messages = []
            st.rerun()

    # Header
    st.markdown("""
    <div class="main-header">
        <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
            <div style="width: 40px; height: 40px; background: rgba(255,255,255,0.2); border-radius: 50%; display: flex; align-items: center; justify-content: center;">
                🤖
            </div>
            <div>
                <h3 style="margin: 0;">PolicyPal</h3>
                <p style="margin: 0; opacity: 0.9;">Always here to help</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Messages container
    messages_container = st.container()

    with messages_container:
        for message in st.session_state.messages:
            timestamp = message['timestamp'].strftime("%H:%M")

            if message['sender'] == 'user':
                st.markdown(f"""
                <div class="user-message">
                    <p style="margin: 0;">{message['text']}</p>
                    <div class="timestamp">{timestamp}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="bot-message">
                    <p style="margin: 0;">{message['text']}</p>
                    <div class="timestamp">{timestamp}</div>
                </div>
                """, unsafe_allow_html=True)

        if st.session_state.is_typing:
            st.markdown("""
            <div class="bot-message">
                <div style="display: flex; gap: 4px; align-items: center;">
                    <div style="width: 8px; height: 8px; background: #ea580c; border-radius: 50%; animation: bounce 1.4s infinite;"></div>
                    <div style="width: 8px; height: 8px; background: #ea580c; border-radius: 50%; animation: bounce 1.4s infinite 0.2s;"></div>
                    <div style="width: 8px; height: 8px; background: #ea580c; border-radius: 50%; animation: bounce 1.4s infinite 0.4s;"></div>
                </div>
            </div>
            <style>
                @keyframes bounce {
                    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                    40% { transform: translateY(-10px); }
                    60% { transform: translateY(-5px); }
                }
            </style>
            """, unsafe_allow_html=True)

    st.markdown("---")
    col1, col2 = st.columns([5, 1])

    # Clear input if flagged
    if 'clear_input' in st.session_state and st.session_state.clear_input:
        st.session_state.clear_input = False
        input_value = ""
    else:
        input_value = st.session_state.get("user_input", "")

    with col1:
        st.text_input(
            "Type your message...",
            key="user_input",
            value=input_value,
            label_visibility="collapsed"
        )

    with col2:
        send_button = st.button("Send", disabled=st.session_state.is_typing)

    # Message send logic
    if (send_button or st.session_state.get('user_input_submitted', False)) and st.session_state.user_input.strip() and not st.session_state.is_typing:
        user_input = st.session_state.user_input

        st.session_state.messages.append({
            'sender': 'user',
            'text': user_input,
            'timestamp': datetime.now()
        })

        # Trigger input clear on next render
        st.session_state.clear_input = True

        st.session_state.is_typing = True
        st.rerun()

    # Bot response
    if st.session_state.is_typing and len(st.session_state.messages) > 0 and st.session_state.messages[-1]['sender'] == 'user':
        time.sleep(1 + random.random() * 2)  # Simulate typing delay

        bot_response = query_lyzr_agent(st.session_state.messages[-1]['text'])
        st.session_state.messages.append({
            'sender': 'bot',
            'text': bot_response,
            'timestamp': datetime.now()
        })

        st.session_state.is_typing = False
        st.rerun()


# Main app logic
if not st.session_state.authenticated:
    login_page()
else:
    chat_interface()
