from django.urls import path
from .views import Authenticate, LoginView, UserView,FollowerView, UnFollowerView, PostView, UserGet, PostDelete, LikeView, UnLikeView

urlpatterns = [
    path("login",Authenticate.as_view()),
    path("authenticate",LoginView.as_view()),
    path("user",UserView.as_view()),
    path("follow/<int:iid>",FollowerView.as_view()),
    path("unfollow/<int:iid>",UnFollowerView.as_view()),
    path("posts", PostView.as_view()),
    path("posts/<int:id>", PostDelete.as_view()),
    # path("posts/<int:id>", PostGetView.as_view()),
    path("all_posts", UserGet.as_view()),   
    path("like/<int:id>", LikeView.as_view()),   
    path("unlike/<int:id>", UnLikeView.as_view()), 
]
