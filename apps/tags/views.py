from apps.tags.serializer import TagSerializer
from apps.tags.models import Tag
from rest_framework import generics, viewsets, status
from apps.publications.serializer import PublicationSerializer
from apps.publications.models import Publication
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
class Tagviewsets(viewsets.ModelViewSet) :
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def publicaciones(self, request, pk=None) :
        tag = self.get_object()
        if request.method == 'GET' :
            id =Publication.objects.filter(tags=int(tag.id))
            serialized = PublicationSerializer(id, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method == 'POST' :
            publication = PublicationSerializer(data=request.data)
            if publication.is_valid() :
                publication.save()
                return Response(status=status.HTTP_201_CREATED)
            else :
                return Response(status=status.HTTP_400_BAD_REQUEST, data=entrada.errors)
        if request.method == 'DELETE' :
            publicaciones_id = request.data['id']
            for publicaciones_id in publicaciones_id :
                publicaciones = Publication.objects.get(id=int(publicaciones_id))
                publicaciones.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)