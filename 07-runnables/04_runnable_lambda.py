from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableLambda,RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv() 

def wordCounter(text):
    return len(text.split())

promt=PromptTemplate(template="Write a joke on {topic}",
                     input_variables=['topic'])

model=ChatGroq(model="openai/gpt-oss-120b")

parser=StrOutputParser()

joke_chain=RunnableSequence(promt,model,parser)

parallel_chian=RunnableParallel({'joke':RunnablePassthrough(),'toal_words':RunnableLambda(wordCounter)})

final_chain=RunnableSequence(joke_chain | parallel_chian)
print(final_chain.invoke({'topic':'Cricket'}))
