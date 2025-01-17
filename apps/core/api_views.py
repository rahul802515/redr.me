from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

from .models import Link
from .serializers import (
    LinkSerializer,
    LinkPublicSerializer,
    LinkEditSerializer
)


class LinkCreateAPIView(generics.CreateAPIView):

    model = Link
    serializer_class = LinkSerializer
    permission_classes = [AllowAny, ]

class LinkRetrieveAPIView(generics.RetrieveAPIView):

    model = Link
    serializer_class = LinkPublicSerializer
    queryset = model.objects.all()
    permission_classes = [AllowAny, ]

    def get_object(self):
        try:
            self.get_queryset().get(code=self.kwargs['code'])
        except self.model.DoesNotExist:
            raise NotFound()

class LinkEditAPIView(generics.UpdateAPIView):
    model = Link
    queryset = model.objects.all()
    serializer_class = LinkEditSerializer
    lookup_field = 'token'
    permission_classes = [AllowAny, ]