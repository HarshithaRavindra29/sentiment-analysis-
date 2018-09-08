ckey=
csecret=
atoken=
asecret=
'''save twitter data into a file and filter using search term '''
#!/usr/bin/python
import tweepy
import csv #Import csv
auth = tweepy.auth.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('result1.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,
                           q = "SEARCH TERM",
                           lang = "en").items():

    # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text
csvFile.close()
import pandas as pd
df= pd.read_csv('result.csv', names = ['Date', 'text'])
pd.to_datetime(df['Date'])
df.head()
df.shape
