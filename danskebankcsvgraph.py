import csv, sys
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
        
dates = []
amount = []

with open(sys.argv[1], newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    first = True
    for row in spamreader:
        if first:
            first = False
            continue
        date = datetime.strptime(row[0], '%d.%m.%Y')
        dates.append(date)
        amount.append(float(row[3].replace('.', '').replace(',', '.')))

plt.plot(dates, amount)
plt.yticks(np.arange(0, max(amount)+1, 5000))

plt.show()

