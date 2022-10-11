from django.urls import path, include
from . import views
from portfolio.views import home

app_name = 'blog'

urlpatterns = [

    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('home/', home),

]

