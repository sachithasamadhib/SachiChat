### SachiChat

SachiChat is a simple, elegant chatbot application powered by Google's Gemini AI. This Streamlit-based web application allows users to have natural conversations with an AI assistant.





## Features

- 💬 Interactive chat interface
- 🧠 Powered by Google's Gemini AI model
- 🚀 Built with Streamlit for a responsive web experience
- 🔄 Conversation history maintained during session
- 🎨 Clean and intuitive user interface


## Installation

### Prerequisites

- Python 3.7 or higher
- A Google Gemini API key


### Setup

1. Clone the repository:


```shellscript
git clone https://github.com/yourusername/sachi_chat.git
cd sachi_chat
```

2. Install the required dependencies:


```shellscript
pip install -r requirements.txt
```

3. Configure your Google Gemini API key:

1. Create a `.streamlit/secrets.toml` file (if not already present)
2. Add your API key to the file:


```plaintext
GOOGLE_GEMINI_KEY = "your-api-key-here"
```




## Usage

1. Start the Streamlit application:


```shellscript
streamlit run main.py
```

2. Open your web browser and navigate to the URL displayed in your terminal (typically `http://localhost:8501`)
3. Start chatting with the AI assistant by typing your message in the input field and pressing Enter


## Configuration

The application uses a `.streamlit/secrets.toml` file to store the Google Gemini API key. You can obtain an API key by:

1. Visiting [Google AI Studio](https://ai.google.dev/)
2. Creating an account or signing in
3. Navigating to the API section to generate a key
4. Adding the key to your `secrets.toml` file


## Development

### Running in a Development Container

This project includes a devcontainer configuration for Visual Studio Code, making it easy to set up a consistent development environment:

1. Install the "Remote - Containers" extension in VS Code
2. Open the project folder in VS Code
3. Click on the green button in the bottom-left corner and select "Reopen in Container"


## Technologies Used

- [Streamlit](https://streamlit.io/) - The web application framework
- [Google Generative AI](https://ai.google.dev/) - The AI model powering the chat functionality
- [Python](https://python.org/) - The programming language


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Future Enhancements

- Add support for image inputs
- Implement conversation saving functionality
- Create a more customizable UI
- Add multiple AI model options


## Contact

Project Link: [https://github.com/yourusername/sachi_chat](https://github.com/yourusername/sachi_chat)
