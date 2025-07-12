# Voice-Assistant-NOVA

Nova is a modern, voice-enabled AI chatbot built with Flask and powered by OpenRouter’s Claude-3 Haiku model. The interface is clean and responsive, offering support for voice input, spoken replies, multi-language conversation, and an animated sliding menu for chat history.

You can ask it anything — from jokes and general knowledge to weather updates — and it will respond like a human assistant.

## Features

- Smart conversation powered by Claude-3 Haiku (via OpenRouter)
- Voice-to-text input using your system’s microphone
- Bot reads replies aloud (text-to-speech)
- Supports English, Hindi, French, and Spanish
- Toggle between light and dark mode
- Slide-in chat history with individual delete options
- Weather response integrated — just ask “What’s the weather?”

## Tech Stack

**Frontend**
- HTML5
- CSS3
- JavaScript

**Backend**
- Python (Flask)

**APIs**
- OpenRouter (Claude-3 Haiku)
- Web Speech API (Browser)
- Optional: Weather API (built-in logic)

## How to Run Locally

1. Clone this repository
   git clone https://github.com/your-username/nova-ai-chatbot.git
   cd nova-ai-chatbot

2. Install Python dependencies

pip install flask requests pytz

3. Open `app.py` and replace this with your API key:

```python
API_KEY = "your-openrouter-api-key"
```

4. Run the server
python app.py

5. Open your browser and go to:
http://localhost:5000

Example Prompts to Try

1. Tell me a joke
2. What’s the weather like in Mumbai?
3. Explain quantum computing
4. Translate “hello” to French
5. Who won the last FIFA World Cup?

Folder Structure
nova-ai-chatbot/
│
├── templates/
│   └── index.html      # Main frontend file
├── app.py              # Flask backend logic
└── README.md           # Project guide

Note
Weather functionality is handled dynamically through the Claude model. You don’t need a separate button — just ask it naturally.

Make sure your browser allows microphone access for voice input.

Best experienced in Chrome or Edge for full Web Speech API support.

📝 License
This project is licensed under the MIT License.


