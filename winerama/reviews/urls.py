from django.conf.urls import url

from . import views

'''
二级boss，就不那么简单清点url了，而是要着手处理与reviews相关的业务了。但问题是，就在urls.py里写真正的业务实现代码么？

答案是“不”， 参考Django的工程学理念MTV模式：选择哪些数据给用户，实际是views来完成。

因此，具体对任务的实现，url总是负责正则匹配而已，即把url对应到相关的实际业务函数。而实际业务函数都在 views.py 里。

小结一下：reviews/url.py 是 reviews业务的大脑， reviews/views.py 是 reviews业务的手脚。

作为开发者，需要关注的是，这两个文件里，变量之间是如何统一从而实现交互的。

'''
urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /wine/
    url(r'^wine$', views.wine_list, name='wine_list'),
    # ex: /wine/5/
    url(r'^wine/(?P<wine_id>[0-9]+)/$', views.wine_detail, name='wine_detail'),
    url(r'^wine/(?P<wine_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    # ex: /review/user - get reviews for the logged user
    url(r'^review/user/(?P<username>\w+)/$', views.user_review_list, name='user_review_list'),
    # ex: /review/user - get reviews for the user passed in the url
    url(r'^review/user/$', views.user_review_list, name='user_review_list'),
    # ex: /recommendation - get wine recommendations for the logged user
    url(r'^recommendation/$', views.user_recommendation_list, name='user_recommendation_list'),
]