from pydantic import BaseModel, Field
from typing import TypedDict, Optional, Dict,Annotated ,List ,Literal
from typing import TypedDict, Optional, Dict,Annotated ,List ,Literal
from langgraph.graph import StateGraph ,START,END
from langchain_openai import ChatOpenAI
from langchain_groq import  ChatGroq
from langchain.prompts import PromptTemplate
from langgraph.graph.message import  add_messages
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import  MessagesState
from langchain_core.messages import HumanMessage,SystemMessage ,AnyMessage, AIMessage
from pydantic import  BaseModel,Field
from Prompts import  Prompts


# CODD MODELS
class Decision(BaseModel):
    state: Annotated[Literal["Complete", "Incomplete"], Field(description="Anlyse the conversation correctly")]

class TechincalPreProcessing(BaseModel):
    pass


class BuisnessNeedPreProcessed(BaseModel):    
    messages:Optional[Annotated[List[AnyMessage], add_messages, Field(description="Conversations as stored")]]=None
    processed_technical_conversions:Optional[Annotated[TechincalPreProcessing,Field(description="")]] = None
    
    
class CoddState(BaseModel):
    business_need: Optional[Annotated[BuisnessNeedPreProcessed, Field(description="Original raw business need text as provided by the client")]] = None


# STONEBREAKER MODELS