from collections import deque


def solution(priorities, location):
    answer = 0
    dq = deque(priorities)

    while len(dq):
        if dq[0] == max(dq):    # 첫 값이 가장 우선순위가 높은 경우
            answer += 1
            dq.popleft()        # 바로 뺌
            if location == 0:   # 타겟 인덱스 0, 우선 순위가 가장 높다면 뺌
                return answer
            else:
                location -= 1   # 아니라면 값이 하나 빠졌으니 타겟 인덱스 감소
        else:
            dq.append(dq.popleft())
            if location == 0:
                location = len(dq) - 1
            else:
                location -= 1
    return answer


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
    print(solution([1, 6, 6, 3, 5, 5], 3))
