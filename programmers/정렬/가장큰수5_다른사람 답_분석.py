def solution(numbers):
    answer = ''
    # numbers 를 str 으로 바꾸기
    numbers = list(map(str, numbers))
    # 세자리 수가 최대 x * 3 ex) '3' --> '333' vs '30' --> '303030' : '333'이 큼
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # numbers 문자열 합치고 저장
    answer = str(int(answer.join(numbers))) # [0, 0, 0, 0] --> '0' 으로 처리하기 위함
    return answer


print(solution([0]))     # 0
print()
print(solution([5]))     # 5
print()
print(solution([6, 10, 2]))     # 6210
print()
print(solution([3, 30, 34, 5, 9]))  # 9534330
print()
print(solution([3, 30, 31, 5, 9]))  # 9533130
print()
print(solution([3, 30, 31, 34, 9]))  # 93433130
print()
print(solution([909, 90, 908, 0, 0]))   # 9099090800
print()
print(solution([909, 90, 9, 0, 0]))   # 99099000