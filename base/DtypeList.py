# Python List = STL Vector = Collection List

a = [1, 2, 3, 4, 5, 6]
print(a)

print(a[4])

a = list()
print(a)

a = []
print(a)

a = [1, 2, 3, 4, 5, 6]
print(a[-1])

print(a[1])

print(a[-3])

a[3] = 10
print(a)

print(a[1:4])

arr = [i for i in range(20) if i % 2 == 1]
print(arr)

arr = []
for i in range(20):
    if i % 2 == 1:
        arr.append(i)
print(arr)

arr = [i * i for i in range(20)]
print(arr)

# N * M 크기의 2차원 리스트 초기화
n, m = 3, 4
arr = [[0] * m for _ in range(n)]
print(arr)

# 특정 크기의 2차원 리스트 초기화 시 반드시 리스트 컴프리헨션 사용
# 사용 안할 시 동일 객체 인식
arr = [[0] * m] * n
print(arr)

arr[1][1] = 5
print(arr)

arr = [1, 4, 3, 2]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)
arr.count(3)
print(arr)
arr.insert(1, 10)
print(arr)
arr.reverse()
print(arr)

# 시간복잡도가 좋은 리스트에서 특정 원소 제외 방법
remove = {3, 4, 2}
arr = [i for i in arr if i not in remove] # remove에 없는 원소를 arr에 넣겠다
print(arr)
