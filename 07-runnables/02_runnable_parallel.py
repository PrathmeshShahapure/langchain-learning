from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv() 

promtTweet=PromptTemplate(template="Write a Tweet on {topic}",
                     input_variables=['topic'])

promtLinkedin=PromptTemplate(template="Write a Linkedin Post Content for {topic} ",
                     input_variables=['topic'])

model=ChatGroq(model="openai/gpt-oss-120b")

parser=StrOutputParser()

parallel_chain=RunnableParallel({ 'tweet':RunnableSequence(promtTweet,model,parser),'linkedin':RunnableSequence(promtLinkedin,model,parser)})

result =parallel_chain.invoke({'topic':'Icecream'})

print(result)

