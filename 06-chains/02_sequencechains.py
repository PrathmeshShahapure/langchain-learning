from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

template1=PromptTemplate(template="Explain {topic} to a beginner in 2 sentences.",
                        input_variables=['topic']
                        )

template2=PromptTemplate(template="Based on this explanation, give a simple real-world analogy. {explanation}",
                         input_variables=['explanation'])

model =ChatGroq(model="openai/gpt-oss-120b")

parser=StrOutputParser();

chain=template1 | model | parser | template2 | model | parser; 
#you later want both the explanation and the analogy in the output use RunnablePassthrough.assign

result = chain.invoke({'topic':'Photosynthesis'})
print(result)

#chain.get_graph().print_ascii() # to get visiual graph of the chain use 