from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

#parse tweets csv file
def parse_csv(file_name):
    tweets =[]
    with open(file_name) as fp:
        hdr = fp.readline()
        tokens = hdr[:-1].split(";@;")
        for line in fp:
            items = line[:-1].split(";@;")
            data = {}
            data["author"] = items[tokens.index("author")]
            data["created_at"] = items[tokens.index("created_at")]
            data["text"] = items[tokens.index("text")]
            data["source"] = items[tokens.index("source")]
            data["coord"] = items[tokens.index("coord")]
            data["geo"] = items[tokens.index("geo")]
            data["lang"] = items[tokens.index("lang")]
            data["fav_cnt"] = items[tokens.index("fav_cnt")]
            data["rt_cnt"] = items[tokens.index("rt_cnt")]
            tweets.append(data)
    return tweets

#plot data
def plot_function(data, filename, label, y_max):
    ind = np.arange(24)
    width = 0.7
    plt.bar(ind, data, width, color='r')
    plt.xlabel('Tweeting hour')
    plt.ylabel('Frequency')
    plt.title(label)
    plt.axis([0, 24, 0, y_max])
    #plt.show()
    plt.savefig('img/' + filename + '.png', bbox_inches='tight')
    plt.close()

#extract and print top maxes
def find_top_max(agg_cnt, key):
    tops = None
    hours = None  #second max & first max in order
    if agg_cnt[0] < agg_cnt[1]:
        hours = [0, 1]
        tops = [agg_cnt[0], agg_cnt[1]]
    else:
        hours = [1, 0]
        tops = [agg_cnt[1], agg_cnt[0]]
    for inx in xrange(2, len(agg_cnt)):
        if (agg_cnt[inx] > tops[0] and agg_cnt[inx] <= tops[1]):
            hours[0] = inx
            tops[0] = agg_cnt[inx]
        elif tops[1] < agg_cnt[inx]:
            hours[0] = hours[1]
            tops[0] = tops[1]
            hours[1] = inx
            tops[1] = agg_cnt[inx]
    #let's find the max
    print "==========================================="
    print key
    #print agg_cnt
    print "top hours =", hours
    print "top values =", tops

#extract frequency of retweets or favourites for posted tweets
def extract_freq(tweets, key):
    posted_times = []
    counts = []
    #Thu 2014-06-12 16:18:23
    FMT = "%a %Y-%m-%d %H:%M:%S"
    for tweet in tweets:
        created_at = datetime.strptime(tweet["created_at"], FMT)
        #get hour and adjust timezone from gmt to pst (pst=gmt-7)
        hour = int((created_at.hour - 7) % 24)
        if not tweet["text"].startswith("RT "):
            posted_times.append(hour)
            cnt = int(tweet[key])
            counts.append(cnt)
    agg_cnt = [0]*24
    for inx in xrange(len(posted_times)):
        hour = posted_times[inx]
        agg_cnt[hour] += counts[inx]
    label = "Distribution of #retweets"
    filename = "retweets"
    if key == "fav_cnt":
        label = "Distribution of #favourites"
        filename = "favourites"
    y_max = max(agg_cnt) + 2
    plot_function(agg_cnt, filename, label, y_max)
    #let's find the top two  max
    find_top_max(agg_cnt, key)

#extract tweeting time pattern
def extract_tw_times(tweets):
    agg_cnt = [0]*24
    #Thu 2014-06-12 16:18:23
    FMT = "%a %Y-%m-%d %H:%M:%S"
    for tweet in tweets:
        created_at = datetime.strptime(tweet["created_at"], FMT)
        #get hour and adjust timezone from gmt to pst (pst=gmt-7)
        hour = int((created_at.hour - 7) % 24)
        if not tweet["text"].startswith("RT "):
            agg_cnt[hour] += 1
    y_max = max(agg_cnt) + 2
    plot_function(agg_cnt, "tweets", "Distribution of tweeting time", y_max)
    #let's find the max
    find_top_max(agg_cnt, "tweeting time")

def main():
    tweets = parse_csv("tweets.csv")
    extract_freq(tweets, "fav_cnt")
    extract_freq(tweets, "rt_cnt")
    extract_tw_times(tweets)

if __name__ == '__main__':
    main()
