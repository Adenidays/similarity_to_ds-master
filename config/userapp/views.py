from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from userapp.models import User
from userapp.serializers import CustomUserSerializer


class GetAllUsersView(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = CustomUserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)
