def average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


def passed_count(scores):
    return sum(score >= 60 for score in scores)
