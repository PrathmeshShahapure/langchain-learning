from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv() 

promt=PromptTemplate(template="Write a joke on {topic}",
                     input_variables=['topic'])

model=ChatGroq(model="openai/gpt-oss-120b")

parser=StrOutputParser()

chain=RunnableSequence(promt,model,parser)

print(chain.invoke({'topic':'Icecream'}))
