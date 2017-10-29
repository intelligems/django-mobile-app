from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from rest_framework.permissions import IsAuthenticated

from .serializers import AccountSerializer


class MeApiHandler(RetrieveUpdateAPIView):
    """
    API Endpoint that returns currently logged-in account's user information.
    This includes information that is not publicly-available.
    """
    permission_classes(IsAuthenticated)
    parser_classes = [FormParser, MultiPartParser, JSONParser]
    serializer_class = AccountSerializer

    def get_object(self):
        return self.request.user
