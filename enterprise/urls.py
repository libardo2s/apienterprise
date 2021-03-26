from django.urls import path

from enterprise.views import EnterpriseApi

urlpatterns = [
    path('enterprise/', EnterpriseApi.as_view()),
    path('enterprise/<int:id>/', EnterpriseApi.as_view()),
]
