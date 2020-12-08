# Create your views here.
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from ..comments.models import Comment
from ..comments.serializer import CommentSerializer
from ..publications.serializer import PublicationSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def publications(self, request, pk=None):
        Comment = self.get_object()
        if request.method == 'GET':
            serialized = PublicationSerializer(Comment.publicaciones, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
