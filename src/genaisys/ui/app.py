# streamlit run app.py
import sys
from pathlib import Path
import random

from genaisys.event_driven.save_conversation_history import save_conversation_history

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import streamlit as st
from genaisys.chat.chat import chat

# Page config
st.set_page_config(page_title="Generative AI Chat Interface", page_icon="🤖", layout="centered")

# Load CSS from external file
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = Path(__file__).parent / "styles.css"
load_css(css_path)

# Title
st.title("Generative AI Chat Interface")

# Security Alert (using session state to control visibility)
if "show_security_alert" not in st.session_state:
    st.session_state.show_security_alert = False

if st.session_state.show_security_alert:
    st.error("🚨 **Security Alert:** Suspicious activity detected.")

st.divider()

# User Selection
selected_user = st.selectbox("👤 User:", ["User01", "User02", "User03"])

# Checkboxes in a row
col_cb1, col_cb2, col_cb3 = st.columns(3)
with col_cb1:
    agent_enabled = st.checkbox("Agent", value=True)
with col_cb2:
    voice_output = st.checkbox("Voice Output")
with col_cb3:
    show_files = st.checkbox("Files")

# Reasoning Dropdown
reasoning_mode = st.selectbox(
    "🧠 Reasoning:",
    ["None",
     #"Analysis",
     #"Generation",
     #"Mobility"
     ]
)

# Model Dropdown
model_selection = st.selectbox(
    "🤖 Model:",
    ["OpenAI",
     "DeepSeek"
     ]
)

# ERP Integration Dropdown
erp_integration = st.selectbox(
    "🔗 ERP, database, platform and meeting integration: (Need to be implemented)",
    [
        "Select ERP, database, platform or Meeting API",
        "SAP",
        "Oracle",
        "AWS",
        "Zoom",
        "Teams",
        "Other"
    ]
)

# Initialize session state for user histories
if "user_histories" not in st.session_state:
    st.session_state.user_histories = {"User01": [], "User02": [], "User03": []}
if "pinecone_context" not in st.session_state:
    st.session_state.pinecone_context = ""
if "save_message" not in st.session_state:
    st.session_state.save_message = None

# Show save message if exists
if st.session_state.save_message:
    st.success(st.session_state.save_message)
    st.session_state.save_message = None

# Get current user's message history
messages = st.session_state.user_histories[selected_user]

# Message Input with Form (allows Enter to submit)
with st.form(key="message_form", clear_on_submit=True):
    user_message = st.text_input(
        "💬 Your Message:",
        placeholder="Type your message here or type 'exit' or 'quit' to end the conversation."
    )
    send_clicked = st.form_submit_button("📤 Send")

# Handle Send button click
if send_clicked and user_message:
    if user_message.lower() in ["exit", "quit"]:
        output_dir = save_conversation_history(st.session_state.user_histories)
        st.session_state.user_histories[selected_user] = []
        st.session_state.save_message = f"✅ Conversation history saved to {output_dir}"
        st.rerun()
    else:
        # Current message (separate from history)
        current_message = {"role": "user", "content": user_message, "username": selected_user}
        # History (previous messages only)
        history = messages.copy()
        # Show spinner while processing
        with st.spinner("Processing..."):
            # Process user message with history and current message separated
            response = chat(history, current_message, reasoning_mode, model_selection)

        # Add user message and assistant response to history
        messages.append(current_message)
        messages.append({"role": "assistant", "content": response})

        # Simulate Pinecone context retrieval
        if "Pinecone" in user_message or "RAG" in user_message:
            st.session_state.pinecone_context = f"Retrieved context for: {user_message[:50]}..."

# Output Area
st.markdown("### 📋 Conversation Output")

# Build conversation HTML with colored messages
conversation_html = '<div class="output-area">'
if messages:
    for msg in messages:
        if msg["role"] == "user":
            conversation_html += f'<div class="user-message"><strong>👤 {selected_user}:</strong> {msg["content"]}</div>'
        else:
            conversation_html += f'<div class="assistant-message"><strong>🤖 Assistant:</strong> {msg["content"]}</div>'
else:
    conversation_html += '<em>Conversation output will appear here...</em>'
conversation_html += '</div>'

st.markdown(conversation_html, unsafe_allow_html=True)

# Pinecone Results Panel
st.markdown("### 🔍 Context Retrieved from Pinecone")
st.markdown('<div class="pinecone-results">', unsafe_allow_html=True)
if st.session_state.pinecone_context:
    st.markdown(st.session_state.pinecone_context)
else:
    st.markdown("*No results yet.*")
st.markdown('</div>', unsafe_allow_html=True)

# Sidebar with additional info (optional)
with st.sidebar:
    st.markdown("### Settings")

    if st.button("⚠️ Toggle Security Alert"):
        st.session_state.show_security_alert = not st.session_state.show_security_alert
        st.rerun()

    if st.button("🗑️ Clear Conversation"):
        st.session_state.user_histories[selected_user] = []
        st.session_state.pinecone_context = ""
        st.rerun()