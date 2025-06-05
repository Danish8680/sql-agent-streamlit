# gui_streamlit.py
import streamlit as st
from agent_core import get_sql_agent_response # Import the agent function you just created

# Set basic page configuration
st.set_page_config(
    page_title="Natural Language SQL Agent",
    layout="centered", # Can be "wide" for more space
    initial_sidebar_state="collapsed" # Options: "auto", "expanded", "collapsed"
)

# --- Title and Description ---
st.title("Ask Your Database Anything!")
st.markdown("""
    Type your natural language questions below to get answers directly from the **Chinook MySQL database**.
    Try questions like:
    * "How many Album are there in the database?"
    * "Describe the PlaylistTrack table"
    * "How many employees are there"
    * "Which country's customers spent the most by invoice?"
    * "Can you left join table Artist and table Album by ArtistId? Please show me 5 Name and AlbumId in the joint table."
""")

# --- Input Area ---
# `st.session_state` can be used to manage widget state across reruns,
# but for simple input, `text_area` and a button are usually enough.
user_prompt = st.text_area("Enter your question:", height=100, key="prompt_input")

# --- Submit Button ---
if st.button("Ask SQL Agent"):
    if user_prompt:
        # Display a spinner while the agent is processing the request
        with st.spinner("Thinking... Generating SQL and fetching data..."):
            response = get_sql_agent_response(user_prompt)

        # --- Output Area ---
        st.subheader("Agent Response:")
        # Use st.success for positive results, st.error for errors, etc.
        if "An error occurred:" in response:
            st.error(response)
        elif "No answer found." in response:
            st.warning(response)
        else:
            st.success(response)
    else:
        st.warning("Please enter a question in the text area above to get an answer.")

st.markdown("---")
st.info("Powered by LangChain, Ollama (local LLM), and MySQL.")