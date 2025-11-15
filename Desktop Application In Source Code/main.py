import tkinter as tk
import random
import time

# Generate 300 sentences of 20-24 words each
words_pool = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "python", "typing","speed", "test", "practice", "coding", "language", "keyboard", "skills", "improves", "fast", 
"errors", "help", "learn", "challenge", "fun", "game", "develop", "focus", "accuracy", "memory",
"typing", "interface", "design", "logic", "performance", "efficient", "clean", "code", "debug",
"optimize", "build", "collaborate", "project", "version", "control"]
def generate_sentence():
    length = random.randint(20, 24)
    sentence = random.choices(words_pool, k=length)
    sentence[0] = sentence[0].capitalize()  # Capitalize first word
    return " ".join(sentence) + "."
sentences = [generate_sentence() for _ in range(300)]
class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("800x300")
        self.sentence = ""
        self.start_time = 0
        self.label = tk.Label(root, text="Press Start to Begin", font=("Arial", 16), wraplength=780)
        self.label.pack(pady=20)
        self.entry = tk.Entry(root, font=("Arial", 16), width=80)
        self.entry.pack(pady=10)
        self.result = tk.Label(root, text="", font=("Arial", 14))
        self.result.pack(pady=20)
        self.start_btn = tk.Button(root, text="Start", command=self.start_test)
        self.start_btn.pack()
        self.entry.bind("<Return>", self.check_input)
    def start_test(self):
        self.sentence = random.choice(sentences)
        self.label.config(text=self.sentence)
        self.entry.delete(0, tk.END)
        self.entry.focus()
        self.result.config(text="")
        self.start_time = time.time()
        self.start_btn.config(state=tk.DISABLED)
    def check_input(self, event):
        typed_text = self.entry.get()
        elapsed = time.time() - self.start_time
        if typed_text == self.sentence:
            word_count = len(self.sentence.split())
            wpm = round(word_count / elapsed * 60)
            self.result.config(text=f"Correct! Time: {elapsed:.2f} sec | WPM: {wpm}")
            self.start_btn.config(state=tk.NORMAL)
        else:
            self.result.config(text="Incorrect, try again!")
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()
