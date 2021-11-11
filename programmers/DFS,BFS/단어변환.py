def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    def check(begin, target, words, visited_, diff):
        if begin == target:
            return 1

        if visited_ == words:
            return 0

        if begin in visited_:
            return 0

        if begin in words:
            visited_.append(begin)
            words.remove(begin)
            return 1

        min_diff = diff
        for w in words:
            if len(set(w) - set(begin)) == 1:
                if min_diff > len(set(w) - set(target)):
                    min_diff = len(set(w) - set(target))

        for w in words:
            if len(set(w) - set(begin)) == 1:
                if w not in visited_ and len(set(w) - set(target)) == min_diff:
                    diff = min_diff
                    check(w, target, words, visited_, diff)

    visited = []
    for w in words:
        if begin != target:
            diff = len(set(begin) - set(target))
            answer += check(w, target, words, visited, diff)
    answer += 1

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print()
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))