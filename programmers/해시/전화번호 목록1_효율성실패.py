def solution(phone_book):
    answer = True

    phone_book.sort()
    for i in range(len(phone_book)):
        for p_n in phone_book[i + 1:]:
            if len(p_n) <= len(phone_book[i]) or p_n[0] != phone_book[i][0]:
                break
            if phone_book[i] in p_n:
                answer = False
                return answer

    return answer


print(solution(["119", "97674223", "1195524421"]))
print()
print(solution(["123", "456", "789"]))
print()
print(solution(["12", "123", "1235", "567", "88"]))