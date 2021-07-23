'''
You should use the statndard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful.
'''

import sys

'''
	The method below means that the program will read from input.txt, instead of standard(keyboard) input.
	To test your program, you may save input data in input.txt file,
	and call below method to read from the file when using open() method.
	You may remove the comment symbols(#) in the below statement and use it.
	But before submission, you must remove the open function or rewrite comment symbols(#).
'''

# inf = open('input.txt');
inf = sys.stdin

T = inf.readline()

for t in range(0, int(T)):

    Answer = 0
    num = int(inf.readline())
    ary = list(inf.readline().replace('\n', '').split(' '))
    i = 0
    while i < num:
        data = ary[i]
        if ary.count(data) == 1:
            Answer = Answer ^ int(data)
        i += 1


    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()