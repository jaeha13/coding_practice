# 자연수 리스트(홀수와 짝수의 개수가 같음)가 주어집니다.(예외 처리 필요)
# 이 리스트를 정렬해야 합니다.
# 순서는 홀-짝-홀-짝-...으로 오게 해야 하며,
# 홀수는 오름차순 정렬로, 짝수는 내림차순 정렬로 배치해야 합니다.

## 함수
def numSort(arr):
    even, odd = [], []
    length = len(arr)
    if length % 2 != 0:
        print('개수 안맞음')
        return
    for n in arr:
        if n <= 0 or type(n) != int:
            print('자연수 아님')
            return
        elif n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)
    if len(even) != len(odd):
        print('개수 안맞음')
        return
    even.sort(reverse=True)
    odd.sort()
    result = []
    for i in range(length):
        if i % 2 == 0:
            result.append(odd[0])
            del odd[0]
        else:
            result.append(even[0])
            del even[0]
    print(result)
    return result


## 전역
import random
ary1 = [4, 1, 3, 2, 6, 5]
ary1_1 = [4, 1.2, 3, 2, 6, 5]
ary1_2 = [4, 1, 3, 2, 6, -5]
ary2 = [random.randint(1, 10) for _ in range(10)]
ary3 = [random.randint(1, 10) for _ in range(10)]
ary4 = [random.randint(1, 10) for _ in range(10)]
ary5 = [1, 2, 3, 4, 5, 6, 7]

## 메인
print(ary1)
numSort(ary1)
print(ary1_1)
numSort(ary1_1)
print(ary1_2)
numSort(ary1_2)
print(ary2)
numSort(ary2)
print(ary3)
numSort(ary3)
print(ary4)
numSort(ary4)
print(ary5)
numSort(ary5)