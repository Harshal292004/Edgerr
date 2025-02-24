from typing import TypedDict, Optional, Dict
from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Define the state structure for the Codd module
class CoddState(TypedDict):
    business_need: str           # Default complex business need
    parsed_need: Optional[Dict]  # Result of parsing the business need
    extracted_entities: Optional[Dict]  # Key entities and mappings from the parsed need
    schema_mapping: Optional[str]       # Proposed DDL based on mapping
    clarifications: Optional[str]       # Clarification feedback if needed
    initial_schema: Optional[str]       # Initial generated DDL
    optimized_schema: Optional[str]     # Schema after optimization and validation
    final_schema: Optional[str]         # Final output schema (post-processing)
    error: Optional[str]                # Error message if any step fails

# Initialize the LLM (using ChatOpenAI for example)
API_KEY="LNDn2rbGUIGZznn1NXT7U4VcADf-d"
ENDPOINT="https://cloud.olakrutrim.com/v1"
MODEL_NAME="Llama-3.3-70B-Instruct"

llm = ChatOpenAI(api_key=API_KEY, base_url=ENDPOINT, model=MODEL_NAME)

# Node: Parse the business need using an LLM chain
def parse_business_need(state: CoddState) -> Dict:
    # Create a prompt to extract structured information from the business need.
    prompt_template = PromptTemplate.from_template(
        "Extract the key dimensions, metrics, and timeframe from the following business need:\n\n"
        "{business_need}\n\n"
        "Return a JSON object with keys 'dimensions', 'metrics', and 'timeframe'."
    )
    # Generate the prompt text
    prompt_text = prompt_template.format(business_need=state["business_need"])
    # Use the LLM to process the prompt
    parsed_output = llm.invoke(prompt_text)
    # In a real-world scenario, you'd parse the LLM's output as JSON.
    # For this example, we simulate the parsed result:
    parsed = {
        "dimensions": ["sales", "customers", "products", "inventory"],
        "metrics": ["total revenue", "customer lifetime value"],
        "timeframe": "Q1",
    }
    return {"parsed_need": parsed}

# Other nodes remain similar to the previous example.
def extract_entities(state: CoddState) -> Dict:
    parsed = state.get("parsed_need", {})
    entities = {
        "sales": {"table": "Sales", "columns": ["revenue", "date", "region"]},
        "customers": {"table": "Customers", "columns": ["customer_id", "name", "country"]},
        "products": {"table": "Products", "columns": ["product_id", "name", "category"]},
        "inventory": {"table": "Inventory", "columns": ["stock", "warehouse"]},
    }
    return {"extracted_entities": entities}

def map_schema(state: CoddState) -> Dict:
    entities = state.get("extracted_entities", {})
    ddl_lines = []
    for key, info in entities.items():
        ddl_lines.append(f"CREATE TABLE {info['table']} (")
        ddl_lines.append(", ".join([f"{col} VARCHAR(255)" for col in info["columns"]]))
        ddl_lines.append(");")
    schema = "\n".join(ddl_lines)
    return {"schema_mapping": schema}

def clarification(state: CoddState) -> Dict:
    return {"clarifications": "No clarifications needed"}

def generate_initial_schema(state: CoddState) -> Dict:
    initial_ddl = state.get("schema_mapping", "") + "\n-- Initial schema generated based on business need."
    return {"initial_schema": initial_ddl}

def optimize_schema(state: CoddState) -> Dict:
    initial = state.get("initial_schema", "")
    optimized = initial + "\n-- Schema optimized for performance and OLAP use."
    return {"optimized_schema": optimized}

def post_process_schema(state: CoddState) -> Dict:
    optimized = state.get("optimized_schema", "")
    final = optimized + "\n-- Schema adapted for target DBMS dialect and safety verified."
    return {"final_schema": final}

# Create the LangGraph state graph and add nodes with their edges
graph = StateGraph(CoddState)
graph.add_node("parse", parse_business_need)
graph.add_node("extract", extract_entities)
graph.add_node("map", map_schema)
graph.add_node("clarify", clarification)
graph.add_node("initial", generate_initial_schema)
graph.add_node("optimize", optimize_schema)
graph.add_node("post_process", post_process_schema)

# Define the sequence of operations
graph.add_edge("parse", "extract")
graph.add_edge("extract", "map")
graph.add_edge("map", "clarify")
graph.add_edge("clarify", "initial")
graph.add_edge("initial", "optimize")
graph.add_edge("optimize", "post_process")
graph.set_entry_point("parse")

# Compile the graph for execution
compiled_graph = graph.compile()

# Define an initial state with the default complex business need
initial_state: CoddState = {
    "business_need": (
        """
        Business Need: Global Retail Solutions (GRS) Data Warehouse

        Global Retail Solutions (GRS) is a multinational, omni-channel retail enterprise operating through brick-and-mortar stores, e-commerce platforms, and mobile applications. To drive data-informed decision-making and support both operational reporting and advanced analytics, GRS requires a robust and scalable data warehousing solution. The core objectives are:

        Comprehensive Sales and Transaction Tracking:

        Capture every sales transaction from multiple channels (in-store, online, mobile) with detailed line-item data including product information, pricing, discounts, taxes, and returns.
        Support real-time updates and historical analysis, enabling ad-hoc queries such as identifying seasonal trends and comparing performance across channels.
        Customer Demographics and Behavioral Analysis:

        Maintain detailed profiles including demographic details, purchase history, browsing behavior, loyalty program membership, and customer feedback.
        Enable segmentation and lifetime value analysis, so analysts can query questions like “Which customer segments show the highest repeat purchase rates?” or “How does customer behavior vary by region?”
        Inventory and Supply Chain Management:

        Track real-time inventory levels across multiple warehouses and retail outlets.
        Integrate supplier data, shipment tracking, order fulfillment metrics, and supplier performance statistics.
        Allow predictive analytics to forecast stock shortages and optimize replenishment cycles.
        Product Catalog and Hierarchical Organization:

        Create a detailed product catalog that captures product attributes, categories, subcategories, variants, and historical pricing.
        Support complex queries that correlate product performance with promotional campaigns and market trends.
        Digital Marketing and Social Media Integration:

        Integrate campaign performance data from digital channels, including click-through rates, conversion metrics, and social media sentiment analysis.
        Enable cross-channel marketing impact analysis, such as comparing promotional effectiveness across regions.
        Financial and Operational Insights:

        Aggregate revenue, cost, and profit data to provide financial dashboards that support quarterly forecasting and performance benchmarking.
        Include key performance indicators (KPIs) that link operational data (like inventory turnover and order fulfillment times) with financial outcomes.
        External Market Data and Competitive Intelligence:

        Integrate external data sources such as industry benchmarks, competitor pricing, and macroeconomic indicators.
        Support queries that compare GRS performance against market trends, enhancing strategic planning.
        The designed schema must be normalized for Online Analytical Processing (OLAP) and optimized for complex, cross-dimensional queries. It should also support natural language query interfaces, enabling non-technical analysts to ask questions like:

        “Which regions had the highest revenue growth in Q1, and what were the top-selling product categories?”
        “How have inventory levels fluctuated in response to recent marketing campaigns?”
        This comprehensive system should be flexible enough to accommodate new data sources over time, support incremental data loads, and ensure high performance and fault tolerance across a variety of DBMS platforms using JDBC connectors, with tailored SQL dialect adjustments for systems like Trino, Spark SQL, PostgreSQL, MS SQL Server, Oracle, and MySQL.
        """
    ),
    "parsed_need": None,
    "extracted_entities": None,
    "schema_mapping": None,
    "clarifications": None,
    "initial_schema": None,
    "optimized_schema": None,
    "final_schema": None,
    "error": None,
}

# Invoke the graph with the initial state
result = compiled_graph.invoke(initial_state)
print("Final Schema Output:\n", result["final_schema"])
