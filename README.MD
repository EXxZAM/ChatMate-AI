# ChatMate AI

ChatMate AI is a user-friendly chatbot application that leverages OpenAI's powerful GPT-3.5 language model to provide interactive conversations. With ChatMate AI, users can engage in natural language conversations by entering prompts and receiving AI-generated responses.

## Features

-   **Speech Recognition**: ChatMate AI supports voice input through the device's microphone, enabling hands-free interaction with the chatbot.
-   **Multilingual Support**: Choose from a variety of language options for both input prompts and AI-generated responses.
-   **Text-to-Speech**: Listen to the chatbot's responses as audio through text-to-speech conversion.
-   **Copy and Save**: Easily copy the chatbot's responses to the clipboard or save them as text files for future reference.

## Description

ChatMate AI is a GUI-based program that provides an intuitive and seamless experience for interacting with an AI chatbot. By integrating OpenAI's GPT-3.5 language model, ChatMate AI delivers highly contextual and human-like responses to user prompts.

Whether you need assistance with tasks, have questions, or simply want to engage in conversational interactions, ChatMate AI is designed to cater to your needs. The application supports both Persian and English languages, allowing users to communicate in their preferred language.

ChatMate AI is built on Python, utilizing the Tkinter library to create a visually appealing and user-friendly interface. The application's functionality extends beyond text-based interactions, as it incorporates speech recognition capabilities for effortless voice input.

## Prerequisites

-   Python 3.7 or higher
-   OpenAI API key
-   Internet connection

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/ChatMate-AI.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ChatMate-AI
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory and add your OpenAI API key:

    ```text
    OPENAI_API_KEY=your-api-key
    ```

## Usage

1. Run the application:

    ```bash
    python chatmate.py
    ```

2. Enter a prompt in the provided text area or click the microphone button to use voice input.

3. Select the language for input prompts and AI-generated responses from the dropdown menu.

4. Click the "Process" button or press Enter to send the prompt to the chatbot.

5. View the AI-generated response in the text area below.

6. To pause the text-to-speech playback of the response, click the pause button.

7. Use the "Clear" button to remove the entered prompt text.

8. Click the "Paste" button to insert text from the clipboard into the prompt text area.

9. To regenerate the prompt and receive a new response, click the "Regenerate" button.

10. To copy the AI-generated response to the clipboard, click the "Copy" button.

11. To save the AI-generated response as a text file, click the "Save" button and choose a location to save the file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

-   This application utilizes OpenAI's GPT-3.5 language model. For more information, visit the [OpenAI website](https://openai.com/).
-   The graphical user interface is created using the Tkinter library for Python.

## Disclaimer

This application is provided as-is without any warranty. Usage of this application may be subject
