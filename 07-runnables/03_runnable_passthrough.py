from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv() 

promt=PromptTemplate(template="Write a joke on {topic}",
                     input_variables=['topic'])
promtExplainJoke=PromptTemplate(template="{topic} -Explain this joke to me in very simple and understanding way.",
                     input_variables=['joke'])

model=ChatGroq(model="openai/gpt-oss-120b")

parser=StrOutputParser()

joke_gen_chain=RunnableSequence(promt,model,parser)
parallel_chain=RunnableParallel({'joke':RunnablePassthrough(),'joke_explanation':RunnableSequence(promtExplainJoke,model,parser)})

final_res=RunnableSequence(joke_gen_chain,parallel_chain)

print(final_res.invoke({'topic':'IceCream'}))

