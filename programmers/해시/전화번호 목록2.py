def solution(phone_book):
    answer = True

    length = len(phone_book)
    phone_book.sort()
    for i in range(length - 1):
        if len(phone_book[i]) > len(phone_book[i]):
            continue
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            answer = False
            return answer
    return answer


print(solution(["119", "97674223", "1195524421"]))
print()
print(solution(["123", "456", "789"]))
print()
print(solution(["12", "123", "1235", "567", "88"]))