import tweepy
import unittest
import sys
import os
import wget

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
config = {}
execfile("twitter.conf", config)

api_key = config["api_key"]
api_secret_key = config["api_secret_key"]

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located under "Your access token")
access_token = config["access_token"]
access_token_secret = config["access_token_secret"]

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#get all methods for tweepy api
def get_methods():
    methods = [method for method in dir(tweepy.api) if callable(getattr(tweepy.api, method))]
    return methods

#Rate Limit Object

#get API limit
def get_api_limit():
    return api.rate_limit_status()

#get method limit
def get_api_method_limit(api_limit, method_name):
        resources = api_limit['resources']
        try:
            user = resources['users'][method_name]
            return user['remaining']
        except KeyError, e:
            pass
        try:
            status = resources['statuses'][method_name]
            return status['remaining']
        except KeyError, e:
            pass
        try:
            application = resources['application'][method_name]
            return application['remaining']
        except KeyError, e:
            pass

        return None

#store tweets info in a csv file
def download_and_save_tweets(tw_handle, download_path):
    with open(download_path + "/" + tw_handle + "/tweets.csv", "w") as fp:

        fp.write("\"user.created_at\";\"user.name\";\"user.screen_name\";\"user.id_str\";\"user.followers_count\";\"user.friends_count\";\"user.statuses_count\";\"user.description\";\"user.default_profile_image\";\"user.verified\";\"user.listed_count\";\"user.location\";\"user.favourites_count\";\"user.url\";\"user.protected\";\"user.default_profile\";\"user.profile_banner_url\";")
        fp.write("\"truncated\";\"text\";\"is_quote_status\";\"quote_count\";\"favorite_count\";\"source\";\"retweeted\";\"in_reply_to_screen_name\";\"retweet_count\";\"id_str\";\"favorited\";\"in_reply_to_user_id_str\";\"lang\";\"created_at\";\"in_reply_to_status_id_str\";\"quoted_status_id_str\";\"reply_count\";\"retweet_count\";\"favorite_count\";")
        fp.write("\"place.id\";\"place.url\";\"place.place_type\";\"place.name\";\"place.full_name\";\"place.country_code\";\"place.country\";")
        fp.write("\"geo.lon\";\"geo.lat\";")
        fp.write("\"media[0].expanded_url\";\"media[0].display_url\";\"media[0].url\";\"media[0].media_url_https\";\"media[0].id_str\";\"media[0].type\";\"media[0].media_url\";\"media[1].expanded_url\";\"media[1].display_url\";\"media[1].url\";\"media[1].media_url_https\";\"media[1].id_str\";\"media[1].type\";\"media[1].media_url\";\"media[2].expanded_url\";\"media[2].display_url\";\"media[2].url\";\"media[2].media_url_https\";\"media[2].id_str\";\"media[2].type\";\"media[2].media_url\";\"media[3].expanded_url\";\"media[3].display_url\";\"media[3].url\";\"media[3].media_url_https\";\"media[3].id_str\";\"media[3].type\";\"media[3].media_url\";")
        fp.write("\"retweet_id\";\"quote_id\"\n")

        for tweet in tweepy.Cursor(api.user_timeline,id=tw_handle).items():
            json_tweet = tweet._json
            while json_tweet: 
                # User information
                description = "" if json_tweet.get("user").get("description", "") is None else json_tweet.get("user").get("description", "").encode('utf-8') 
                out = "\"" + json_tweet.get("user").get("created_at", "").encode('utf-8') + "\";\"" + json_tweet.get("user").get("name", "").encode('utf-8') + "\";\"" + json_tweet.get("user").get("screen_name", "").encode('utf-8') + "\";\"" + json_tweet.get("user").get("id_str", "").encode('utf-8') + "\";\"" + str(json_tweet.get("user").get("followers_count", "")) + "\";\"" + str(json_tweet.get("user").get("friends_count", "")) + "\";\"" + str(json_tweet.get("user").get("statuses_count", "")) + "\";\"" + description + "\";\"" + str(json_tweet.get("user").get("default_profile_image", "")) + "\";\"" + str(json_tweet.get("user").get("verified", "")) + "\";\"" + str(json_tweet.get("user").get("listed_count", "")) + "\";\"" + str(json_tweet.get("user").get("location", "")) + "\";\"" + str(json_tweet.get("user").get("favourites_count", "")) + "\";\"" + str(json_tweet.get("user").get("url", "")) + "\";\"" + str(json_tweet.get("user").get("protected", "")) + "\";\"" + str(json_tweet.get("user").get("default_profile", "")) + "\";\"" + json_tweet.get("user").get("profile_banner_url", "").encode('utf-8') + "\""

                # Tweet details
                out = out + ";\"" + str(json_tweet.get("truncated", "")) + "\";\"" + json_tweet.get("text","").encode('utf-8') + "\";\"" + str(json_tweet.get("is_quote_status","")) + "\";\"" + str(json_tweet.get("quote_count","")) + "\";\"" + str(json_tweet.get("favorite_count","")) + "\";\"" + json_tweet.get("source","").encode('utf-8') + "\";\"" + str(json_tweet.get("retweeted","")) + "\";\"" + str(json_tweet.get("in_reply_to_screen_name","")) + "\";\"" + str(json_tweet.get("retweet_count","")) + "\";\"" + json_tweet.get("id_str","").encode('utf-8') + "\";\"" + str(json_tweet.get("favorited","")) + "\";\"" + str(json_tweet.get("in_reply_to_user_id_str","")) + "\";\"" + str(json_tweet.get("lang","")) + "\";\"" + json_tweet.get("created_at","").encode('utf-8') + "\";\"" + str(json_tweet.get("in_reply_to_status_id_str","")) + "\";\"" + str(json_tweet.get("quoted_status_id_str","")) + "\";\"" + str(json_tweet.get("reply_count","")) + "\";\"" + str(json_tweet.get("retweet_count","")) + "\";\"" + str(json_tweet.get("favorite_count","")) + "\""

                # Place details
                if json_tweet.get("place") is not None:
                    out = out + ";\"" + json_tweet.get("place").get("id", "").encode('utf-8') + "\";\"" + json_tweet.get("place").get("url", "").encode('utf-8') + "\";\"" + json_tweet.get("place").get("place_type", "").encode('utf-8') + "\";\"" + json_tweet.get("place").get("name", "").encode('utf-8') + "\";\"" + json_tweet.get("place").get("full_name", "").encode('utf-8') + "\";\"" + json_tweet.get("place").get("country_code", "").encode('utf-8') + "\";\"" + json_tweet.get("place").get("country", "").encode('utf-8') + "\"" 
                else:
                    out = out + ";\"\";\"\";\"\";\"\";\"\";\"\";\"\""

                # Geo details
                if json_tweet.get("coordinates") is not None:
                    out = out + ";\"" + str(json_tweet.get("coordinates", {}).get("coordinates", [0, 0])[0]) + "\";\"" + str(json_tweet.get("coordinates", {}).get("coordinates", [0, 0])[1]) + "\""
                else:
                    out = out + ";\"\";\"\""

                # Media attached
                media_cnt = 0 
                try:
                    for media in json_tweet["extended_entities"]["media"]:
                        out = out + ";\"" + media.get("expanded_url", "").encode('utf-8') + "\";\"" + media.get("display_url", "").encode('utf-8') + "\";\"" + media.get("url", "").encode('utf-8') + "\";\"" + media.get("media_url_https", "").encode('utf-8') + "\";\"" + media.get("id_str", "").encode('utf-8') + "\";\"" + media.get("type", "").encode('utf-8') + "\";\"" + media.get("media_url", "").encode('utf-8') + "\""
                        download_media(media.get("media_url_https"), json_tweet["id_str"], media_cnt, download_path, tw_handle)
                        media_cnt += 1
                except KeyError:
                    pass
                while media_cnt < 4:
                    out = out + ";\"\";\"\";\"\";\"\";\"\";\"\";\"\""
                    media_cnt += 1

                # The current tweet may be a retweet or contain another tweet nested in it, and it will be saved. 
                try:
                    json_tweet = json_tweet["retweeted_status"]
                    out = out + ";\"" + str(json_tweet["id_str"]) + "\""
                except KeyError:
                    json_tweet = None
                    out = out + ";\"\"" 

                # ... or may be a quote for a tweet:
                try:
                    json_tweet = json_tweet["quoted_status"]
                    out = out + ";\"\"" + str(json_tweet["id_str"]) + "\""
                except KeyError:
                    json_tweet = None
                    out = out + ";\"\""
                except TypeError:
                    # This happened because the parent tweet contained a retweet
                    pass

                # Getting rid of all newlines
                out = out.replace("\n", "")
                fp.write(out+"\n")

def download_media(url, tweet_id, media_cnt, download_path, tw_handle):
    extension = url.split('.')[-1]
    filename = download_path + "/" + tw_handle + "/media/" + tweet_id + "-media-" + str(media_cnt) + "." + extension
    wget.download(url, filename)

def check_path_and_create(tw_handle, download_path):
    filename = download_path + "/" + tw_handle + "/"
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    filename = filename + "media/"
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print 'Usage: ' + sys.argv[0] + ' twitter_user_handle download_path'
        sys.exit(1)
    tw_handle = sys.argv[1]
    download_path = sys.argv[2]
    check_path_and_create(tw_handle, download_path)
    download_and_save_tweets(tw_handle, download_path)
