from django.urls import path
from authentication import views

app_name = 'authenticate'

urlpatterns = [
    # path('login/', login),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
]
