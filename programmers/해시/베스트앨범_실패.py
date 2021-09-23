from collections import defaultdict


def solution(genres, plays):
    answer = []

    songs_dict = defaultdict(list)
    for i in range(len(genres)):
        if genres[i] not in songs_dict.keys():
            songs_dict[genres[i]] = [[i, plays[i]]]
        else:
            songs_dict[genres[i]].append([i, plays[i]])

    cand = []
    for lst in songs_dict.values():
        lst.sort(key=(lambda x: x[1]), reverse=True)
        cand.append(lst[:2])

    cand.sort(key=(lambda x: x[0][1]), reverse=True)

    for i in range(len(cand)):
        for j in range(len(cand[i])):
            answer.append(cand[i][j][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))