import time
from collections import Counter

import keyboard
from colorama import Fore, Style


class TypingAnalyzer:
    def __init__(self):
        self.word_buffer = ""
        self.word_count = Counter()
        self.running = True

    def on_key_event(self, event):
        if event.event_type == "down":
            if event.name == "space":
                self.add_word()
            elif event.name == "backspace":
                self.word_buffer = self.word_buffer[:-1]
            elif len(event.name) == 1 and event.name.isprintable():
                self.word_buffer += event.name

    def add_word(self):
        if self.word_buffer and self.word_buffer.isalpha():  # Only add words that are not empty and contain letters
            self.word_count[self.word_buffer] += 1
            self.word_buffer = ""

    # Save the results to a file
    def save_results_to_file(self, filename="typing_results.txt"):
        with open(filename, 'w') as file:
            file.write("Most typed words this session:\n")
            for word, count in self.word_count.most_common():
                file.write(f"{word}: {count}\n")
        print(f"Results saved to {filename}")

    def print_top_words(self):
        print(Fore.CYAN + "\nMost typed words this session:" + Style.RESET_ALL)  # Print typed words colored in cyan
        for word, count in self.word_count.most_common():
            print(Fore.GREEN + f"{word}: {count}" + Style.RESET_ALL)  # Print typed words colored in green

    def start(self):
        print(Fore.YELLOW +
              "Typing analyzer started. Press space to add a word, "
              "backspace to delete a character, and Ctrl+C to exit." + Style.RESET_ALL)
        keyboard.hook(self.on_key_event)
        while self.running:
            time.sleep(0.1)
            if keyboard.is_pressed('esc'):
                self.add_word()
                self.running = False
                self.print_top_words()
                self.save_results_to_file()
                print(Fore.RED + "Exiting typing analyzer." + Style.RESET_ALL)  # Print exit message in red
