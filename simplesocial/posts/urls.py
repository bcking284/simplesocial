from django.conf.urls import url

from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$',views.PostList.as_view(),name='all'),
    url(r'^new/$',views.CreatePost.as_view(),name='create'),
    #click on a user and can see their posts
    url(r'^by/(?P<username>[-\w]+)',views.UserPosts.as_view(),name='for_user'),
    #post DetailView
    url(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    #last one for if you want to delete something
    url(r'^delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name='delete'),
]
