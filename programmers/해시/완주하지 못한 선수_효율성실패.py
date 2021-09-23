def solution(participant, completion):
    answer = ''

    i = 0
    while i < len(participant) and completion:
        if participant[i] in completion:
            completion.remove(participant[i])
            del participant[i]
        else:
            i += 1

    answer += participant[0]

    return answer


print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
print()
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print()
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
