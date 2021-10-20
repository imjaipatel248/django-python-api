from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

class RegisterView(APIView):
    def post(self, request):
        pass
        # serializers = UserSerializers(data=request.data)
        # serializers.is_valid(raise_exception=True)
        # serializers.save()
        # return Response(serializers.data)