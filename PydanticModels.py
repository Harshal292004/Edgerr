from pydantic import BaseModel, Field
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
from enum import Enum

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
class IsPromptRelated(BaseModel):
    isRelated: Annotated[bool, Field(description="Is the SQL prompt related")]

class Query(BaseModel):
    query: Annotated[str, Field(description="Generated SQL query")]

class OptimizedQuery(BaseModel):
    query: Annotated[str, Field(description="Optimized SQL query")]
    
class FinalEvaluation(BaseModel):
    evaluation: Annotated[bool, Field(description="Is the query appropriate for the SQL prompt and context")]

class DB_TYPES(Enum):
    POSTGRESS:"postgress"
    MYSQL:"mysql"
    MARIADB:"mariadb"
class DBConfigurations(BaseModel):
    db_type:Optional[Annotated[DB_TYPES, Field(description="Type fo the database")]] 
    db_username:Optional[Annotated[str,Field(description="Username of the database")]]
    db_password:Optional[Annotated[str,Field(description="Password of the database")]]
    db_host:Optional[Annotated[str,Field(description="Host of the database")]]
    db_port:Optional[Annotated[str,Field(description="Port of the database")]]
    db_name:Optional[Annotated[str,Field(description="Name of the database")]]
    db_connection_str:Optional[Annotated[str,Field(description="Connection string for database")]]
    
class StoneBreakerState(BaseModel):
    db_configurations: Optional[Annotated[DBConfigurations,Field(description="Database configurations")]]
    sql_context: Optional[Annotated[str, Field(description="SQL schema")]] = None
    sql_prompt: Optional[Annotated[str, Field(description="User SQL query prompt")]] = None
    sql_context_from_vector_store: Optional[Annotated[str, Field(description="SQL context retrieved from vector store")]] = None
    sql_query_generated: Optional[Annotated[str, Field(description="Generated SQL query")]] = None
    sql_query_optimized: Optional[Annotated[str, Field(description="Optimized SQL query")]] = None
    executed_success: Optional[Annotated[bool, Field(description="Query execution success status")]] = None
    execution_results: Optional[Annotated[str, Field(description="Results from query execution")]] = None
    final_evaluation: Optional[Annotated[bool, Field(description="Is the query appropriate for the SQL prompt and context")]] = None
    trino_sql: Optional[Annotated[str, Field(description="SQL query converted to Trino dialect")]] = None
    spark_sql: Optional[Annotated[str, Field(description="SQL query converted to Spark dialect")]] = None
    error: Optional[Annotated[str, Field(description="Error message if execution failed")]] = None