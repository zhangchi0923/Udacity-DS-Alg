"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

from collections import defaultdict
t_dict = defaultdict(lambda: 0)
# for i in range(len(calls)):
#     if calls[i][0] in t_dict:
#         t_dict[calls[i][0]] += int(calls[i][3])
#     else:
#         t_dict[calls[i][0]] = int(calls[i][3])

#     if calls[i][1] in t_dict:
#         t_dict[calls[i][1]] += int(calls[i][3])
#     else:
#         t_dict[calls[i][1]] = int(calls[i][3])
for call in calls:
    t_dict[call[0]] += int(call[3])
    t_dict[call[1]] += int(call[3])
k_max = list(t_dict.keys())[list(t_dict.values()).index(max(list(t_dict.values())))]
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(k_max, t_dict[k_max]))
# (080)33251027 spent the longest time, 90456 seconds, on the phone during September 2016.
