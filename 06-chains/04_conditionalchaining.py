from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv() 

class Feedback(BaseModel):
    sentiment:Literal['Positive','Negative']=Field(description="Give the sentiment of the feedback")

py_parser=PydanticOutputParser(pydantic_object=Feedback)
st_parser=StrOutputParser()

template=PromptTemplate(template="""Classify the sentiment of the following feedback text into postive or negative 
                                 {feedback}
                                 {format_instruction} """,
                                 input_variables=['feedback'],
                                 partial_variables={'format_instruction':py_parser.get_format_instructions()}
                                 )

model=ChatGroq(model="qwen/qwen3.8-27b")

classifier_chain=template | model | py_parser #imp use pydantic parser to enforce the schema

prompt2 = PromptTemplate(
    template='Write one line response to  positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write one line response to negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain=RunnableBranch(
    (lambda x:x.sentiment == 'Positive' , prompt2 | model | st_parser),
    (lambda x:x.sentiment== 'Negative', prompt3 | model | st_parser),
    RunnableLambda(lambda x: "Could not find the Sentiment Sorry!!!")
)
chain =classifier_chain | branch_chain

print(chain.invoke({'feedback': 'that was a good exprience '}))


