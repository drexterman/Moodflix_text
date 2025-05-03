from .utils import TextToEmotion

def text(input_text):
    model=TextToEmotion()
    if not input_text:
        input_text = input("Describe your mood in a sentence: ")
    text_mood_vector=model(input_text)
    return text_mood_vector
