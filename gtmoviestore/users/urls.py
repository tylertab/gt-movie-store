from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', views.signup, name='users.signup'),
    path('login', views.login, name='users.login'),
    path('logout', views.logout, name='users.logout'),
    path('reset_password', views.reset_password, name='users.reset_password'),
    path('reset_password/done', views.reset_password_done, name ='users.reset_password_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # gpt generated
    path('orders/', views.orders, name='users.orders')

]