from .forms import PostForm
from django.utils import timezone
from .models import Post
from urllib import request
from django.shortcuts import redirect
from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator , EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.models import SocialAccount
from open_facebook import OpenFacebook
from django.http import HttpResponse
import ssl
import requests
from .forms import PostForm
from .forms import RemotePostForm
import json




ssl._create_default_https_context = ssl._create_unverified_context


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = SocialAccount.objects.get(user=request.user)
            access_token = SocialToken.objects.get(account_id=user, account__provider='facebook')
            idUser = user.uid
            graph = OpenFacebook(access_token=access_token)

            if graph.is_authenticated():

                idPages = (graph.get('me/accounts/'))
                id_Pages_List = [id['id'] for id in idPages['data']]
                id_Pages_List = ", ".join(id_Pages_List)


                id_Page_Access_Token = (graph.get(id_Pages_List, fields='access_token'))
                id_Page_Access_Token = (id_Page_Access_Token['access_token'])


                graph = OpenFacebook(access_token=id_Page_Access_Token)

                feed_url = 'https://graph.facebook.com/'+id_Pages_List+'/feed?message='+post.text+'&access_token='+id_Page_Access_Token
                feed_Request = requests.post(feed_url)

                print(feed_Request.status_code)

                if(feed_Request.status_code == 200):
                    return render(request, 'blog/home.html', {'user': request.user,'access_token': id_Page_Access_Token,'page_id': id_Pages_List })
                else:
                    return HttpResponse(feed_Request)
                    print('bad')
                return render(request, 'blog/loginFacebook.html', {'access_token': access_token, 'idUser': idUser})
            else:
               print('bad')
            return render(request, 'blog/loginFacebook.html')


    else:
        form = PostForm()
    return render(request, 'blog/add_new_post.html', {'form': form})

def remote_post_new(request):
    if request.method == "POST":
        form = RemotePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            user = SocialAccount.objects.get(user=request.user)
            access_token = SocialToken.objects.get(account_id=user, account__provider='facebook')
            idUser = user.uid
            graph = OpenFacebook(access_token=access_token)

            if graph.is_authenticated():

                idPages = (graph.get('me/accounts/'))
                id_Pages_List = [id['id'] for id in idPages['data']]
                id_Pages_List = ", ".join(id_Pages_List)


                id_Page_Access_Token = (graph.get(id_Pages_List, fields='access_token'))
                id_Page_Access_Token = (id_Page_Access_Token['access_token'])


                graph = OpenFacebook(access_token=id_Page_Access_Token)

                feed_url = 'https://graph.facebook.com/'+id_Pages_List+'/feed?&published=false&message='+post.text+'&access_token='+id_Page_Access_Token+'&scheduled_publish_time='+str(post.time.timestamp())
                feed_Request = requests.post(feed_url)

                if(feed_Request.status_code == 200):
                    return render(request, 'blog/home.html', {'user': request.user,'access_token': id_Page_Access_Token,'page_id': id_Pages_List })
                else:
                    return HttpResponse(feed_Request)
                return render(request, 'blog/loginFacebook.html', {'access_token': access_token, 'idUser': idUser})
            else:
                return render(request, 'blog/loginFacebook.html')

    else:
        form = RemotePostForm()
        return render(request, 'blog/add_new_remote_post.html', {'form': form})




def post_list(request):
    posts_list = Post.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(posts_list, 2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new_bd(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish(author=request.user)

            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'blog/post_add.html', {'form': form})



def get_price_btc(request):
    getPriceUrl = 'https://api-pub.bitfinex.com/v2/tickers?symbols=tBTCUSD'
    getPrice = requests.get(getPriceUrl)
    json_string = json.loads(getPrice.text)
    print(json_string)
    return render(request, 'blog/home.html',{'json_string': json_string})






