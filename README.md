# Twitter-Sentiment-Analysis
Sentiment Analysis of tweets using Twitter API and RoBERTa model

![cover](https://user-images.githubusercontent.com/15322711/213688023-eb1ab3c5-c237-4abe-b1bb-a1bb52d5ab11.jpg)

The Twitter API is a set of programming interfaces that allows developers to access the functionality of the Twitter platform. It enables developers to integrate Twitter functionality into their own applications, such as posting tweets, retrieving tweets, and searching for tweets. The API also provides access to other features of Twitter, such as user profiles, lists, and direct messages. The API is available in several languages and can be accessed using RESTful or streaming methods. With the use of appropriate access credentials, developers can make requests to the API and receive data in various formats including JSON and XML.

One popular use of the Twitter API is for sentiment analysis, which involves analyzing tweets to determine the sentiment or attitude expressed in them. This can be used for various purposes such as brand monitoring, customer service, and market research. Developers can use the Twitter API to retrieve a large number of tweets containing specific keywords or hashtags, and then use natural language processing techniques to analyze the sentiment of the tweets. Sentiment analysis can be performed on various levels such as the overall sentiment of a tweet, the sentiment of specific entities or topics mentioned in the tweet, and the sentiment of specific phrases or words.

In this project, we use the Twitter API to retrieve tweets and a pre-trained RoBERTa model to perform sentiment analysis. RoBERTa is a variant of BERT (Bidirectional Encoder Representations from Transformers) which is a transformer-based model trained on a large corpus of text data. It is considered to be one of the state-of-the-art models for natural language processing tasks such as sentiment analysis. By fine-tuning RoBERTa on the twitter data retrieved by the API, we can achieve more accurate and reliable results compared to traditional methods. There are several libraries and frameworks like Hugging Face's transformers and PyTorch that makes it easy to fine-tune RoBERTa on twitter data and access the Twitter API. To learn more about RoBERTa and fine-tuning, you can refer to the following links:

https://huggingface.co/transformers/

https://pytorch.org/tutorials/intermediate/roberta_classification_tutorial.html

https://arxiv.org/abs/1907.11692
