from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import TweetForm
from .models import Tweets,Followers_Data
from django.http import HttpResponse
from django.contrib.auth.models import User
import json


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
        
    return render(request, 'signup.html', {'form': form})


def post_tweet(request):
    if request.user.id:
        if request.method == 'POST':
            form = TweetForm(request.POST)
            if form.is_valid():
                user_id = request.user.id
                tweet_body = request.POST['tweet_body']
                obj = Tweets(user_id=user_id,tweet_body=tweet_body,retweet_count=0,
                                likes_count=0,replies_count=0,is_deleted=0)
                obj.save()
                return redirect('/thanks/')
        else:
            form = TweetForm()
        return render(request, 'tweet_form.html', {'form': form})
    else:
        return render(request, 'logged_out.html')


def render_thanks_page(request):
    return render(request, 'thanks.html')


def dashboard_tweets(request):
    if request.user.id:
        user_id = request.user.id
        followed_users = Followers_Data.objects.filter(follower_user_id=user_id)
        if len(followed_users) > 0:
            obj = []
            followed_user_ids = [f.followed_user_id for f in followed_users]
            tweets_data = Tweets.objects.filter(user_id__in=followed_user_ids).filter(is_deleted=0).order_by('-published_datetime')
            for data in tweets_data:
                print(data.user_id,data.published_datetime)
                current_tweet = {}
                current_tweet['user_id'] = data.user_id
                current_tweet['username'] = User.objects.filter(id=user_id)[0].username
                current_tweet['tweet_body'] = data.tweet_body
                current_tweet['retweet_count'] = data.retweet_count
                current_tweet['likes_count'] = data.likes_count
                current_tweet['replies_count'] = data.replies_count
                obj.append(current_tweet)
        else:
            obj = {}
        data = json.dumps(obj)
    else:
        data = json.dumps({'error':'please login in order to access this endpoint'})

    return HttpResponse(data, content_type='application/json')


def dashboard(request):
    return render(request, 'dashboard.html')