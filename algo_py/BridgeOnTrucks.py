from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    waited_truck = deque(truck_weights)
    cur_bridge = [0] * bridge_length
    cur_weight = 0

    while cur_bridge:
        cur_weight -= cur_bridge.pop(0)
        if waited_truck:
            if(cur_weight + waited_truck[0]) <= weight:
                cur_weight += waited_truck[0]
                cur_bridge.append(waited_truck.popleft())
            else:
                cur_bridge.append(0)
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution(2, 10, [7, 4, 5, 6]))
    print(solution(9, 99, [2, 4, 12, 52, 4]))
