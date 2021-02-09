from collections import deque


def solution(priorities, location):
    answer = 0
    dq = deque(priorities)

    while len(dq):
        if dq[0] == max(dq):  # 우선순위 체크
            answer += 1
            dq.popleft()
            #  location 체크
            if location == 0:
                return answer
            else:
                location -= 1
        else:
            dq.append(dq.popleft())  # 우선순위가 높지 않다면 뒤로 보냄
            # location 체크, 다른 점은 0번이면 끝으로 갔을테니 최종 위치에서 하나씩 감소
            if location == 0:
                location = len(dq) - 1
            else:
                location -= 1
    return answer


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
    print(solution([1, 6, 6, 3, 5, 5], 3))
