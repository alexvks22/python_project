"""
Use Twitter API to grab user information from Twitter Profiles

Uses Tweepy module to access Twitter API
"""
import tweepy

#API Codes
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

#authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth) #personal api

name1=raw_input('Enter first profile: ') 
name2=raw_input('Enter second profile: ')

user1 = api.get_user(name1) # get username of first profile
user2 = api.get_user(name2) # get username of second profile

print ('\nProfile:')
print('@' + user1.name)

tweets = user1.statuses_count # calculate tweets of first profile

#examine multiple occasions, could have embody them to different functions differentiated the two users 

if tweets <= 9999:
	print ('TWEETS: ' + str(tweets))

if tweets >= 10000 and tweets <= 99999:
	tweets = str(tweets)
	print ('TWEETS: ' + tweets.replace( '.' , '.' )[:-3] + '.' + tweets[2] + 'K')

if tweets >= 100000 and tweets <= 999999:
	tweets = str (tweets)
	print  ('TWEETS: ' + tweets.replace( '.' , '.' )[:-3] + '.' + tweets[3] + 'K')

if tweets >= 1000000 and tweets <= 9999999:
		tweets = str(tweets)
		print ('TWEETS: ' + tweets.replace( '.' , '.' )[:-6] + '.' + tweets[1:2] +  'M')

if tweets >= 10000000 and tweets <= 99999999:
		tweets = str(tweets)
		print ('TWEETS: ' + tweets.replace( '.' , '.' )[:-6] + '.' + tweets[2:3] + 'M')

if tweets >= 100000000 and tweets <= 999999999:
	tweets = str(tweets)
	print ('TWEETS: ' + tweets.replace( '.' , '.' )[:-6] + '.' + tweets[3:4] + 'M')

if tweets >= 1000000000 and tweets <= 9999999999:
	tweets = str(tweets)
	print  ('TWEETS: ' + tweets.replace( '.' , '.' )[:-9] + '.' + tweets[1:3] + 'B')


following = user1.friends_count # calculate sum of user's 1 following

if following <= 9999:
	print ('FOLLOWING: ' + str(following))

if following >= 10000 and following <= 99999:
	following = str(following)
	print ('FOLLOWING: ' + following.replace( '.' , '.' )[:-3] + '.' + following[2] + 'K')

if following >= 100000 and following <= 999999:
	following = str (following)
	print  ('FOLLOWING: ' + following.replace( '.' , '.' )[:-3] + '.' + following[3] + 'K')

if following >= 1000000 and following <= 9999999:
		following = str(following)
		print ('FOLLOWING: ' + following.replace( '.' , '.' )[:-6] + '.' + following[1:2] +  'M')

if following >= 10000000 and following <= 99999999:
		following = str(following)
		print ('FOLLOWING: ' + following.replace( '.' , '.' )[:-6] + '.' + following[2:3] + 'M')

if following >= 100000000 and following <= 999999999:
	following = str(following)
	print ('FOLLOWING: ' + following.replace( '.' , '.' )[:-6] + '.' + following[3:4] + 'M')

if following >= 1000000000 and following <= 9999999999:
	following = str(following)
	print('FOLLOWING: ' + following.replace( '.' , '.' )[:-9] + '.' + following[1:3] + 'B')

followers = user1.followers_count #calculate followers of first profile

if followers <= 9999:
	print ('FOLLOWERS: ' + str(followers))

if followers >= 10000 and followers <= 99999:
	followers = str(followers)
	print ('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-3] + '.' + followers[2] + 'K')

if followers >= 100000 and followers <= 999999:
	followers = str (followers)
	print  ('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-3] + '.' + followers[3] + 'K')

if followers >= 1000000 and followers <= 9999999:
		followers = str(followers)
		print ('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-6] + '.' + followers[1:2] +  'M')

if followers >= 10000000 and followers <= 99999999:
		followers = str(followers)
		print ('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-6] + '.' + followers[2:3] + 'M')

if followers >= 100000000 and followers <= 999999999:
	followers = str(followers)
	print ('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-6] + '.' + followers[3:4] + 'M')

if followers >= 1000000000 and followers <= 9999999999:
	followers = str(followers)
	print('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-9] + '.' + followers[1:3] + 'B')

likes = user1.favourites_count #calculate likes of user 1, first profile

if likes <= 9999:
	print ('LIKES: ' + str(likes) + '\n')

if likes >= 10000 and likes <= 99999:
	likes = str(likes)
	print ('LIKES: ' + likes.replace( '.' , '.' )[:-3] + '.' + likes[2] + 'K' + '\n')

if likes >= 100000 and likes <= 999999:
	likes = str (likes)
	print  ('LIKES: ' + likes.replace( '.' , '.' )[:-3] + '.' + likes[3] + 'K' + '\n')

if likes >= 1000000 and likes <= 9999999:
		likes = str(likes)
		print ('LIKES: ' + likes.replace( '.' , '.' )[:-6] + '.' + likes[1:2] +  'M' + '\n')

if likes >= 10000000 and likes <= 99999999:
		likes = str(likes)
		print ('LIKES: ' + likes.replace( '.' , '.' )[:-6] + '.' + likes[2:3] + 'M' + '\n')

if likes >= 100000000 and likes <= 999999999:
	likes = str(likes)
	print ('LIKES: ' + likes.replace( '.' , '.' )[:-6] + '.' + likes[3:4] + 'M' + '\n')

if likes >= 1000000000 and likes <= 9999999999:
	likes = str(likes)
	print('LIKES: ' + likes.replace( '.' , '.' )[:-9] + '.' + likes[1:3] + 'B' + '\n')


print ('Profile:')		#doing the same for the second profile
print('@' + user2.name)

tweets=user2.statuses_count

if tweets <= 9999:
	print ('TWEETS: ' + str(tweets))

if tweets >= 10000 and tweets <= 99999:
	tweets = str(tweets)
	print ('TWEETS: ' + tweets.replace( '.' , '.' )[:-3] + '.' + tweets[2] + 'K')

if tweets >= 100000 and tweets <= 999999:
	tweets = str (tweets)
	print  ('TWEETS: ' + tweets.replace( '.' , '.' )[:-3] + '.' + tweets[3] + 'K')

if tweets >= 1000000 and tweets <= 9999999:
		tweets = str(tweets)
		print ('TWEETS: ' + tweets.replace( '.' , '.' )[:-6] + '.' + tweets[1:2] +  'M')

if tweets >= 10000000 and tweets <= 99999999:
		tweets = str(tweets)
		print ('TWEETS: ' + tweets.replace( '.' , '.' )[:-6] + '.' + tweets[2:3] + 'M')

if tweets >= 100000000 and tweets <= 999999999:
	tweets = str(tweets)
	print ('TWEETS: ' + tweets.replace( '.' , '.' )[:-6] + '.' + tweets[3:4] + 'M')

if tweets >= 1000000000 and tweets <= 9999999999:
	tweets = str(tweets)
	print  ('TWEETS: ' + tweets.replace( '.' , '.' )[:-9] + '.' + tweets[1:3] + 'B')

following = user2.friends_count

if following <= 9999:
	print ('FOLLOWING: ' + str(following))

if following >= 10000 and following <= 99999:
	following = str(following)
	print ('FOLLOWING: ' + following.replace( '.' , '.' )[:-3] + '.' + following[2] + 'K')

if following >= 100000 and following <= 999999:
	following = str (following)
	print  ('FOLLOWING: ' + following.replace( '.' , '.' )[:-3] + '.' + following[3] + 'K')

if following >= 1000000 and following <= 9999999:
		following = str(following)
		print ('FOLLOWING: ' + following.replace( '.' , '.' )[:-6] + '.' + following[1:2] +  'M')

if following >= 10000000 and following <= 99999999:
		following = str(following)
		print ('FOLLOWING: ' + following.replace( '.' , '.' )[:-6] + '.' + following[2:3] + 'M')

if following >= 100000000 and following <= 999999999:
	following = str(following)
	print ('FOLLOWING: ' + following.replace( '.' , '.' )[:-6] + '.' + following[3:4] + 'M')

if following >= 1000000000 and following <= 9999999999:
	following = str(following)
	print('FOLLOWING: ' + following.replace( '.' , '.' )[:-9] + '.' + following[1:3] + 'B')


followers = user2.followers_count

if followers <= 9999:
	print ('FOLLOWERS: ' + str(followers))

if followers >= 10000 and followers <= 99999:
	followers = str(followers)
	print ('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-3] + '.' + followers[2] + 'K')

if followers >= 100000 and followers <= 999999:
	followers = str (followers)
	print  ('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-3] + '.' + followers[3] + 'K')

if followers >= 1000000 and followers <= 9999999:
		followers = str(followers)
		print ('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-6] + '.' + followers[1:2] +  'M')

if followers >= 10000000 and followers <= 99999999:
		followers = str(followers)
		print ('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-6] + '.' + followers[2:3] + 'M')

if followers >= 100000000 and followers <= 999999999:
	followers = str(followers)
	print ('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-6] + '.' + followers[3:4] + 'M')

if followers >= 1000000000 and followers <= 9999999999:
	followers = str(followers)
	print('FOLLOWERS: ' + followers.replace( '.' , '.' )[:-9] + '.' + followers[1:3] + 'B')

likes = user2.favourites_count

if likes <= 9999:
	print ('LIKES: ' + str(likes) + '\n')

if likes >= 10000 and likes <= 99999:
	likes = str(likes)
	print ('LIKES: ' + likes.replace( '.' , '.' )[:-3] + '.' + likes[2] + 'K' + '\n')

if likes >= 100000 and likes <= 999999:
	likes = str (likes)
	print  ('LIKES: ' + likes.replace( '.' , '.' )[:-3] + '.' + likes[3] + 'K' + '\n')

if likes >= 1000000 and likes <= 9999999:
		likes = str(likes)
		print ('LIKES: ' + likes.replace( '.' , '.' )[:-6] + '.' + likes[1:2] +  'M' + '\n')

if likes >= 10000000 and likes <= 99999999:
		likes = str(likes)
		print ('LIKES: ' + likes.replace( '.' , '.' )[:-6] + '.' + likes[2:3] + 'M' + '\n')

if likes >= 100000000 and likes <= 999999999:
	likes = str(likes)
	print ('LIKES: ' + likes.replace( '.' , '.' )[:-6] + '.' + likes[3:4] + 'M' + '\n')

if likes >= 1000000000 and likes <= 9999999999:
	likes = str(likes)
	print('LIKES: ' + likes.replace( '.' , '.' )[:-9] + '.' + likes[1:3] + 'B' + '\n')

score1 = 0		#calculate the score between those 2 profiles, according to statics we have collect 
score2 = 0
if user1.statuses_count < user2.statuses_count:
	score2 = score2 + 1
else:
	score1 = score1 + 1

if user1.friends_count < user2.friends_count:
	score2 = score2 + 1
else:
	score1 = score1 + 1

if user1.followers_count < user2.followers_count:
	score2 = score2 + 1
else:
	score1 = score1 + 1

if user1.favourites_count < user2.favourites_count:
	score2 = score2 + 1
else:
	score1 = score1 + 1

print ('Score:' + str(score1) + '-' + str(score2))
