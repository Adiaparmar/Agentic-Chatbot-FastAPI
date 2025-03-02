# LangGraph AI Agent 🤖

LangGraph AI Agent is a personal AI bot built using LangGraph, designed to interact with users for various applications. It leverages multiple language models (LLMs) to provide intelligent responses and can be configured according to user preferences.

## Technologies Used 🛠️

- **LangGraph**: A framework for building language model applications.
- **Streamlit**: Used for the frontend interface, providing an interactive UI.
- **FastAPI**: Serves as the backend, handling API requests.
- **Pydantic**: Facilitates data validation and settings management.
- **LangChain**: Integrates different LLMs like GPT-4 and Groq models.
- **Requests**: Handles HTTP requests for API communication.
- **Python dotenv**: Manages environment variables securely.

## Features ✨

- **Multiple Model Support**: Choose between Groq and OpenAI models.
- **Web Search Capability**: Allows the agent to search the web for additional information.
- **Customizable System Prompts**: Define the personality and capabilities of your AI agent.

## Usage 🚀

1. **Clone the Repository**:

```bash
git clone https://github.com/Adiaparmar/langgraph-ai-agent.git
cd langgraph-ai-agent
```

2. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your API keys:

```plaintext
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
OPENAI_API_KEY=your_openai_api_key
```

4. **Run the Application**:
   Start the backend server:

```bash
uvicorn backend:app --host 127.0.0.1 --port 9999
```

Open a new terminal for the frontend:

```bash
streamlit run frontend.py
```

## How to Use 🖥️

- Access the application via your browser at `http://localhost:8501`.
- Configure the AI agent via the interface by selecting a model and setting your system prompt.
- Enter your queries in the provided text area and submit to receive intelligent responses.

## Contributing 🤝

1. **Fork the Repository**:
   Click the "Fork" button at the top right of the repository page.

2. **Create a New Branch**:

```bash
git checkout -b feature-branch
```

3. **Make Changes and Commit**:

```bash
git add .
git commit -m "Add new feature"
```

4. **Push Your Changes**:

```bash
git push origin feature-branch
```

5. **Create a Pull Request**:
   Go to your forked repository, click on "Pull Request", and submit your changes for review.

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

_Created by [Adiaparmar](https://github.com/Adiaparmar)_
