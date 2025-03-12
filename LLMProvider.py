from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
class LLMProvider:
    def __init__(self):
        self.KRUTRIM_API_KEY = "LNDn2rbGUIGZznn1NXT7U4VcADf-d"
        self.KRUTRIM_ENDPOINT = "https://cloud.olakrutrim.com/v1"
        self.MODEL_NAME = "Llama-3.3-70B-Instruct"
        self.EVALUATION_MODEL_NAME = "Llama-3.3-70B-Instruct"
        self.GROQ_API_KEY = "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"
        self.GROQ_MODEL_NAME = "llama-3.3-70b-versatile"

    def get_structured_llm(self, structured_output_schema, model_name="", provider="GROQ"):
        model_name = model_name or (self.GROQ_MODEL_NAME if provider == "GROQ" else self.MODEL_NAME)
        llm = (
            ChatGroq(groq_api_key=self.GROQ_API_KEY, model_name=model_name)
            if provider == "GROQ"
            else ChatOpenAI(api_key=self.KRUTRIM_API_KEY, base_url=self.KRUTRIM_ENDPOINT, model=model_name)
        )
        return llm.with_structured_output(schema=structured_output_schema)

    def get_llm(self, model_name="", provider="GROQ"):
        model_name = model_name or (self.GROQ_MODEL_NAME if provider == "GROQ" else self.MODEL_NAME)
        return (
            ChatGroq(groq_api_key=self.GROQ_API_KEY, model_name=model_name)
            if provider == "GROQ"
            else ChatOpenAI(api_key=self.KRUTRIM_API_KEY, base_url=self.KRUTRIM_ENDPOINT, model=model_name)
        )