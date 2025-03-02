import streamlit as st
import requests

# Page configuration must be the first Streamlit command
st.set_page_config(page_title="Langgraph AI Agent", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for styling with dark theme
st.markdown("""
    <style>
    /* Global dark theme styles */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        font-family: 'Inter', sans-serif;
        color: #e6e6e6;
    }

    /* Title and subtitle */
    .title {
        font-size: 2.8em;
        font-weight: 800;
        color: #7b68ee;
        text-align: center;
        margin-bottom: 0.3em;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
    }
    .subtitle {
        font-size: 1.3em;
        color: #a9a9a9;
        text-align: center;
        margin-bottom: 2em;
    }

    /* Input fields */
    .stTextArea textarea {
        border: 2px solid #7b68ee;
        border-radius: 12px;
        padding: 12px;
        background-color: #16213e;
        font-size: 1.05em;
        color: #e6e6e6;
    }
    .stTextArea textarea:focus {
        border-color: #9370db;
        box-shadow: 0 0 8px rgba(123, 104, 238, 0.6);
    }

    /* Radio buttons, checkboxes, and selectboxes */
    .stRadio > div {
        background-color: #1f2833;
        border-radius: 10px;
        padding: 10px;
    }
    .stRadio > div > div > label {
        color: #e6e6e6 !important;
    }
    .stCheckbox > div > div > label {
        color: #e6e6e6 !important;
    }
    .stSelectbox > div > div {
        background-color: #1f2833;
        border: 1px solid #7b68ee;
        border-radius: 10px;
    }
    .stRadio > label, .stCheckbox > label, .stSelectbox > label, .stTextArea > label {
        font-size: 1.15em;
        color: #c5c5c5;
        font-weight: 500;
        margin-bottom: 8px;
    }

    /* Button */
    .stButton button {
        background: linear-gradient(90deg, #7b68ee 0%, #9370db 100%);
        color: white;
        border-radius: 25px;
        padding: 12px 24px;
        font-size: 1.2em;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
        width: 100%;
        margin-top: 10px;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #9370db 0%, #7b68ee 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.3);
    }

    /* Response box */
    .response-box {
        background-color: #1f2833;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        margin-top: 25px;
        border-left: 5px solid #7b68ee;
    }

    /* Dividers and sections */
    .section-divider {
        border-top: 1px solid #444;
        margin: 20px 0;
    }

    .section-header {
        color: #7b68ee;
        font-size: 1.4em;
        font-weight: 600;
        margin: 10px 0;
    }

    /* Custom container */
    .custom-container {
        background-color: #1f2833;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
    }

    /* Status indicator */
    .status-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
    }
    .status-online {
        background-color: #32CD32;
    }
    </style>
""", unsafe_allow_html=True)

# Header with logo and status
col_logo, col_title, col_status = st.columns([1, 10, 1])
with col_title:
    st.markdown('<div class="title">Langgraph AI Agent</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Your intelligent assistant powered by LLMs</div>', unsafe_allow_html=True)

with col_status:
    st.markdown('<div style="text-align: right; margin-top: 15px;"><span class="status-indicator status-online"></span><span style="font-size: 0.9em;">Online</span></div>', unsafe_allow_html=True)

# Main container
with st.container():
    st.markdown('<div class="section-header">Agent Configuration</div>', unsafe_allow_html=True)

    # System prompt input with improved styling
    with st.expander("Define Your AI Agent", expanded=True):
        system_prompt = st.text_area(
            "System Prompt",
            height=120,
            placeholder="You are a helpful AI assistant specialized in...",
            key="system_prompt",
            help="This defines the personality and capabilities of your AI agent"
        )

    # Model selection with improved styling
    st.markdown('<div class="custom-container">', unsafe_allow_html=True)
    MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
    MODEL_NAMES_OPENAI = ["gpt-4o-mini", "gpt-4o", "gpt-4-turbo"]

    provider = st.radio("Model Provider:", ["Groq", "OpenAI"], horizontal=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if provider == "Groq":
            selected_model = st.selectbox("Model:", MODEL_NAMES_GROQ)
        else:
            selected_model = st.selectbox("Model:", MODEL_NAMES_OPENAI)
    with col2:
        allow_web_search = st.checkbox("Enable Web Search", value=True)
        st.caption("Allow the agent to search the web for information")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Your Query</div>', unsafe_allow_html=True)

    # User query input
    user_query = st.text_area(
        "What would you like to ask?",
        height=150,
        placeholder="Type your question or request here...",
        key="user_query"
    )

    # Submit button
    if st.button("Generate Response"):
        if not user_query.strip():
            st.error("Please enter a query before submitting.")
        else:
            with st.spinner("AI agent is thinking..."):
                payload = {
                    "model_name": selected_model,
                    "model_provider": provider,
                    "system_prompt": system_prompt,
                    "messages": [user_query],
                    "allow_search": allow_web_search
                }
                API_URL = "http://127.0.0.1:9999/chat"

                try:
                    response = requests.post(API_URL, json=payload)
                    if response.status_code == 200:
                        response_data = response.json()
                        if "error" in response_data:
                            st.error(response_data["error"])
                        else:
                            st.markdown('<div class="response-box">', unsafe_allow_html=True)
                            st.markdown("### Agent Response")
                            st.markdown(response_data)
                            st.markdown('</div>', unsafe_allow_html=True)

                            # Show thinking process in an expander (if available)
                            if "thinking" in response_data:
                                with st.expander("View Agent's Thinking Process"):
                                    st.markdown(response_data.get('thinking', ''))
                    else:
                        st.error(f"API request failed with status code: {response.status_code}")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error connecting to the API: {str(e)}")
                    st.info("Make sure the backend server is running at http://127.0.0.1:9999")

# Footer
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; margin-top: 30px; color: #888; font-size: 0.8em;">Powered by Langgraph and LLMs • Made with ❤️</div>', unsafe_allow_html=True)
