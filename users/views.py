from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializers, PostSerializers
from .models import User, Post
import jwt
import datetime


class Authenticate(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data["email"]
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password..!")

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }
        # return Response({
        #     "message":"Success..!"
        # })

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        user = User.objects.filter(id=payload["id"])
        response.data = {
            'jwt': token,
        }

        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializers(user)
        return Response(serializer.data)


class FollowerView(APIView):

    def post(self, request, iid):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        # if iid not in user.follower_list:
        # user.follower_list.append(iid)
        user.follower += 1
        user.save()
        serializer = UserSerializers(user)

        return Response(serializer.data)


class UnFollowerView(APIView):

    def post(self, request, iid):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        # if iid in user.follower_list:
        # user.follower_list.remove(iid)
        user.follower -= 1
        user.save()
        # else:
        #     raise AuthenticationFailed('Unknown user!')
        serializer = UserSerializers(user)

        return Response(serializer.data)


class PostView(APIView):
    def post(self, request):

        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        request.data["author"] = payload['id']
        print(request.data["author"], request.data["title"],
              request.data["description"])
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class PostDelete(APIView):
    def delete(self, request, id):

        token = request.COOKIES.get('jwt')
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        posts = Post.objects.get(id=id)
        posts.delete()
        return Response("Geetha aa a  is awesomeeeeeee...!")


class UserGet(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        # print(payload)
        # user = User.objects.filter(id=payload['id']).first()
        posts = Post.objects.filter(author=payload['id'])

        # print(posts)

        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)


# class LikeView(APIView):

#     def post(self, request, iid):

#         token = request.COOKIES.get('jwt')
#         payload = jwt.decode(token, 'secret', algorithms=['HS256'])

#         posts = Post.objects.get(id=iid)
#         # print(posts)
#         posts.like += 1
#         posts.save()

#         # serializer = PostSerializers(posts)

#         return Response("Working")
    
class LikeView(APIView):
    def post(self, request, id):

        # token = request.COOKIES.get('jwt')
        # payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        posts = Post.objects.get(id=id)
        posts.like += 1
        posts.save()
        return Response("Post working with the like..")
    
class UnLikeView(APIView):
    def post(self, request, id):

        # token = request.COOKIES.get('jwt')
        # payload = jwt.decode(token, 'secret', algorithms=['HS256'])

        posts = Post.objects.get(id=id)
        posts.like -= 1
        posts.save()
        return Response("Post working with the like..")


# class PostGetView(APIView):
#     def get(self, request,id):
#         token = request.COOKIES.get('jwt')

#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#         try:
#             payload = jwt.decode(token, 'secret', algorithms=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')
#         # print(payload)
#         # user = User.objects.filter(id=payload['id']).first()
#         posts = Post.objects.filter(id=id)

#         # print(posts)

#         serializer = PostSerializers(posts)
#         return Response(serializer.data)