from rest_framework import serializers

from django_app.models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['player', 'comment_text', 'publication_date']


