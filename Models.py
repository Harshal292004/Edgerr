from langchain_openai import ChatOpenAI  

class Models:
    """.env"""
    @staticmethod
    def get_llama(api_key="LNDn2rbGUIGZznn1NXT7U4VcADf-d",endpoint="https://cloud.olakrutrim.com/v1",model_name="Llama-3.3-70B-Instruct"):
        """
        API
        """
        return ChatOpenAI(
            api_key=api_key,
            base_url=endpoint,
            model=model_name
        )
    