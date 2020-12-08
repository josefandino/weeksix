from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from ..publications.serializer import PublicationSerializer
from ..comments.serializer import CommentSerializer
from ..publications.models import Publication
from ..tags.serializer import TagSerializer
from ..tags.models import Tag


<<<<<<< HEAD
class Tagviewsets(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def publicaciones(self, request, pk=None):
        tag = self.get_object()
        if request.method == 'GET':
            id = Publication.objects.filter(tags=int(tag.id))
            serialized = PublicationSerializer(id, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method == 'POST':
            publication = PublicationSerializer(data=request.data)
            if publication.is_valid():
                publication.save()
                return Response(status=status.HTTP_201_CREATED)
        else:
                return Response(status=status.HTTP_400_BAD_REQUEST, )
        if request.method == 'DELETE':
            publicaciones_id = request.data['id']
            for publicaciones_id in publicaciones_id:
                publicaciones = Publication.objects.get(id=int(publicaciones_id))
                publicaciones.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
=======
class TagViewSet(viewsets.ModelViewSet):
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
>>>>>>> 13ddd2046f9259766f16ab407bf620a236704a09
