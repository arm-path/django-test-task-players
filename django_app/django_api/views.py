from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from django_app.django_api.serializers import CommentsSerializer
from django_app.models import Comments


class CommentsViewSet(CreateModelMixin, ListModelMixin, GenericViewSet, ):
    """ Представление данных Comments GET AND CREATE """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    """ Фильтры backend """
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['player']
    ordering_fields = ['publication_date']
