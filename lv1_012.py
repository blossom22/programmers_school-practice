# Programmers Lv1_012_하샤드 수 

def solution(x):
    a = sum(int(i) for i in str(x))
    return True if x%a == 0 else False