from django.http import HttpResponse

from rest_framework import permissions, viewsets

from rsoi_reservation_app.models import Reservation
from rsoi_reservation_app.serializers import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ('status', 'reservation_uid')

    def get_queryset(self):
        return Reservation.objects.filter(username=self.request.user.username)
 

def healthcheck_view(request):
    
    return HttpResponse("")
