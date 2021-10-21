from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from blogs.serializers import BlogSerializers
from .models import Blog
import sys
sys.path.append("..")
from rest_framework.exceptions import AuthenticationFailed
import jwt
class ManageBlog(APIView):
    def checkIsAuthenticated(self, request):
        token = request.headers['Authorization']
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithms='HS256')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        return payload

    def post(self, request):
        try:
            payload =self.checkIsAuthenticated(request)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        serializers = BlogSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        user=User.objects.get(id=payload['id'])
        serializers.save(author=user)

        return Response({
            'status':"true",
            'data':serializers.data})
    def put(self,request,id):
        
        payload =self.checkIsAuthenticated(request)
        try:
            blog=Blog.objects.get(id=id) 
        except ValueError:
            return Response({'message': 'The tutorial does not exist'}) 

        serializers = BlogSerializers(blog,data=request.data)
        serializers.is_valid(raise_exception=True)
        user=User.objects.get(id=payload['id'])
        serializers.save(author=user)
        return Response({
            "success":"success"
        })
    def get(self, request):
        blog = Blog.objects.all()
        serializer = BlogSerializers(blog, many=True)
        return Response({
            "status":True,
            "data":serializer.data
            })
            

class getTagList(APIView):
    def get(self, request,tag):
        blog = Blog.objects.filter(tags__contains=tag+",")
        serializer = BlogSerializers(blog, many=True)
        return Response({
            "status":True,
            "data":serializer.data
            })
class getBlog(APIView):
    def get(self, request,id):
        blog = Blog.objects.filter(id=id).first()
        serializer = BlogSerializers(blog)
        return Response({
            "status":True,
            "data":serializer.data
            })
