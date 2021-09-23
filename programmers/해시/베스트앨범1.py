from collections import defaultdict


def solution(genres, plays):
    answer = []

    songs = defaultdict(list)
    for i in range(len(genres)):
        if genres[i] not in songs.keys():
            songs[genres[i]] = [[i, plays[i]]]
        else:
            songs[genres[i]].append([i, plays[i]])

    how_many = dict()
    for k, v in songs.items():
        s = 0
        for i in range(len(v)):
            s += v[i][1]
        how_many[k] = s

    how_many = sorted(how_many.items(), key=lambda x: x[1], reverse=True)

    for k, lst in songs.items():
        lst.sort(key=lambda x: x[1], reverse=True)
        if len(lst) == 1:
            songs[k] = lst
        else:
            songs[k] = lst[:2]

    for g in how_many:
        for i in range(len(songs[g[0]])):
            answer.append(songs[g[0]][i][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print()
print(solution(["classic", "pop", "k-pop", "classic", "pop"], [600, 400, 150, 800, 900]))
print()
print(solution(["classic", "j-pop", "k-pop", "classic", "pop"], [500, 600, 150, 800, 2500]))
print()
print(solution(["classic", "pop", "classic", "classic", "classic"], [500, 1000, 400, 300, 200, 100]))