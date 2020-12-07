# Create your views here.
from rest_framework import viewsets

from apps.comments.models import Comment
from apps.comments.serializer import CommentSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
