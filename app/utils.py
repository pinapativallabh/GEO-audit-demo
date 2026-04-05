def calculate_score(title, meta, headings, image):
    score = 0

    if title:
        score += 25
    if meta:
        score += 25
    if headings:
        score += 25
    if image:
        score += 25

    return score