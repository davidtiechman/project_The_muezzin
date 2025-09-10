def connect_words(text, related_words):
    for i in range(len(text)-1):
        if text[i] + text[i+1] in related_words:
            text[i] = text[i] + text[i+1]
    return text
