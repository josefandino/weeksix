from apps.publications.serializer import PublicationSerializer
from apps.tags.serializer import TagSerializer
from apps.tags.models import Tag
from apps.publications.models import Publication
from apps.comments.serializer import CommentSerializer
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def tags(self, request, pk=None):
        Publication = self.get_object()
        if request.method == 'GET':
            serialized = TagSerializer(Publication.tags, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method == 'POST':
            publications_id = request.data['publications']
            for tag_id in publications_id:
                tags = Publication.objects.get(id=int(tag_id))
                publications_id.publicaciones.add(tags)
                return Response(status=status.HTTP_201_CREATED)
        if request.method == 'DELETE':
            paublications_id = request.data['publications']
            for tag_id in publications_id:
                tag = Tag.objects.get(id=int(tag_id))
                publications.tags.remove(tag)
                return Response(status=status.HTTP_204_NO_CONTENT)
