def solution(n, lost, reserve):
    answer = 0
    clothes = [1] * n

    for i in reserve:
        clothes[i-1] += 1

    for i in lost:
        clothes[i-1] -= 1

    for i in range(len(clothes)):
        if 0 < i and clothes[i] == 0 and clothes[i-1] > 1:
            clothes[i] += 1
            clothes[i-1] -= 1
        elif i < n - 1 and clothes[i] == 0 and clothes[i+1] > 1:
            clothes[i] += 1
            clothes[i+1] -= 1

    for i in range(len(clothes)):
        if clothes[i] != 0:
            answer += 1

    return answer  # n - clothes.count(0) 으로 집계 가능


if __name__ == '__main__':
    print(solution(5, [2, 4], [1, 3, 5]))
    print(solution(5, [2, 4], [3]))
    print(solution(3, [3], [1]))
