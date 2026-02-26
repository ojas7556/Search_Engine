import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

# -------------------- TOOLS SETUP --------------------

# Arxiv tool
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

# Wikipedia tool
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

# Web search tool
search = DuckDuckGoSearchRun(
    name="Search",
    description="Search the internet for recent information"
)

tools = [search, arxiv, wiki]

# -------------------- UI --------------------

st.title("LangChain - Chat with Search Agent")

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter Groq API key", type="password")

# Stop app if no key
if not api_key:
    st.info("Please enter Groq API key")
    st.stop()

# -------------------- CHAT MEMORY --------------------

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. Ask me anything!"}
    ]

# Display history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# -------------------- USER INPUT --------------------

if prompt := st.chat_input("Ask a question..."):

    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # -------------------- LLM --------------------

    llm = ChatGroq(
        groq_api_key=api_key,
        model_name="llama-3.1-8b-instant",
        streaming=True
    )

    # -------------------- AGENT --------------------

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=3,
        early_stopping_method="generate",
        handle_parsing_errors=True
    )

    # -------------------- RESPONSE --------------------

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)

        try:
            response = agent.run(prompt, callbacks=[st_cb])
        except Exception as e:
            response = f"Error: {e}"

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)