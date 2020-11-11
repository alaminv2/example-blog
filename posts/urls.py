from django.urls import path
from posts.views import posts, post_details

app_name = 'app_posts'

urlpatterns = [
    path('details/<int:id>/', post_details, name='post_details'),
]
