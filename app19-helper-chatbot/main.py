from helper_chatbot.helper_chatbot import HelperChatbot

topic = "Python programming"

knowledge_base = {
    "Python programming": "Python is a powerful programming language",
    "how do yoe define a function in Python": "you can define a function using the def keyword, "
                                              "followed by the function name, parentheses, and a colon",
    "data science": "Data Science is a multi-disciplinary field that uses scientific methods, processes, algorithms"
                    " and systems to extract knowledge and insights from structured and unstructured data.",
    "machine learning": "Machine learning is an application of artificial intelligence (AI) "
                        "that provides systems the ability to automatically learn and improve from experience "
                        "without being explicitly programmed.",
    "deep learning": "Deep learning is a subset of machine learning in artificial intelligence (AI) "
                     "that has networks "
}

if __name__ == "__main__":

    chatbot = HelperChatbot(topic, knowledge_base)

    print(chatbot.greet())

    while True:
        user_question = input("your question: ").strip()
        if user_question.lower() in ['exit', 'quit', 'bye']:
            print(chatbot.bye())
            break
        answer = chatbot.answer_question(user_question)
        print(f"Chatbot says: {answer}")
