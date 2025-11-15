import streamlit as st
import random
import time
# Generate 300 sentences of 20-24 words each
words_pool = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "python", "typing",
              "speed", "test", "practice", "coding", "language", "keyboard", "skills", "improves", "fast",
              "errors", "help", "learn", "challenge", "fun", "game", "develop", "focus", "accuracy", "memory",
              "typing", "interface", "design", "logic", "performance", "efficient", "clean", "code", "debug",
              "optimize", "build", "collaborate", "project", "version", "control"]
def generate_sentence():
    length = random.randint(20, 24)
    sentence = random.choices(words_pool, k=length)
    sentence[0] = sentence[0].capitalize()  # Capitalize first word
    return " ".join(sentence) + "."
sentences = [generate_sentence() for _ in range(300)]
if "sentence" not in st.session_state:
    st.session_state.sentence = ""
    st.session_state.start_time = None
    st.session_state.completed = False
st.title("Typing Speed Test")
def start_test():
    st.session_state.sentence = random.choice(sentences)
    st.session_state.start_time = time.time()
    st.session_state.completed = False
if st.button("Start Typing Test") or st.session_state.sentence == "":
    start_test()
st.write("Type the following sentence:")
st.markdown(f"**{st.session_state.sentence}**")
typed_text = st.text_input("Start typing and press Enter when done:")
if st.session_state.start_time and typed_text:
    if typed_text == st.session_state.sentence:
        elapsed = time.time() - st.session_state.start_time
        word_count = len(st.session_state.sentence.split())
        wpm = round(word_count / elapsed * 60)
        st.success(f"Correct! Time: {elapsed:.2f} seconds | WPM: {wpm}")
        st.session_state.completed = True
    else:
        st.error("Incorrect, please try again.")
if st.session_state.completed:
    if st.button("Restart Test"):
        start_test()
        st.rerun()
