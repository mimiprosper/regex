import re

# #text = 'this_is-Python_Check'

text1 = 'the_boy-lives in spain'

text2 = re.split('_', text1)

for t in text2:
    text2 = re.split('-', t)
    
    for t1 in t:
        print(t1, end='')

