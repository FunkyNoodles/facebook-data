from dateutil.parser import *
import json
import time
import numpy as np
import operator
import re
import matplotlib.pyplot as plt


def histogram_of_message_count_by_hour(all_messages, conversation_people):
    hist, bin_edges = np.histogram([parse(message['time']).hour for message in all_messages[conversation_people]], bins=range(25))
    histogram_fig = plt.figure()
    plt.bar(range(24), hist, color='r')
    plt.title('Number of messages vs. hour between ' + conversation_people)
    plt.xlabel('Hour')
    plt.ylabel('Number of messages')
    return histogram_fig


def rank_most_common_words(all_messages, conversation_people):
    words = {}
    for message in all_messages[conversation_people]:
        message_data = message['data']
        word_list = re.sub("[^\w]", " ", message_data).split()
        for word in word_list:
            if words.get(word) is None:
                words[word] = 1
            else:
                words[word] += 1

    sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_words


json_file_name = 'D://Facebook/2016-01-28/json/messages.json'


t0 = time.time()
with open(json_file_name, 'r') as infile:
    allMessages = json.load(infile)

t1 = time.time()
print 'Reading data from JSON took:', (t1 - t0), 's'


people_name = 'Islam Kadri, Louis Lu'


# Plot the histogram
t0 = time.time()
histogram = histogram_of_message_count_by_hour(allMessages, people_name)
t1 = time.time()
print 'Computing histogram took:', (t1 - t0), 's'

# Rank words
t0 = time.time()
ranked_words = rank_most_common_words(allMessages, people_name)
t1 = time.time()
print 'Ranking most common words took:', (t1 - t0), 's'

common_words_output_file = open('common words.csv', 'w+')
for w, c in ranked_words:
    common_words_output_file.write(w + ', ' + str(c) + '\n')

plt.show()
