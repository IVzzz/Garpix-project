import os

for i in os.walk('../var/tmp/hackathon/data1/'):
    for itm in i[1]:
        for items in itm[0]:
            print(items)

