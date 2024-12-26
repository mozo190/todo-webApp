from collections import Counter


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
        if self.word_buffer:
            self.word_count[self.word_buffer] += 1
            self.word_buffer = ""

    def print_top_words(self):
        print("\nMost typed words this session:")
        for word, count in self.word_count.most_common(10):
            print(f"{word}: {count}")
