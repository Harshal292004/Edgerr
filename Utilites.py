class Models:
    def  __init__():
        self.KRUTRIM_API_KEY="LNDn2rbGUIGZznn1NXT7U4VcADf-d"
        self.KRUTRIM_ENDPOINT="https://cloud.olakrutrim.com/v1"
        self.MODEL_NAME="Llama-3.3-70B-Instruct"
        self.EVALUATION_MODEL_NAME="Llama-3.3-70B-Instruct"
        self.GROQ_API_KEY="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"
        self.GROQ_MODEL_NAME="llama-3.3-70b-versatile"
    
    
    def get_structured_llm(provider="GROQ"):
        groq_llm= ChatGroq(groq_api_key=GROQ_API_KEY,model_name= GROQ_MODEL_NAME)
        groq_evaluation_llm= ChatGroq(groq_api_key=GROQ_API_KEY,model =GROQ_MODEL_NAME)
        groq_evaluation_llm=groq_evaluation_llm.with_structured_output(schema=Decision)
    