'''
You should use the statndard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful.
'''

import sys
import pdb
'''
	The method below means that the program will read from input.txt, instead of standard(keyboard) input.
	To test your program, you may save input data in input.txt file,
	and call below method to read from the file when using open() method.
	You may remove the comment symbols(#) in the below statement and use it.
	But before submission, you must remove the open function or rewrite comment symbols(#).
'''

#inf = open('input.txt');
inf = sys.stdin

T = inf.readline();
list = []

def find_words(string):

  h = string.count('h')
  list.append(h)

  e = string.count('e')
  list.append(e)

  l = string.count('l')/2
  list.append(l)

  o = string.count('o')
  list.append(o)

  minimum = min(list)
  #pdb.set_trace()

  if h>0 and e>0 and l>0 and o>0:
    return int(minimum)
  else:
    return 0


for t in range(0, int(T)):

  Answer=0;
  worrd = input()

  Answer = find_words(worrd)
  #############################################################################################
  #
  #  Implement your algorithm here.
  #  The answer to the case will be stored in variable Answer.
  #
  #############################################################################################

  # Print the answer to standard output(screen).
  print('Case #%d' %(int(t)+1))
  print(Answer)


inf.close()




