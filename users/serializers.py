from rest_framework import serializers
from .models import User, Post

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "name", "password","follower","following"]
        extra_kwargs=  {
            'password': {"write_only":True},
            "email": {"write_only":True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id","title", "description","created_time",'author']
      

   