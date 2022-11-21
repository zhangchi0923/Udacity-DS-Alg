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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


tele_num_dict = set()
idx = 0
while idx < len(texts):
    tele_num_dict.update([texts[idx][0], texts[idx][1]])
    idx += 1
idx = 0
while idx < len(calls):
    tele_num_dict.update([calls[idx][0], calls[idx][1]])
    idx += 1

print("There are {} different telephone numbers in the records.".format(len(tele_num_dict)))
# There are 570 different telephone numbers in the records.
