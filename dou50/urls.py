
from django.contrib import admin
from django.urls import path

from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('obr_standarti/', TemplateView.as_view(template_name='obr_standarti.html'), name='obr_standarti'),
    path('struktura_upravlenia/', TemplateView.as_view(template_name='struktura_upravlenia.html'), name='struktura_upravlenia'),
    path('obrazovanie/', TemplateView.as_view(template_name='obrazovanie.html'), name='obrazovanie'),
    path('documenti/', TemplateView.as_view(template_name='documenti.html'), name='documenti'),
    path('poryadok_priema_v_dou/', TemplateView.as_view(template_name='poryadok_priema_v_dou.html'), name='poryadok_priema_v_dou'),
    path('roditelskaya_oplata/', TemplateView.as_view(template_name='roditelskaya_oplata.html'), name='roditelskaya_oplata'),
    path('admin/', admin.site.urls),

]
