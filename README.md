# Friday - your AI Conversational Assistant 

A sophisticated AI-powered conversational assistant built with ElevenLabs voice synthesis and OpenAI integration, featuring web search capabilities and dynamic content generation.

## Features

- **Voice Conversations**: Natural speech-to-speech interactions using ElevenLabs Conversational AI
- **Web Search Integration**: Real-time web search capabilities using DuckDuckGo
- **Content Generation**: AI-powered image generation using DALL-E 3
- **File Management**: Save conversations and generate HTML reports
- **Visual Interface**: Beautiful web-based UI with cool cat animations

##  Tech Stack

- **Backend**: Python with ElevenLabs SDK
- **AI/ML**: OpenAI GPT, DALL-E 3
- **Web Interface**: HTML5, CSS3, JavaScript
- **Audio**: PyAudio for audio processing
- **Search**: DuckDuckGo Search API

##  Prerequisites

- Python 3.7+
- ElevenLabs API key
- OpenAI API key
- Microphone and speakers for voice interactions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/friday.git
cd friday
```

2. Install dependencies:
```bash
pip install -r requirement.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory:
```env
AGENT_ID=your_elevenlabs_agent_id
ELEVENLABS_API_KEY=your_elevenlabs_api_key
OPENAI_API_KEY=your_openai_api_key
```

## 🎯 Usage

### Starting the Conversation
```bash
python main.py
```

The assistant will start listening for voice input and respond with synthesized speech.

### Available Tools

- **Web Search**: Ask questions and get real-time web results
- **Image Generation**: Create custom images with DALL-E 3
- **File Saving**: Save conversations to text files
- **HTML Reports**: Generate beautiful HTML summaries

### Example Interactions

- "Search for the latest AI news"
- "Generate an image of a futuristic city"
- "Save this conversation to a file"
- "Create an HTML report of our discussion"


## 📁 Project Structure

```
friday/
├── main.py              # Main application entry point
├── tools.py             # Custom tools and functions
├── cool_cats.html       # Visual web interface
├── requirement.txt      # Python dependencies
├── .env                 # Environment variables (create this)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## 🔍 API Integration

### ElevenLabs Conversational AI
- Real-time voice synthesis
- Natural conversation flow
- Custom agent configuration

### OpenAI Services
- **DALL-E 3**: High-quality image generation
- **GPT Models**: Advanced text understanding and generation

### DuckDuckGo Search
- Privacy-focused web search
- Real-time information retrieval

## 🚀 Getting Started

1. **Setup Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirement.txt
   ```

2. **Configure API Keys**:
   - Get your ElevenLabs API key from [elevenlabs.io](https://elevenlabs.io)
   - Get your OpenAI API key from [openai.com](https://openai.com)

3. **Run the Application**:
   ```bash
   python main.py
   ```

## 🎮 Interactive Features

- **Voice Commands**: Speak naturally to interact with the AI
- **Visual Feedback**: See real-time transcriptions and responses
- **File Output**: Save conversations and generated content
- **Web Integration**: Access current information from the web

## 🔧 Development

### Adding New Tools
Extend the functionality by adding new tools in `tools.py`:

```python
def new_tool(parameters):
    # Your custom functionality
    return result

client_tools.register("newTool", new_tool)
```

### Customizing the Interface
Modify `cool_cats.html` to change the visual appearance:
- Update CSS styles
- Add new animations
- Change color schemes

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

For questions or support:
- Open an issue on GitHub
- Check the documentation
- Join our community discussions

## 🗺️ Roadmap

- [ ] Multi-language support
- [ ] Advanced conversation memory
- [ ] Custom voice training
- [ ] Real-time collaboration features

---

**Made with ❤️ by the Friday Team**
