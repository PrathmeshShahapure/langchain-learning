from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel,Field

json_schema={
"type": "object",
"properties": {
"product_name": {
"type": "string",
"title": "Product Name"
},
"sentiment": {
"enum": ["pos", "neg", "neutral"],
"title": "Sentiment",
"type": "string"
},
"pros": {
"default": [],
"description": "write down the pros of the review",
"items": {
"type": "string"
},
"title": "Pros",
"type": ["array", "null"]
},
"cons": {
"items": {
"type": "string"
},
"title": "Cons",
"type": "array"
},
"rating": {
"description": "Give rating by analysing overall review if user didn't give any specific review else note the user original review",
"title": "Rating",
"type": "number"
},
"key_themes": {
"description": "write down all keywords discussed in a review",
"items": {
"type": "string"
},
"title": "Key Themes",
"type": "array"
}
},
"required": [
"product_name",
"sentiment",
"cons",
"rating",
"key_themes"
],
"title": "Review"
}

load_dotenv()
model=ChatGroq(model="openai/gpt-oss-120b")

struture_output=model.with_structured_output(json_schema)

response =struture_output.invoke(" i recently bought the Zenith X5 Noise-Cancelling Headphones. und quality is absolutely stunning with deep bass and crisp highs. The noise cancellation is the best I've ever experienced, making them perfect for my long commutes.The so However, the headband feels a bit tight after wearing them for more than two hours, and the companion app is quite buggy. Overall, a solid 4.5/5 for the audio performance alone. ")

print(response) #response will be pydantic object so 
dic_res=dict(response)
print(dic_res['cons'])
print(dic_res['rating'])