from django.urls import path

from forums import views

app_name = 'forums'

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/search/', views.category_search, name='category_search'),
    path('create/category/', views.category_create, name='category_create'),
    path('edit/category/<slug:slug>/', views.category_edit, name='category_edit'),
    path('category/<slug:category_slug>/topics/', views.topic_list, name='topic_list'),
    path('category/<slug:category_slug>/topics/search/', views.topic_search, name='topic_search'),
    path('category/<slug:category_slug>/create/topics/', views.topic_create, name='topic_create'),
    path('category/<slug:category_slug>/edit/topics/<slug:slug>/', views.topic_edit, name='topic_edit'),
    path('category/<slug:category_slug>/detail/topics/<slug:slug>/', views.topic_detail, name='topic_detail'),
    path('category/<slug:category_slug>/detail/topics/<slug:slug>/congrats/',
         views.discuss_send_congratulation, name='discuss_send_congratulation'),
]