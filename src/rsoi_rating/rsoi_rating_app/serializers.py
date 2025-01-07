from rest_framework import serializers

from rsoi_rating_app.models import Rating


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'username', 'stars']