"""
URL configuration for hh_back project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
from api.views import (
    CompanyListView, CompanyDetailView,
    VacancyListView, VacancyDetailView,
    CompanyListAPIView, CompanyDetailAPIView
)
#VacancyCreateView, VacancyUpdateView, VacancyDeleteView,
#CompanyCreateView, CompanyUpdateView, CompanyDeleteView,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', views.testingCompany, name='company_list'),
    path('company/<int:company_id>/', views.company_detail, name='company_detail'),
    path('vacancy/', views.testingVacancy, name='vacancy_list'),
    path('vacancy/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
    path('vacancies_sorted/', views.vacancy_sorted, name='vacancy_sorted_by_salary'),
    path('company/<int:company_id>/vacancies/', views.vacancies_by_company, name='vacancies_by_company'),
    #----------class based
    # Companies
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company_detail'),
    # path('companies/create/', CompanyCreateView.as_view(), name='company_create'),
    # path('companies/<int:pk>/update/', CompanyUpdateView.as_view(), name='company_update'),
    # path('companies/<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete'),
    # Vacancies
    path('vacancies/', VacancyListView.as_view(), name='vacancy_list'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail'),
    # path('vacancies/create/', VacancyCreateView.as_view(), name='vacancy_create'),
    # path('vacancies/<int:pk>/update/', VacancyUpdateView.as_view(), name='vacancy_update'),
    # path('vacancies/<int:pk>/delete/', VacancyDeleteView.as_view(), name='vacancy_delete'),

    path('companiesserializer/', CompanyListAPIView.as_view(), name='company_list_api'),
    path('companiesserializer/<int:pk>/', CompanyDetailAPIView.as_view(), name='company_detail_api'),
]



