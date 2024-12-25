# Helper Chatbot

Helper Chatbot is a Python-based chatbot that can answer questions about the Python programming language. 
It uses the ChatterBot library to generate responses to user input.

## Features

* Text-to-speech functionality using 'pyttsx3' library. (Alternatively, you can use 'gTTS' library - google text-to-speech)
* Ability to answer questions based on a predefined knowledge base.
* Learns new answers from user input and saves them to a database file
* Provides suggestions for closely matching questions if an exact match is not found

## Requirements

* Python 3.6 or higher
* pyttsx3 library

## Installation

1. Clone the repository
    
2. Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the chatbot.py file:
```bash
python chatbot.py
```
2. The chatbot will greet you and prompt you to ask a question. Type your question and press Enter.
3. The chatbot will generate a response based on the knowledge base and display it to you.
4. If the chatbot does not know the answer to your question, it will provide suggestions for similar questions that it can answer.
5. You can also teach the chatbot new answers by typing in a question and its corresponding answer.
6. To exit the chatbot, type 'exit' and press Enter.
7. The chatbot will save the new answers to the database file and exit.
8. You can run the chatbot again to see the updated knowledge base.
9. Enjoy chatting with the Helper Chatbot!

## File Structure

* chatbot.py: Main script that runs the chatbot
* 'helper_chatbot/helper_chatbot.py': Helper class that contains the chatbot logic
* 'dictionary.json': JSON file containing the knowledge base of questions and answers
* 'requirements.txt': List of required libraries for the project


## Example

'''sh
$ python chatbot.py
Hello! I am the Helper Chatbot. How can I assist you today?
You: What is Python?
Python is an interpreted, high-level, general-purpose programming language.
You: What are the features of Python?
Python features a dynamic type system and automatic memory management.
You: exit
Goodbye! Have a great day!
'''

## Contributing

Contributions are welcome! Please feel free to submit a pull request if you have any improvements or new features to add.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
