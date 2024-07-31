import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate

from config_extraction import ConfigExtraction

os.environ["GOOGLE_API_KEY"] = ConfigExtraction().AI_STUDIO_KEY

# # Basic example 1
# llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
# result = llm.invoke("Write a ballad about LangChain")
# print(result.content)


# # Example 2
# llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
# result = llm.invoke(
#     [
#         SystemMessage(content="Answer only yes or no."),
#         HumanMessage(content="Is apple a fruit?"),
#     ]
# )
# print(result.content)

# # Example 3
# llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
# messages = [
#     (
#         "system",
#         "You are a helpful assistant that translates English to French. Translate the user sentence.",
#     ),
#     ("human", "I love programming."),
# ]
# result = llm.invoke(messages)
# print(result.content)



# # # Example 4 - Chaining
# llm = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a helpful assistant that translates {input_language} to {output_language}.",
#         ),
#         ("human", "{input}"),
#     ]
# )

# chain = prompt | llm
# result = chain.invoke(
#     {
#         "input_language": "English",
#         "output_language": "German",
#         "input": "I love programming.",
#     }
# )
# print(result.content)


# Example 5
llm = ChatGoogleGenerativeAI(model="gemini-pro")
result = llm.invoke(
    """
        Prompt
    """
)
print(result.content)