def generate_related_words(list_word):
    related_words = [word for word in list_word if ' ' in word]
    return related_words