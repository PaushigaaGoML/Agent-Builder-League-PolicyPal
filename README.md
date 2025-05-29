# Agent-Builder-League-PolicyPal
PolicyPal is goML's in-house HR and policy assistant chatbot. It helps employees quickly understand company rules, employee benefits, HR procedures, compliance policies, and internal guidelines. Whether you're a new joiner or a senior employee, PolicyPal provides instant, accurate, and friendly responses based on official company documentation.

## Features

- **User Authentication**: Login functionality
- **Chat Interface**: Real-time chat with AI assistant
- **Beautiful UI**: Orange and white gradient theme
- **Responsive Design**: Works on all screen sizes
- **Typing Indicators**: Shows when AI is "thinking"
- **Message Timestamps**: Track conversation flow

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run main.py
```

3. Open your browser and navigate to `http://localhost:8501`

## Usage

1. **Authentication**: Start by logging in with existing credentials
2. **Chat**: Once logged in, start chatting with the AI assistant
3. **Navigation**: Use the sidebar to see your profile and sign out

## Features Overview

- **Login/Signup**: Secure authentication system
- **AI Responses**: Intelligent responses based on user input
- **Message History**: Keep track of your conversation
- **Real-time Updates**: Instant message delivery and responses

## Customization

The application uses custom CSS for styling. You can modify the colors and theme by editing the CSS in the `main.py` file under the `st.markdown()` section with custom styles.
