from django.conf.urls import include, url

urlpatterns = [

    url(r'', include('fas.urls.employee_urls')),  # NOQA
]
