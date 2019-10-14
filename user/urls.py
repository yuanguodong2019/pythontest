from django.conf.urls import url
from.views import list
from.views import add
from.views import delete
from.views import edit

urlpatterns = [
    url(r'^list/', list),
    url(r'^add/', add),
    url(r'^delete/', delete),
    url(r'^edit/', edit),
]