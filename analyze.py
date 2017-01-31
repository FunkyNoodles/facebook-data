from dateutil.parser import *
import json
import time
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

json_file_name = 'D://Facebook/2016-01-28/json/messages.json'

allMessages = {}
t0 = time.time()
with open(json_file_name, 'r') as infile:
    allMessages = json.load(infile)

t1 = time.time()
print 'Reading data from JSON took:', (t1 - t0), 's'

# for people, message_thread in allMessages.iteritems():
#     print people, len(allMessages[people])

# Computing histogram
people = 'Islam Kadri, Louis Lu'

t0 = time.time()
hist, bin_edges = np.histogram([parse(message['time']).hour for message in allMessages[people]], bins=range(25))
t1 = time.time()
print 'Computing histogram took:', (t1 - t0), 's'

# Plot the histogram
plt.bar(range(24), hist, color='r')
plt.title('Number of messages vs. hour between ' + people)
plt.xlabel('Hour')
plt.ylabel('Number of messages')
plt.show()
