from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 

load_dotenv()
model=ChatGoogleGenerativeAI(model="gemini-3.7-flash",temperature=0.2)
response=model.invoke("Explain Recursion in simple terms.")

print(response)


## tempreature
# # 0.0 → more deterministic
# 0.2 → focused
# 0.7 → more creative
# 1.0+ → more variation

# max_output_tokens=500
# It doesn't mean the model will always generate 500 tokens—it sets the upper limit.