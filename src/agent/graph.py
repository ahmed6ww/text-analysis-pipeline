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
        "Analyze the following text in detail and classify it into one of the categories: News, Blog, Research, or Other. "
        "Consider the tone, structure, and content type of the text before making a decision.\n\n"
        "Text:\n{text}\n\n"
        "Please provide a clear category:"
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
