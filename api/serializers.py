from rest_framework import serializers

from Posts.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title" , "post" , "auth" , "create_at" , "update_at")