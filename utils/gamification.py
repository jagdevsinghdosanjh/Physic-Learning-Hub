def calculate_xp(scores):
    return sum(int(s["score"]) for s in scores)

def determine_level(xp):
    return xp // 100
