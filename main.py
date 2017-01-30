import numpy as np
import time
from BeautifulSoup import BeautifulSoup
from dateutil.parser import *
import json


def remove_values_from_list(the_list, val):
    return [value for value in the_list if value != val]


class Message:
    def __init__(self, author, time_sent, data):
        self.author = author
        self.time = time_sent
        self.data = data

    def print_message(self):
        print self.author, ': ', self.data
        return


class MessageThread:
    def __init__(self, people):
        self.messages = []
        self.people = people
        return

    def add(self, m):
        self.messages.append(m)
        return

html_file_name = 'D://Facebook/2016-01-28/html/messages.htm'
json_file_name = 'D://Facebook/2016-01-28/json/messages.json'

t0 = time.time()
docData = BeautifulSoup(open(html_file_name, 'r'))
t1 = time.time()
print 'Reading data took: ', (t1 - t0), 's'

allMessages = {}

t0 = time.time()
for i, mThread in enumerate(docData.findAll("div", attrs={"class": "thread"})):
    mThreadContents = remove_values_from_list(mThread.contents, '\n')
    # Create the MessageThread, if necessary
    people = mThreadContents[0]
    message_thread = []
    for j in range(1, len(mThreadContents), 2):
        message = {}
        # Get message author and time
        messageHeaderContents = remove_values_from_list(mThreadContents[j].contents, '\n')
        messageContents = remove_values_from_list(messageHeaderContents[0].contents, '\n')
        senderContents = remove_values_from_list(messageContents[0].contents, '\n')
        messageAuthor = senderContents[0]
        messageTimeContents = remove_values_from_list(messageContents[1].contents, '\n')
        messageTime = messageTimeContents[0]
        messageTimeParsed = parse(messageTime)
        # Get message data
        if len(mThreadContents[j+1].contents) != 0:
            messageData = mThreadContents[j+1].contents[0]
        else:
            messageData = ''

        message['author'] = messageAuthor
        message['time'] = str(messageTimeParsed)
        message['data'] = messageData

        # Add the message to list
        message_thread.append(message)

    if allMessages.get(people) is None:
        allMessages[people] = message_thread
    else:
        tmp_list = allMessages[people]
        tmp_list += message_thread
        allMessages[people] = tmp_list

t1 = time.time()
print 'Parsing data took: ', (t1 - t0), 's'

t0 = time.time()
with open(json_file_name, 'w') as outfile:
    json.dump(allMessages, outfile, sort_keys=True, indent=4, separators=(',', ': '))

t1 = time.time()
print 'Writing data to JSON took: ', (t1 - t0), 's'
