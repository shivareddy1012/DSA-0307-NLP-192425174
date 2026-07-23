import re

text = "Natural Language Processing is interesting"
pattern = "Language"

result = re.search(pattern, text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")
