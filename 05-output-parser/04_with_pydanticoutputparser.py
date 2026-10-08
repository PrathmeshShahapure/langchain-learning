from langchain_groq import ChatGroq
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import PydanticOutputParser # here we  get flexiblity to enforce schema as well as validation
from pydantic import Field,BaseModel

load_dotenv() 

class Person(BaseModel):
    name:str=Field(description="generate the name of the person")
    age:int=Field(gt=18,lt=28,description="generate the age ")
    city: str = Field(description='Name of the city the person belongs to')

parser=PydanticOutputParser(pydantic_object=Person)

template=PromptTemplate(template='generate the user infromnation from {country}  \n {format_instruction}',
                        input_variables=['country'],
                        partial_variables={'format_instruction':parser.get_format_instructions()})

model=ChatGroq(model="openai/gpt-oss-120b")

chain= template | model | parser

result = chain.invoke({'country':'India'})
print(result)

