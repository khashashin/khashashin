from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

from me.models import Me
from me.serializers import MeSerializer


class MeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that displays personal information.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Me.objects.all()
    serializer_class = MeSerializer
