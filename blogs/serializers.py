
from rest_framework import fields, serializers
from .models import Blog

class BlogSerializers(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.email',required=False)
    author_id = serializers.CharField(source='author.id',required=False)

    class Meta:
        model=Blog
        fields = ['id','title','tags','body','author_id','author_name','date']
