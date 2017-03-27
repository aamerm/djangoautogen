from django.conf.urls import url
from ..views import (EmployeeListView, EmployeeCreateView, EmployeeDetailView,
                     EmployeeUpdateView, EmployeeDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        # login_required(EmployeeCreateView.as_view()),
        EmployeeCreateView.as_view(),
        name="employee_create"),

    url(r'^(?P<pk>\d+)/update/$',
        # login_required(EmployeeUpdateView.as_view()),
        EmployeeUpdateView.as_view(),
        name="employee_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(EmployeeDeleteView.as_view()),
        name="employee_delete"),

    url(r'^(?P<pk>\d+)/$',
        EmployeeDetailView.as_view(),
        name="employee_detail"),

    url(r'^$',
        EmployeeListView.as_view(),
        name="employee_list"),
]
