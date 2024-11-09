import streamlit as st
from transformers import pipeline

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Function to generate response using the summarizer
def generate_response_with_summarizer(txt):
    try:
        # Generate summary
        summary = summarizer(txt, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        st.error(f"An error occurred during summarization: {str(e)}")
        return None

# Page title and layout
st.set_page_config(page_title='🦜🔗 Text Summarization App')
st.title('🦜🔗 Text Summarization App')

# Text input area for user to input text
txt_input = st.text_area('Enter your text', '', height=200)

# Form to accept the user's text input for summarization
response = None
with st.form('summarize_form', clear_on_submit=True):
    submitted = st.form_submit_button('Submit')
    if submitted and txt_input:
        with st.spinner('Summarizing...'):
            response = generate_response_with_summarizer(txt_input)

# Display the response if available
if response:
    st.info(response)

# Instructions for using the summarization app
st.subheader("Hugging Face Summarization")
st.write("""
This app uses Hugging Face's `facebook/bart-large-cnn` model to summarize input text.
The model provides concise summaries by capturing the main points of the text.
""")
