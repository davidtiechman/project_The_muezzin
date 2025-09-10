def get_score(text,list_word_host,list_word_not_host):
    score = 0
    for word in text:
        if word in list_word_host:
            score += 2.0
        elif word in list_word_not_host:
            score += 1.0
    score /= len(text)
    return score


