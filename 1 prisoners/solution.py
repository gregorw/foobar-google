def solution(x, y):
    symmetric_difference = set(x) ^ set(y)
    return next(iter(symmetric_difference))
