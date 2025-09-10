def calculate_document_score(word_scores, total_words):
    """
    word_scores: dict -> מילה/ביטוי : ציון
    total_words: int -> מספר כל המילים במסמך
    """
    # 1. סכום כל הנקודות של המילים/ביטויים
    total_points = sum(word_scores.values())

    # 2. חישוב ציון כולל למסמך (נורמליזציה לפי אורך הטקסט)
    doc_score = total_points / max(1, total_words)  # max(1,...) למניעת חלוקה באפס

    # 3. קביעת רמת איום לפי ספים
    if doc_score < 0.05:
        threat_level = "none"       # אין איום
    elif doc_score < 0.15:
        threat_level = "medium"     # איום בינוני
    else:
        threat_level = "high"       # איום גבוה

    # 4. מחזירים גם את הציון וגם את רמת האיום
    return {"doc_score": doc_score, "threat_level": threat_level}


# ===== דוגמה לשימוש =====
word_scores = {
    "genocide": 2,
    "war crimes": 2,
    "refugees": 2,
    "gaza": 1
}
total_words = 50  # לדוגמה, מספר כל המילים במסמך

result = calculate_document_score(word_scores, total_words)

print("Document score:", result["doc_score"])
print("Threat level:", result["threat_level"])
