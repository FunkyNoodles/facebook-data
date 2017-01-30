from dateutil.parser import *
import json
import time

json_file_name = 'D://Facebook/2016-01-28/json/messages.json'

allMessages = {}
t0 = time.time()
with open(json_file_name, 'r') as infile:
    allMessages = json.load(infile)

t1 = time.time()
print 'Reading data from JSON took:', (t1 - t0), 's'

for people, message_thread in allMessages.iteritems():
    print people, len(allMessages[people])

