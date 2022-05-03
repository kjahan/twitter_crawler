Twitter Crawler
===============
<p>This is a python script to crawl account properties and tweets for a given twitter handle.</p>

## Dependencies

Twitter crawler uses <a href="https://github.com/tweepy/tweepy">tweepy</a> and wget libraries. 

	pip2 install -r requirements.txt

## How to run Twitter crawler

First, create a Twitter app on the <a href="https://developer.twitter.com/">developer portal</a>, create a file "twitter.conf" in the repository directory and copy the required information in it. See below for the format of "twitter.conf" file:

	api_key = "your_api_key"
	api_secret_key = "your_api_secret_key"
	access_token = "your_access_token"
	access_token_secret = "your_access_token_secret"

The API keys can be found when creating an App in the <a href="https://developer.twitter.com/en/portal/projects-and-apps">Twitter developer portal</a>.

Next, you can run Twitter crawler as follows:

	python crawler.py target_twitter_handle download_full_path

Kudos to <a href="https://github.com/kjahan">kjahan</a> for the inspiration. 

## Licence

    Copyright (c) 2013 Black Square Media Ltd. All rights reserved.
    (The MIT License)

    Permission is hereby granted, free of charge, to any person obtaining
    a copy of this software and associated documentation files (the
    'Software'), to deal in the Software without restriction, including
    without limitation the rights to use, copy, modify, merge, publish,
    distribute, sublicense, and/or sell copies of the Software, and to
    permit persons to whom the Software is furnished to do so, subject to
    the following conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
