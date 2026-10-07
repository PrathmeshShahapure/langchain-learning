from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage,HumanMessage
from dotenv import load_dotenv

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

messages=[SystemMessage(content="You are a Helpfull and friendly chatbot")]

while True:
    user_input=input("You: ")
    if user_input.lower()=="exit":
        print("GoodBye !!!")
        break
    human_msg=HumanMessage(content=user_input)
    messages.append(human_msg)

    ai_res=model.invoke(messages)
    messages.append(ai_res)

    print("AI:", ai_res.content[0]["text"])
