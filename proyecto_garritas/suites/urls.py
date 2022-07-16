from django.urls import path

from proyecto_garritas.suites.views import suites_detail_view

app_name = "suites"
urlpatterns = [
    path("<str:name>/", view=suites_detail_view, name="detail"),
]
