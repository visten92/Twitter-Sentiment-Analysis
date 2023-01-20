from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import tweepy

API_KEY = 'YOUR_API_KEY'
API_SECRET_KEY = 'YOUR_SECRET_KEY'

auth = tweepy.OAuth1UserHandler(
  API_KEY ,
  API_SECRET_KEY
)

date = '2023-01-17'
api = tweepy.API(auth)
tweets = api.search_tweets("Stock market", tweet_mode="extended", until=date)


tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")

score_coef = [-1,0,1]
labels = ['Negative', 'Neutral', 'Positive']
total_score = 0
for tweet in tweets:
    try:
        inputs = tokenizer(tweet.retweeted_status.full_text, return_tensors="pt")
        classification = model(**inputs)
        scores = classification[0][0].detach().numpy()
        scores = softmax(scores)
        print("Tweet: ", tweet.retweeted_status.full_text)
        for i in range(len(scores)):
            l = labels[i]
            s = scores[i]
            print(l, s)
            total_score = score_coef[i] * scores[i]
        print("==============================================================================================================================")
    except AttributeError:
        print(tweet.full_text)
        print("==============================================================================================================================")

print('Total score: ', total_score)




