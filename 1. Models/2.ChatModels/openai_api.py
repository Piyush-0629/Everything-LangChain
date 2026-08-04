from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature = 0.1)

result = model.invoke("Name 5 life insurance company in india?")

print(result.content)