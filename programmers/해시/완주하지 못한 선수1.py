def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()
    for i, j in zip(participant, completion):
        if i != j:
            answer += i
            return answer
    answer += participant.pop()
    return answer


print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
print()
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print()
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
