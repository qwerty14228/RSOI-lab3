from django.http import HttpResponse

from rest_framework import permissions, viewsets

from rsoi_rating_app.models import Rating
from rsoi_rating_app.serializers import RatingSerializer

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.AllowAny]
    def get_queryset(self):
        return Rating.objects.filter(username=self.request.user.username).order_by('id')


def healthcheck_view(request):
    
    return HttpResponse("")
