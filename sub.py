import re

phone_no = '(212)-456-7890'
pattern = '\D'
result = re.sub(pattern, ' ', phone_no)

print(result)