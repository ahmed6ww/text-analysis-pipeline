from langgraph.graph import StateGraph, END
# from langchain_core.runnables.graph import MermaidDrawMethod
from IPython.display import display, Image
from graph import classification_node, entity_extraction_node, summarization_node
from state import State

# Define the workflow
workflow = StateGraph(State)

# Add nodes to the graph
workflow.add_node("classification_node", classification_node)
workflow.add_node("entity_extraction", entity_extraction_node)
workflow.add_node("summarization", summarization_node)

# Set entry point and add edges
workflow.set_entry_point("classification_node")
workflow.add_edge("classification_node", "entity_extraction")
workflow.add_edge("entity_extraction", "summarization")
workflow.add_edge("summarization", END)

# Compile the graph
app = workflow.compile()

# Display graph
# display(
#     Image(
#         app.get_graph().draw_mermaid_png(
#             draw_method=MermaidDrawMethod.API,
#         )
#     )
# )



