import datetime as dt

from rest_framework import status
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     get_object_or_404)
from rest_framework.response import Response
from rest_framework.views import APIView

from records.models import Record
from records.serializers import RecordCreateSerializer, RecordSerializer


class RecordsAllView(ListAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordCreateView(CreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordCreateSerializer


class RecordDetailView(APIView):

    def get(self, request):
        uuid = self.request.query_params.get('uuid')
        if uuid is not None:
            record = get_object_or_404(Record, uuid=uuid)
            serializer = RecordSerializer(record)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            {'Добавьте параметры в запрос!': 'uuid'},
            status=status.HTTP_404_NOT_FOUND
        )


class RecordDeleteView(APIView):

    def get(self, request):
        uuid = self.request.query_params.get('uuid')
        if uuid is not None:
            record = get_object_or_404(Record, uuid=uuid)
            record.delete()
            return Response(
                {'Запись удалена!': uuid},
                status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'Добавьте параметры в запрос!': 'uuid'},
            status=status.HTTP_404_NOT_FOUND
        )


class FilteredRecordsView(APIView):

    def get(self, request):
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        if start is not None and end is not None:
            try:
                start_date = dt.datetime.strptime(start, '%d.%m.%y').date()
                end_date = dt.datetime.strptime(end, '%d.%m.%y').date()
            except Exception:
                return Response(
                    {'Неверный формат даты': (start, end)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            records = Record.objects.filter(
                created__date__range=(start_date, end_date)
            ).order_by('-created')
            serializer = RecordSerializer(records, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        if start is not None:
            try:
                start_date = dt.datetime.strptime(start, '%d.%m.%y').date()
            except Exception:
                return Response(
                    {'Неверный формат даты': (start)},
                    status=status.HTTP_400_BAD_REQUEST
                )
            records = Record.objects.filter(
                created__date__gte=start_date
            ).order_by('-created')
            serializer = RecordSerializer(records, many=True)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        if end is not None:
            try:
                end_date = dt.datetime.strptime(end, '%d.%m.%y').date()
            except Exception:
                return Response(
                    {
                        'Неверный формат даты': (end)
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
            records = Record.objects.exclude(
                created__date__gt=end_date
            ).order_by('-created')
            serializer = RecordSerializer(records, many=True)
            return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
            )
        return Response(
            {'Добавьте параметры в запрос!': ('start', 'end')},
            status=status.HTTP_200_OK
        )
