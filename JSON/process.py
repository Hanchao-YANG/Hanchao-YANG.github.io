import csv
import os
import json


STATE_CODE = [
    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
    "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
    "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
    "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
    "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY", "DC"
]
data = [None]*len(STATE_CODE)
for ind in range(len(STATE_CODE)):
    data[ind] = []
# data = [
#     [
#         {"name": "washinton", "lat": "33"},
#         {"name": "blacks", "lat": "37"}
#     ],
#     [
#         {"name": "wash", "lat": "33"},
#         {"name": "bb", "lat": "37"}
#     ]
# ]

with open("uscities.csv") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    counter = 0
    for row in spamreader:
        counter += 1
        if counter >= 2:
            state = row[2][1:-1]
            city = {
                "name": row[0][1:-1],
                "state": row[2][1:-1],
                "lat": row[8][1:-1],
                "lng": row[9][1:-1],
            }
            if (state in STATE_CODE):
                state_index = STATE_CODE.index(state)
                data[state_index].append(city)
            else:
                pass
                # print(state)

for state in STATE_CODE:
    file_name = state + ".json"
    state_index = STATE_CODE.index(state)
    print("writing " + str(state_index + 1) +  " " +file_name)
    with open(file_name, 'w') as outfile:
        json_obj = json.dumps(data[state_index])
        outfile.write(json_obj)
