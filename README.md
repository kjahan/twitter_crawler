Twitter Crawler
===============
<p>This is a python script to crawl account properties and tweets for a given twitter handle.</p>

## Dependencies

Twitter crawler uses <a href="https://github.com/tweepy/tweepy">tweepy library</a>. 

## How to run twitter crawler

First, create a twitter app and copy your app secret key and access token into a file under the same directory "twitter.conf" file. See below for the format of "twitter.conf" file:

	consumer_key = "your_consumer_key"
	consumer_secret = "your_consumer_secret"
	access_token = "your_access_token"
	access_token_secret = "your_access_token_secret"

Next, you can run twitter crawler as follows:

	python crawler.py

<p>
If you have any question about this project or you want to report a bug, please contact me @ kDOTjahanbakhshATgmailDOTcom
</p>

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
