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
    ####################################################################################################################################
    num = int(inf.readline())
    ary = tuple(inf.readline().replace('\n', '').split(' '))
    ary_1 = set()
    ary_2 = set()
    for i in range(num):
        data = ary[i]
        if data not in ary_1:
            ary_1.add(data)
        elif data not in ary_2:
            ary_2.add(data)

    ary_result = ary_1 - ary_2
    for e in ary_result:
       Answer = Answer ^ int(e)
    ####################################################################################################################################

    # Print the answer to standard output(screen).
    print('Case #%d' % (int(t) + 1))
    print(Answer)
inf.close()

"""
element in collection 는 collection 에 데이터가 존재하는 지 확인하는 것으로
list 는 O(n) 의 실행속도를 갖지만 set 은 O(1) 으로 매우 빠르다!
"""