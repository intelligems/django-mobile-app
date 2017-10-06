from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AccountSerializer


class MeApiHandler(APIView):
    """
    API Endpoint that returns currently logged-in account's user information.
    This includes information that is not publicly-available.
    """
    permission_classes(IsAuthenticated)

    def get(self, request):
        user = self.request.user
        serializer = AccountSerializer(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)
