# Prerequisites
Before testing, ensure you have the following installed:
- Ollama: Download and install it from ollama.com.
- Python 3.10+: Ensure Python is installed on your machine.
- Local LLM: You need at least one model downloaded. Open your terminal and run:
```
  ollama pull llama3
```
## How to Test the App
Follow these four steps to get the interface running:

1. Clone the Repository
Bash
git clone https://github.com/MrSplatchy/Ollama-Chatbot.git
cd Ollama-Chatbot
2. Install Dependencies
It is recommended to use a virtual environment. Run:
```
pip install ollama streamlit llama-index llama-index-llms-ollama
```
3. Start the Ollama Server
Ensure the Ollama application is running in the background. You can start it manually by running:

```
ollama serve
```
4. Run the Streamlit App
Launch the chatbot interface with the following command:
```
streamlit run app.py
```
5. Accessing the App
Once the command is running, Streamlit will provide a local URL (usually http://localhost:8501). Open this in your browser to start chatting with your local AI.
