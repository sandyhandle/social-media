from django.urls import path
from .views import Authenticate, LoginView, UserView,FollowerView, UnFollowerView, PostView, UserGet

urlpatterns = [
    path("authenticate",Authenticate.as_view()),
    path("login",LoginView.as_view()),
    path("user",UserView.as_view()),
    path("follow/<int:iid>",FollowerView.as_view()),
    path("unfollow/<int:iid>",UnFollowerView.as_view()),
    path("posts", PostView.as_view()),
    # path("posts/<int:id>", PostDelete.as_view()),
    path("all_posts", UserGet.as_view()),    
]
