"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


chk_set = set()
res = set()
for i in range(len(texts)):
    chk_set.update([texts[i][0], texts[i]][1])
for j in range(len(calls)):
    chk_set.add(calls[j][1])

for k in range(len(calls)):
    if calls[k][0] not in chk_set:
        res.add(calls[k][0])

print("These numbers could be telemarketers: ")
for num in sorted(res):
    print(num)
