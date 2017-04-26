__author__ = 'Randev Senaratne'

from TwitterAPI import TwitterAPI
import time


SEARCH_TERMS = ['#pythondev', '#python', '#twitterbot', '#developer', '#dev', '#tiqri' ,'#exilesoft', '#javadev', '#NoSQL', '#SQL', '#PHP', '#javascript', '#git', '#jquery', '#NodeJS', '#agile', '#CSS', '#html', '#AndroidStudio', '#jetbrains', '#nexus', '#ios', '#AndroidDev', '#iot', '#AndroidIOT', '#Tiqricorp', '#microsoft', '#ubuntu', '#c++', '#stackoverflow', '#syntaxerror', '#angularjs', '#reactjs', '#webdevelopment', '#webdeveloper' '#webdesign', '#webdesigner', '#html5', '#bootstrap', '#application', '#app', '#development', '#css', '#css3', '#js', '#jquery', '#nodejs', '#laravel', '#mongodb', '#postgresql', '#robotic']
CONSUMER_KEY = '<your consumer key>'
CONSUMER_SECRET = 'your consumer secret'
ACCESS_TOKEN_KEY = 'your access token key'
ACCESS_TOKEN_SECRET = 'access token secret'

already_tweeted = []

api = TwitterAPI(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET)

re_tweet_count = 1
search_count = 0
while True:
    try:
        print('Searching for ' + SEARCH_TERMS[search_count])
        result = api.request('search/tweets', {'q': SEARCH_TERMS[search_count]})
        for item in result:
            if (item['id'] not in already_tweeted):
                try:
                    print(item['text'] if 'text' in item else item)
                    api.request('statuses/retweet/:%d' % item['id'])
                    already_tweeted.append(item['id'])
                    print('SUCCESS' if result.status_code == 200 else 'FAILURE')
                    break
                except Exception as err:
                    print('There was an error searching for tweets')
                    print(err)
                    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
                    time.sleep(10)

    except Exception as err:
        print('There was an error searching for tweets')
        print(err)
        api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
        time.sleep(10)
                
                
    search_count += 1
    if search_count == len(SEARCH_TERMS):
        search_count = 0
    print('Tweet iteration: ' + str(search_count))
    print('QUOTA: %s' % result.get_rest_quota())
    print('TWEET COUNT: ' + str(re_tweet_count))
    re_tweet_count += 1
    print('\n\n')

    time.sleep(30)
