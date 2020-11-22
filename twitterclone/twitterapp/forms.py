from django import forms


class TweetForm(forms.Form):
    tweet_body = forms.CharField(label='Tweet', max_length=140)