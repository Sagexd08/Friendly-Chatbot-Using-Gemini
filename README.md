# Friendly Chatbot

A **Friendly Chatbot** built in Python that leverages Google's Gemini Generative AI model to create engaging, empathetic, and context-aware conversations. Designed with a supportive personality, this chatbot is ideal for users seeking a friendly AI companion that remembers details, detects emotions, and adapts its responses with warmth and care.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Overview

This project, maintained by [sagexd08](https://github.com/sagexd08), is a Python-based chatbot that uses a combination of memory management, emotion detection, and a personality engine to simulate a natural conversation. By utilizing the Gemini model from [google-generativeai](https://github.com/google/generative-ai), the chatbot can generate thoughtful, contextually aware responses. It is designed to be easily extended and integrated into various applications.

---

## Features

- **Context Management:**  
  Uses a custom memory manager to store recent interactions, track common topics, and provide relevant conversation context. This helps maintain a continuous and meaningful dialogue.

- **Emotion Detection:**  
  Implements an emotion detection system that analyzes user inputs to determine emotions such as happy, sad, angry, curious, or grateful. The chatbot adjusts its responses based on these emotional cues.

- **Personality Engine:**  
  Enhances responses with appropriate emojis and a friendly tone. This engine adds a layer of personalization that makes interactions feel more human-like and engaging.

- **Gemini Generative AI Integration:**  
  Connects to Google's Gemini model through the `google-generativeai` package to generate natural, fluent responses. This integration allows the chatbot to handle a wide range of conversation topics effectively.

- **Input Sanitization:**  
  Sanitizes user inputs to remove problematic characters, ensuring safe and clean processing of the conversation.

- **Logging:**  
  Utilizes Python's `logging` module to record interactions and errors, aiding in debugging and performance monitoring.

---

## Project Structure

```
Friendly-Chatbot/
├── chatbot.py          # Main Python script with the chatbot implementation
├── chatbot.log         # Log file generated during runtime
├── LICENSE             # MIT License file
├── README.md           # This README file
└── requirements.txt    # List of Python dependencies
```

*Note: The file names and structure assume the main code is contained in `chatbot.py`.*

---

## Installation

### 1. Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/sagexd08/friendly-chatbot.git
cd friendly-chatbot
```

### 2. Set Up a Virtual Environment (Optional but Recommended)

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Make sure you have a `requirements.txt` file containing:

```txt
google-generativeai
textblob
```

Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

*Standard libraries (e.g., `datetime`, `json`, `logging`, etc.) are included with Python.*

---

## Usage

### 1. Configure Your API Key

Before running the chatbot, update the `API_KEY` variable in `chatbot.py` with your actual Google API key:

```python
API_KEY = "YOUR_ACTUAL_API_KEY"
```

### 2. Run the Chatbot

Launch the chatbot by running:

```bash
python chatbot.py
```

You should see a welcome message similar to:

```
👋 Hello! I'm your friendly AI companion! How can I help you today?
```

### 3. Interact with the Chatbot

Type your messages in the terminal. To exit, simply type `bye`, `goodbye`, `exit`, or `quit`.

---

## Configuration

- **Memory Manager:**  
  The chatbot stores a short-term conversation history (default up to 15 messages) and tracks topics using simple keyword matching. This allows the bot to refer back to earlier parts of the conversation.

- **Emotion Detection & Personality Engine:**  
  The `EmotionDetector` class scans user input for emotional keywords. The `PersonalityEngine` then adapts the response by appending suitable emojis and adjusting the tone to fit the detected emotion.

- **Input Sanitization:**  
  User input is sanitized using regular expressions to remove any potentially problematic characters before processing.

- **Logging:**  
  All significant actions and errors are logged to `chatbot.log` using Python’s `logging` module, making troubleshooting easier.

---

## Contributing

Contributions are welcome! If you’d like to contribute to the project:

1. **Fork the Repository:**  
   Click the "Fork" button on the top right of the repository page.

2. **Create a New Branch:**  
   Create a branch for your feature or bug fix:
   ```bash
   git checkout -b feature/my-new-feature
   ```

3. **Commit Your Changes:**  
   Make your changes and commit them:
   ```bash
   git commit -m "Add new feature or fix bug"
   ```

4. **Push Your Branch:**  
   Push your changes to GitHub:
   ```bash
   git push origin feature/my-new-feature
   ```

5. **Open a Pull Request:**  
   Open a pull request on GitHub to merge your changes.

For any questions or suggestions, please open an issue in the repository.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

**MIT License**

```
MIT License

Copyright (c) 2025 sagexd08

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Acknowledgements

- **Google Generative AI:**  
  Thanks to the [google-generativeai](https://github.com/google/generative-ai) package for providing the interface to the Gemini model.

- **TextBlob:**  
  Used for text processing and basic sentiment analysis.

- **Community Contributions:**  
  Thanks to everyone who has contributed ideas, bug reports, and enhancements.

- **sagexd08:**  
  This project is proudly maintained by [sagexd08](https://github.com/sagexd08).

---

Happy coding and enjoy building your friendly AI companion!
