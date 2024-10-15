from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from typing import TypedDict

import langsmith
from configuration import llm

def classification_node(state: dict):
    '''Deeply analayze and classify the text into one of the categories: News, Blog, Research, or Other '''
    prompt = PromptTemplate(
    input_variables=["text"],
    template=(
        "Analyze the following text and classify it into one of the categories: News, Blog, Research, or Other.\n\n"
        "### Category Descriptions:\n"
        "- **News**: Articles that report on current events, characterized by factual and objective information.\n"
        "- **Blog**: Informal writings that express personal opinions or experiences, often in a conversational tone.\n"
        "- **Research**: Academic content presenting original findings or reviews of existing knowledge in a structured manner.\n"
        "- **Other**: Any content that does not fit into the above categories.\n\n"
        "If the text contains elements from multiple categories, select the one that best represents the main focus. "
        "Please provide your classification along with a brief explanation for your choice.\n\n"
        "Text:\n{text}\n\n"
        "Category:"
    )
)
    message = HumanMessage(content=prompt.format(text=state["text"]))
    classification = llm.invoke([message]).content.strip()
    
    return {"classification": classification}


def entity_extraction_node(state: dict):
    ''' Extract all the entities (Person, Organization, Location) from the text '''
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Extract all the entities (Person, Organization, Location) from the following text. Provide the result as a comma-separated list.\n\nText:{text}\n\nEntities:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    entities = llm.invoke([message]).content.strip().split(", ")
    return {"entities": entities}


def summarization_node(state: dict):
    ''' Summarize the text in one short sentence '''
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Summarize the following text in one short sentence.\n\nText:{text}\n\nSummary:"
    )
    message = HumanMessage(content=prompt.format(text=state["text"]))
    summary = llm.invoke([message]).content.strip()
    return {"summary": summary}
