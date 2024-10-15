import streamlit as st
from workflow import app  # Ensure 'app' is accessible

# Application Title
st.title("TextFusion: AI-Powered Text Analyzer")

# User Input
user_input = st.text_area("Enter the text you want to analyze:", height=200)

# Analyze Button
if st.button("Analyze Text"):
    if not user_input.strip():
        st.warning("Please enter some text to analyze.")
    else:
        try:
            with st.spinner("Analyzing..."):
                state_input = {"text": user_input}
                result = app.invoke(state_input)
            st.success("Analysis Complete!")

            # Display Results
            st.write("### Text Classification:")
            st.write(result["classification"])

            st.write("### Extracted Entities:")
            st.write(", ".join(result["entities"]))

            st.write("### Summary:")
            st.write(result["summary"])

        except Exception as e:
            st.error(f"An error occurred during analysis: {e}")
