from django.db import models

class Tweets(models.Model):
    user_id = models.IntegerField()
    tweet_body = models.CharField(max_length=140)
    retweet_count = models.IntegerField()
    likes_count = models.IntegerField()
    replies_count = models.IntegerField()
    is_deleted = models.IntegerField()
    published_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.user_id) + ': ' + self.tweet_body


class Followers_Data(models.Model):
    followed_user_id = models.IntegerField()
    follower_user_id = models.IntegerField()
    created_datetime = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return str(self.follower_user_id) + ' follows ' + str(self.followed_user_id)