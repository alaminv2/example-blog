from django.urls import path
from authentication.views import SignUpView

urlpatterns = [
    # path('login/', login),
    path('register/', SignUpView.as_view(), name='register'),
]
