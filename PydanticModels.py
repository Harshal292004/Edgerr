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
class IsContextEnough(BaseModel):
    isEnough: Annotated[bool, Field(description="Is the sql context enough")]


class FixContext(BaseModel):
    context:Annotated[str, Field(description="Fixed context")]
    

class Query(BaseModel):
    query:Annotated[str,Field(description="")]
    

class OptimizedQuery(BaseModel):
    query:Annotated[str,Field(description="")]
    
class FinalEvaluation(BaseModel):
    evaluation:Annotated[bool,Field(description="")]    

class StoneBreakerState(BaseModel):
    data_base:Optional[Annotated[str,Field(description="")]]=None
    sql_context:Optional[Annotated[str,Field(description="")]]=None
    sql_prompt:Optional[Annotated[str,Field(description="")]]=None
    sql_context_from_vector_store:Optional[Annotated[str,Field(description="")]]=None
    sql_query_generated:Optional[Annotated[str,Field(description="")]]=None
    sql_query_optimized:Optional[Annotated[str,Field(description="")]]=None
    executed_success:Optional[Annotated[bool,Field(description="")]]=None
    execution_results:Optional[Annotated[str,Field(description="")]]=None
    final_evaluation:Optional[Annotated[bool,Field(description="Is the query appropriate in regards to the sql prompt and context")]]=None
    trino_sql:Optional[Annotated[str,Field(description="")]]=None
    spark_sql:Optional[Annotated[str,Field(description="")]]=None
    error:Optional[Annotated[str,Field(description="")]]=None
    
