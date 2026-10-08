from langchain_groq import ChatGroq
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import JsonOutputParser # here we don't get flexiblity to enforce json schema 
load_dotenv() 

model=ChatGroq(model="openai/gpt-oss-120b", max_tokens=100)

parser = JsonOutputParser()
template=PromptTemplate(template='Write  2 facts on {topic} \n {format_instruction}',
                         input_variables=['topic'],
                         partial_variables={'format_instruction': parser.get_format_instructions()}
                         )   

# prompt = template.format()
# result=model.invoke(prompt)
# parser_result=parser.parse(result.content)
# print(parser_result)

chain= template | model | parser
result =chain.invoke({'topic':'trees'})
print(result)