import logging

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

if __name__ == "__main__":
    logging.info("Start simple AI chat")
    load_dotenv()
    llm = ChatOpenAI(model="gpt-4o-mini")

    while True:
        query = input("\n\n >> Enter your question: ")  # What was Nike's revenue in 2023?
        messages = [
            (
                "system",
                "You are a helpful assistant. You use three sentences maximum for answering and keep the answer concise. You are answering based on provided context."
                "If you don't know the answer, you just say that you don't know.",
            ),
            ("human", query),
        ]

        ai_answer = llm.invoke(messages)
        logging.info(f'AI ANSWER: {ai_answer.content}')
