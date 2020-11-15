from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


# POSTS VIEW ENDPOINT
@login_required
def posts(request):
    result = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = result.json()
    posts = []
    for item in data:
        post = {
            'userId': item['userId'],
            'id': item['id'],
            'title': item['title'],
            'body': item['body'],
        }
        posts.append(post)
    return render(request, 'blog-listing.html', {'posts': posts})


# POST DETAILS VIEW ENDPOINT
@login_required
def post_details(request, id):
    result = requests.get(f'https://jsonplaceholder.typicode.com/posts/{id}')
    data = result.json()
    post = {
        'userId': data['userId'],
        'id': data['id'],
        'title': data['title'],
        'body': data['body'],
    }

    res = requests.get(
        f'https://jsonplaceholder.typicode.com/posts/{id}/comments')
    # print(res.text)
    cmnts = res.json()
    comments = []
    for item in cmnts:
        comment = {
            'postId': item['postId'],
            'id': item['id'],
            'name': item['name'],
            'email': item['email'],
            'body': item['body'],
        }
        comments.append(comment)
    return render(request, 'blog-post.html', {'post': post, 'comments': comments})
