from django.urls import path

from records.views import (FilteredRecordsView, RecordCreateView,
                           RecordDeleteView, RecordDetailView, RecordsAllView)

urlpatterns = [
    path(
        'records/all/',
        RecordsAllView.as_view(),
        name='records_all'
    ),
    path(
        'record/create/',
        RecordCreateView.as_view(),
        name='record_create'
    ),
    path(
        'record/get',
        RecordDetailView.as_view(),
        name='record_detail'
    ),
    path(
        'records/list',
        FilteredRecordsView.as_view(),
        name='filtered_records'
    ),
    path(
        'record/delete',
        RecordDeleteView.as_view(),
        name='record_delete'
    ),
]
