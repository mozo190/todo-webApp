class HelperChatbot:
    def __init__(self, topic, knowledge_base):
        """
        Initializes the chatbot with a specific topic and a knowledge base.

        :param topic: str: The specific topic of the chatbot is knowledgeable about.
        :param knowledge_base: dict: A dictionary containing questions as keys and answers as values.
        """

        self.topic = topic
        self.knowledge_base = knowledge_base

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
         is not available or a default message.
        """
        exact_answer = self.knowledge_base.get(question.lower())
        if exact_answer:
            return exact_answer

        closest_match = self.find_closest_match(question)
        if closest_match:
            return f'I think you might be asking about "{closest_match[0]}".\n Here is the answer: {closest_match[1]}'

        return "I'm sorry, I don't have an answer to that question."

    def bye(self):
        """
        Says goodbye to the user when they end the conversation.

        """
        return "Thank you for chatting with me. Have a great day!"
