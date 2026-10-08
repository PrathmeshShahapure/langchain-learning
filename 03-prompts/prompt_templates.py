from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

model=ChatGroq(model="openai/gpt-oss-120b",temperature=0.4)
prompt=ChatPromptTemplate.from_messages([
    ("system","you are a helfull programming teacher"),
    ("human", "Explain {topic} in simple terms.")
])

messages = prompt.invoke({"topic": "Event loop"})
response=model.invoke(messages)

# chain = prompt|model
# response=chain.invoke({"topic": "Event loop"})


print(response.content)