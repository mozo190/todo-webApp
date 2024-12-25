import json


class HelperChatbot:
    def __init__(self, topic, knowledge_base, db_file="dictionary.db"):
        """
        Initializes the chatbot with a specific topic and a knowledge base.

        :param topic: str: The specific topic of the chatbot is knowledgeable about.
        :param knowledge_base: dict: A dictionary containing questions as keys and answers as values.
        :param db_file: str: The name of the database file to use for storing the knowledge base.
        """

        self.topic = topic
        self.knowledge_base = knowledge_base
        self.db_file = db_file
        self.loading_additional_data()

    def greet(self):
        """
        Greets the user when they start a conversation with the chatbot.
        """
        return f"Hello! I am a chatbot that knows about {self.topic}. How can I help you today?"

    def find_closest_match(self, question):
        """
        Finds the closest match to the user's question in the knowledge base.
        :param question: The user's question as a string.
        :return: A tuple containing the closest matching question and its answer, or None if no match is found.
        """
        question = question.lower()
        for key in self.knowledge_base:
            if question in key:
                return key, self.knowledge_base[key]
        return None

    def answer_question(self, question):
        """
        Answers a user's question based on the knowledge base.
        :param self:
        :param question: The user's question as a string.
        :return: The answer if found in the knowledge base, otherwise a message indicating the answer
         is not available or a default message. Prompts the user to provide an answer if the question is not found.
        """
        exact_answer = self.knowledge_base.get(question.lower())
        if exact_answer:
            return exact_answer

        closest_match = self.find_closest_match(question)
        if closest_match:
            return f'I think you might be asking about "{closest_match[0]}".\n Here is the answer: {closest_match[1]}'

        print("I'm sorry, I don't have an answer to that question.")
        new_answer = input("Please provide an answer to this question: ").strip()
        if new_answer:
            self.save_additional_data(question, new_answer)
            return "Thank you for providing an answer. I will remember that for next time."

        return "Alright, let me know if there is anything else I can help you with."

    def bye(self):
        """
        Says goodbye to the user when they end the conversation.

        """
        return "Thank you for chatting with me. Have a great day!"

    def loading_additional_data(self):
        """
        Loads additional data from the database file if it exists.
        """
        try:
            with open(self.db_file, "r", encoding="utf-8") as file:
                additional_knowledge = json.load(file)
                self.knowledge_base.update(additional_knowledge)
        except FileNotFoundError:
            with open(self.db_file, "w", encoding="utf-8") as file:
                json.dump({}, file)
        except json.JSONDecodeError:
            print("Error loading additional data from the database file.")
            return

    def save_additional_data(self, question, answer):
        """
        Saves additional data to the database file.

        """
        self.knowledge_base[question.lower()] = answer
        try:
            with open(self.db_file, "w", encoding="utf-8") as file:
                json.dump(self.knowledge_base, file, indent=4)
        except Exception as e:
            print(f"Error saving additional data to the database file: {e}")
            return
