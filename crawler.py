import tweepy
import unittest
import sys

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
config = {}
# execfile("twitter.conf", config)
config_filename = "twitter.conf"
with open(config_filename, "rb") as fp:
    code = compile(fp.read(), config_filename, "exec")
exec(code, config)


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
        except KeyError:
            pass
        try:
            status = resources['statuses'][method_name]
            return status['remaining']
        except KeyError:
            pass
        try:
            application = resources['application'][method_name]
            return application['remaining']
        except KeyError:
            pass

        return None

#User Object
#get user object
def get_user(twitter_handle):
    #attributes = [attr for attr in dir(user) if not callable(getattr(user, method))]
    #print attributes
    user = api.get_user(twitter_handle)
    #methods = [method for method in dir(user) if callable(getattr(user, method))]
    return user

#get twitter account creation time
def get_user_created_at(user):
    return user.created_at.strftime('%a %Y-%m-%d %H:%M:%S')

#default profile
def is_user_default_profile(user):
    if not user.default_profile:
        return False
    return True

#default profile img
def is_user_default_profile_img(user):
    if not user.default_profile_image:
        return False
    return True

#get description
def get_user_description(user):
    return user.description

#get fav count
def get_user_fav_cnt(user):
    return user.favourites_count

#get followers list
def get_user_followers(user):
    return user.followers()

#get friends
def get_user_friends(user):
    return user.friends()

#get follower ids
def get_user_follower_ids(user):
    return user.followers_ids()

#get no of followers
def get_user_followers_count(user):
    return user.followers_count

def get_user_friends_count(user):
    return user.friends_count

#get name
def get_user_name(user):
    return user.name

#get location
def get_user_location(user):
    return user.location

#get screen name
def get_user_screen_name(user):
    return user.screen_name

#get utc offset
def get_user_utc_offset(user):
    return user.utc_offset

#get time zone
def get_user_time_zone(user):
    return user.time_zone

#get geo enabled
def get_user_geo_enabled(user):
    return user.geo_enabled

#get user id
def get_user_id_string(user):
    return user.id_str

#get user language
def get_user_language(user):
    return user.lang

#get user protected
def get_user_protected(user):
    return user.protected

#get user statuses or tweets count
def get_user_statuses_count(user):
    return user.statuses_count

#get user url
def get_user_url(user):
    return user.url

#is user verified
def is_user_verified(user):
    return user.verified
    
#get profile bg img url
def get_user_prof_bg_img_url(user):
    return user.profile_background_image_url

#get profile banner url (this attribute might not appear on some accounts, 
#and an exception will be thrown)
def get_user_prof_banner_url(user):
    return user.profile_banner_url

#is user using prof bg img
def is_user_prof_bg_img(user):
    return user.profile_use_background_image

#Tweet Object
#get timeline: user tweets
# By default exclude retweets: https://stackoverflow.com/questions/50052330/tweepy-check-if-a-tweet-is-a-retweet#:~:text=Whilst%20you%20can%20exclude%20retweets,tweet%20begins%20with%20the%20rt.
def get_timeline(twitter_handle, numOfTweet, includeRTs=False):
    statuses = api.user_timeline(screen_name = twitter_handle, count = numOfTweet, include_rts = includeRTs)
    return statuses

#get author, which is an object of user
def get_status_author(status):
    return status.author.screen_name

#get author id string
def get_status_author_id_string(status):
    return status.author.id_str

#get tweet created timestamp
def get_status_created_at(status):
    return status.created_at.strftime('%a %Y-%m-%d %H:%M:%S')

#get tweet favourite count
def get_status_favorite_count(status):
    return status.favorite_count

#get tweet coordinates
def get_status_coordinates(status):
    return status.coordinates

#get tweet id
def get_status_id_string(status):
    return status.id_str

#get tweet language
def get_status_language(status):
    return status.lang

#get retweet count
def get_status_retweet_count(status):
    return status.retweet_count

#get tweet source
def get_status_source(status):
    return status.source

#get tweet source url
def get_status_source_url(status):
    return status.source_url

#get tweet text
def get_status_text(status):
    return status.text

#get geo info
def get_status_geo(status):
    return status.geo


#check if there is a unidirectional or bi-directional link betweet two twitter users
def check_link(src_name, tgt_name):
    source, target = api.show_friendship(source_screen_name = src_name, target_screen_name = tgt_name)
    if source.followed_by:
        print("{} followed by {}".format(source.screen_name, target.screen_name))
    if source.following:
        print("{} following {}".format(source.screen_name, target.screen_name))
    if target.followed_by:
        print("{} followed by {}".format(target.screen_name, source.screen_name))
    if target.following:
        print("{} following {}".format(target.screen_name, source.screen_name))

    
#get user profile
def get_user_profile(twitter_handle):
    user = get_user(twitter_handle)
    profile = {}
    profile["created_at"] = str(get_user_created_at(user))
    profile["followers_count"] = get_user_followers_count(user)
    profile["followees_count"] = get_user_friends_count(user)
    if is_user_default_profile(user):
        profile["default_profile"] = True
    else:
        profile["default_profile"] = False
    if is_user_default_profile_img(user):
        profile["default_profile_img"] = True
    else:
        profile["default_profile_img"] = False
    profile["description"] = get_user_description(user).encode('utf-8')
    profile["name"] = get_user_name(user).encode('utf-8')
    profile["location"] = get_user_location(user).encode('utf-8')
    profile["screen_name"] = get_user_screen_name(user).encode('utf-8')
    profile["fave_count"] = get_user_fav_cnt(user)
    profile["time_zone"] = get_user_time_zone(user)
    profile["utc_offset"] = str(get_user_utc_offset(user))
    profile["user_id"] = get_user_id_string(user)
    profile["acc_protected"] = get_user_protected(user)
    profile["status_count"] = get_user_statuses_count(user)
    return profile

#print user profile
def print_user_profile(profile):
    print("twitter handle={}".format(profile["screen_name"]))
    print("account created at={}".format(profile["created_at"]))
    print("followers count={}".format(profile["followers_count"]))
    print("followees count={}".format(profile["followees_count"]))
    print("default profile={}".format(profile["default_profile"]))
    print("default profile img={}".format(profile["default_profile_img"]))
    print("description={}".format(profile["description"]))
    print("name={}".format(profile["name"]))
    print("location={}".format(profile["location"]))
    print("screen name={}".format(profile["screen_name"]))
    print("fav count={}".format(profile["fave_count"]))
    print("time zone={}".format(profile["time_zone"]))
    print("UTC offset={}".format(profile["utc_offset"]))
    print("user id={}".format(profile["user_id"]))
    print("acc is protected={}".format(profile["acc_protected"]))
    print("status count={}".format(profile["status_count"]))


#get user tweets
def get_user_tweets(twitter_handle, tw_cnt):
    tweets = []
    statuses = get_timeline(twitter_handle, tw_cnt)
    for status in statuses:
        # print("status:{}".format(status))
        tweet = {}
        tweet["source"] = get_status_source(status)
        tweet["text"] = get_status_text(status)
        tweet["created_at"] = str(get_status_created_at(status))
        tweet["author"] = get_status_author(status)
        tweet["coordinate"] = get_status_coordinates(status)
        tweet["geo"] = get_status_geo(status)
        tweet["lang"] = get_status_language(status)
        tweet["fav_cnt"] = get_status_favorite_count(status)
        tweet["rt_cnt"] = get_status_retweet_count(status)
        tweets.append(tweet)
    return tweets

#store tweets info in a csv file
def write_user_tweets(tweets):
    with open("data/tweets.csv", "w") as fp:
        fp.write("author;@;created_at;@;text;@;source;@;coord;@;geo;@;lang;@;fav_cnt;@;rt_cnt\n")
        for tweet in tweets:
            out = "%s;@;%s;@;%s;@;%s;@;%s;@;%s;@;%s;@;%d;@;%d\n" % (tweet["author"].encode('utf-8'), tweet["created_at"], tweet["text"].encode('utf-8'), tweet["source"].encode('utf-8'), tweet["coordinate"], tweet["geo"], tweet["lang"].encode('utf-8'), tweet["fav_cnt"], tweet["rt_cnt"])
            fp.write(out)

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: {}".format(sys.argv[0]))
        sys.exit(1)
    #let's get my handle profile and tweets data using tw api
    # tw_handle = "kjahanbakhsh"
    tw_handle = "sama"
    #profile = get_user_profile(tw_handle)
    #print_user_profile(profile)
    tw_cnt = 500
    tweets = get_user_tweets(tw_handle, tw_cnt)
    write_user_tweets(tweets)
