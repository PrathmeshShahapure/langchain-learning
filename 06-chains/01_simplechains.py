from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

template=PromptTemplate(template="Write 2 facts about {topic}",
                        input_variables=['topic']
                        )

model =ChatGroq(model="openai/gpt-oss-120b")

parser=StrOutputParser();

chain=template | model | parser;

result = chain.invoke({'topic':'Cricket'})
print(result)

chain.get_graph().print_ascii() # to get visiual graph of the chain use 