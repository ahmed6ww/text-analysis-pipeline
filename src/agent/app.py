import streamlit as st
import asyncio
from workflow import app as workflow_app  # Ensure 'app' is accessible

async def stream_workflow(user_input):
    state_input = {"text": user_input}
    version = "v1"  # Use your appropriate version

    try:
        async for event in workflow_app.astream_events(state_input, version=version):
            # Process the events here
            if event["event"] == "on_chain_end":
                if event["name"] == "classification_node":
                    classification = event["data"]["output"]["classification"]
                    st.write(f"**Text Classification:** {classification}")

                elif event["name"] == "entity_extraction":
                    entities = event["data"]["output"]["entities"]
                    entities_display = ", ".join(entities) if entities else "No entities found."
                    st.write(f"**Extracted Entities:** {entities_display}")

                elif event["name"] == "summarization":
                    summary = event["data"]["output"]["summary"]
                    st.write(f"**Summary:** {summary}")

    except Exception as e:
        st.error(f"An error occurred during streaming: {e}")

# Streamlit App Layout
def main():
    st.title("TextFusion: AI-Powered Text Analyzer")
    user_input = st.text_area("Enter the text you want to analyze:", height=200)

    if st.button("Analyze Text"):
        if not user_input.strip():
            st.warning("Please enter some text to analyze.")
        else:
            st.spinner("Analyzing...")  # You can show a spinner during streaming
            asyncio.run(stream_workflow(user_input))

if __name__ == "__main__":
    main()

# app.py

# import streamlit as st
# import asyncio
# from workflow import app as workflow_app  # Ensure 'app' is accessible
# # from langgraph.schema import GraphEvent

# # Function to handle streaming and updating the UI
# async def stream_workflow(user_input, placeholders):
#     """
#     Streams events from the LangGraph workflow and updates Streamlit placeholders.

#     Args:
#         user_input (str): The input text from the user.
#         placeholders (dict): Dictionary containing Streamlit placeholders.
#     """
#     state_input = {"text": user_input}
    
#     # Specify the version here. Replace 'v1' with your actual version if different.
#     version = "v1"
    
#     try:
#         # Correct method call without 'mode' parameter
#         async for event in workflow_app.astream_events(state_input, version=version):
#             # Debugging: Uncomment the next line to see raw events
#             # st.write(event)
            
#             # Handle events based on their type and node name
#             if event["event"] == "on_chain_start" and event["name"] == "classification_node":
#                 placeholders["classification"].markdown("**Text Classification:** Processing...")
            
#             elif event["event"] == "on_chain_end" and event["name"] == "classification_node":
#                 classification = event["data"].get("classification", "N/A")
#                 placeholders["classification"].markdown(f"**Text Classification:** {classification}")
            
#             elif event["event"] == "on_chain_start" and event["name"] == "entity_extraction":
#                 placeholders["entities"].markdown("**Extracted Entities:** Processing...")
            
#             elif event["event"] == "on_chain_end" and event["name"] == "entity_extraction":
#                 entities = event["data"].get("entities", [])
#                 entities_display = ", ".join(entities) if entities else "No entities found."
#                 placeholders["entities"].markdown(f"**Extracted Entities:** {entities_display}")
            
#             elif event["event"] == "on_chain_start" and event["name"] == "summarization":
#                 placeholders["summary"].markdown("**Summary:** Processing...")
            
#             elif event["event"] == "on_chain_end" and event["name"] == "summarization":
#                 summary = event["data"].get("summary", "N/A")
#                 placeholders["summary"].markdown(f"**Summary:** {summary}")
            
#             # Optionally, handle other events for debugging or progress indication
#             elif event["event"].startswith("on_chain"):
#                 # Example: Log other events if needed
#                 pass

#     except Exception as e:
#         placeholders["error"].markdown(f"**Error:** {str(e)}")

# # Streamlit App Layout
# def main():
#     st.set_page_config(page_title="TextFusion: AI-Powered Text Analyzer", page_icon="💬")
#     st.title("💬 TextFusion: AI-Powered Text Analyzer")
    
#     # User Input
#     user_input = st.text_area("Enter the text you want to analyze:", height=200)
    
#     # Analyze Button
#     if st.button("Analyze Text"):
#         if not user_input.strip():
#             st.warning("Please enter some text to analyze.")
#         else:
#             # Create placeholders for streaming outputs
#             classification_placeholder = st.empty()
#             entities_placeholder = st.empty()
#             summary_placeholder = st.empty()
#             error_placeholder = st.empty()  # Placeholder for errors
            
#             placeholders = {
#                 "classification": classification_placeholder,
#                 "entities": entities_placeholder,
#                 "summary": summary_placeholder,
#                 "error": error_placeholder
#             }
            
#             with st.spinner("Analyzing..."):
#                 try:
#                     # Run the asynchronous streaming function
#                     asyncio.run(stream_workflow(user_input, placeholders))
#                     st.success("Analysis Complete!")
#                 except Exception as e:
#                     st.error(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()
