class Tools:
    @staticmethod 
    def exit_conversation():
        exit()    
        pass
    
    
    
input_messages = [SystemMessage(Prompts.gen_analysis_business_need())]
print(input_messages) 
print("="*20)   
try:
    output = graph.invoke({"business_need": {"messages":input_messages}}, config)
except Exception as err:
    print(err)