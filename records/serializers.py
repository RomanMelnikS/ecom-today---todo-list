from rest_framework import serializers

from records.models import Record


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = (
            'pk',
            'uuid',
            'body',
            'created',
            'active'
        )


class RecordCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = (
            'body',
        )

    def to_representation(self, instance):
        serializer = RecordSerializer(
            instance,
            context=self.context
        )
        return serializer.data
