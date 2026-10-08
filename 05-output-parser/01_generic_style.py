from langchain_groq import ChatGroq
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
load_dotenv() 

model=ChatGroq(model="openai/gpt-oss-120b")

template1=PromptTemplate(template='Write a detail report on {topic}',input_variables=['topic'])   

template2 = PromptTemplate(
    template='Write only 5 line summary on the following text. /n {text}',
    input_variables=['text']
)
prompt1=template1.invoke({'topic':'blackhole'})
result1=model.invoke(prompt1)

prompt2 = template2.invoke({'text':result1.content})
result2 = model.invoke(prompt2)

print(result2.content)