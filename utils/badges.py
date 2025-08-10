def calculate_badges(scores):
    badges = []
    high_scores = [s for s in scores if s["score"] >= 80]
    if len(high_scores) >= 5:
        badges.append("Consistent High Performer")
    topics = set(s["topic"] for s in scores)
    if len(topics) >= 10:
        badges.append("Explorer")
    return badges

def calculate_streak(scores):
    from datetime import datetime, timedelta
    dates = sorted(set(datetime.strptime(s["date"], "%Y-%m-%d") for s in scores))
    streak = 1
    for i in range(len(dates)-1, 0, -1):
        if dates[i] - dates[i-1] == timedelta(days=1):
            streak += 1
        else:
            break
    return streak

def rank_badge(score):
    if score >= 90:
        return "🥇 Gold"
    elif score >= 75:
        return "🥈 Silver"
    elif score >= 60:
        return "🥉 Bronze"
    else:
        return "🎓 Participant"
