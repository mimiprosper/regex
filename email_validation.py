import re

emails = [
        'mike@.com',
        'emma@gmail.com',
        'joe.chidi@com.ng', 
        'fred@com',
        'williams.com',
          ]

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

for email in emails:
    if (re.fullmatch(regex, email)):
        print(f' {email} : valid')
    else:
        print(f' {email} : invalid')

