import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 
def process_or_store(tweet):
    print(tweet)

class StdOutListener(StreamListener):

	def on_data(self, data):
		print (data)
		return True

	def on_error(self, status):
		print (status)
		
def main() :
	consumer_key = ''
	consumer_secret =''
	access_token = ''
	access_secret = ''
	l = StdOutListener();
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	stream = Stream(auth,l);
	api = tweepy.API(auth);
	stream.filter(track=['python', 'javascript', 'ruby'])
	for friend in tweepy.Cursor(api.friends).items():
		process_or_store(friend._json)
		
if __name__ == '__main__':
  main()