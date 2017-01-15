from adoption.models import Ad, Owner
from rest_framework import serializers


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            'id',
            'title',
            'description',
            'created_at',
            'updated_at',
            'type_of_pet',
            'birth_date',
            'neutered',
            'gender',
            'owner_id',
        )


class OwnerSerializer(serializers.ModelSerializer):
    ads = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = (
            'id',
            'name',
            'phone_number',
            'email',
            'ads',
        )
