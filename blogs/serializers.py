
from rest_framework import fields, serializers
from .models import Blog

class BlogSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='data.username')

    class Meta:
        model=Blog
        fields = ['id','title','tags','body','author']
