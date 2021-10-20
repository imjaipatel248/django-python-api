from rest_framework.views import APIView
from rest_framework.response import Response
from users.serializers import UserSerializers

class RegisterView(APIView):
    def post(self, request):
        serializers = UserSerializers(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)
