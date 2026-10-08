from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal

#  we can't do datavalidation in typedDict
class Review(TypedDict):
    product_name:str
    sentiment:Literal["pos","neg","neutral"]
    pros:Annotated[Optional[list[str]],"write down the pros of the review"]
    cons:list[str]
    rating:Annotated[float,"Give rating by analysing overall review if user didn't give any specific review else note the user original rview "]
    key_themes:Annotated[list[str],"write down all keywords discussed in a review"]



load_dotenv()
model=ChatGroq(model="openai/gpt-oss-120b")

struture_output=model.with_structured_output(Review)

response =struture_output.invoke(" i recently bought the Zenith X5 Noise-Cancelling Headphones. The sound quality is absolutely stunning with deep bass and crisp highs. The noise cancellation is the best I've ever experienced, making them perfect for my long commutes. However, the headband feels a bit tight after wearing them for more than two hours, and the companion app is quite buggy. Overall, a solid 4.5/5 for the audio performance alone. ")

print(response)
print(response['cons'])
print(response['rating'])