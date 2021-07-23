import sys

'''
	The method below means that the program will read from input.txt, instead of standard(keyboard) input.
	To test your program, you may save input data in input.txt file,
	and call below method to read from the file when using open() method.
	You may remove the comment symbols(#) in the below statement and use it.
	But before submission, you must remove the open function or rewrite comment symbols(#).
'''

#inf = open('input.txt')
inf = sys.stdin

T = inf.readline()

for t in range(0, int(T)):
    Answer = 0
    num = int(inf.readline())
    ary = list(inf.readline().replace('\n', '').split(' '))
    print(ary)
    ary_result = []
    i = 0
    while ary and i < num:
        i = 0
        if ary.count(ary[i]) != 1:
            data = ary[i]
            while data in ary:
                ary.remove(data)
        else:
            ary_result.append(ary[i])
            ary.remove(ary[i])
        i += 1
    for x in range(len(ary_result)):
        Answer = Answer ^ int(ary_result[x])

    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()