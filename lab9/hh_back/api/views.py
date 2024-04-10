from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Company, Vacancy
from django.core import serializers

# Create your views here.
def testingCompany(request):
    companies = Company.objects.all()
    data = serializers.serialize('json', companies)
    return HttpResponse(data, content_type='application/json')

def testingVacancy(request):
    vacancies = Vacancy.objects.all()
    data = serializers.serialize('json', vacancies)
    return HttpResponse(data, content_type='application/json')


def company_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    data = serializers.serialize('json', [company])
    return HttpResponse(data, content_type='application/json')


def vacancy_detail(request, company_id):
    vacancy = get_object_or_404(Vacancy, pk=company_id)
    data = serializers.serialize('json', [Vacancy])
    return HttpResponse(data, content_type='application/json')


def vacancy_sorted(request):
    vacancies = Vacancy.objects.order_by('-salary')  
    data = serializers.serialize('json', vacancies)
    return HttpResponse(data, content_type='application/json')


def vacancies_by_company(request, company_id):
    company = Company.objects.get(pk=company_id)
    vacancies = Vacancy.objects.filter(company=company).values('name', 'description', 'salary')
    vacancies_data = list(vacancies)  # Convert QuerySet to list for JSON serialization
    return JsonResponse({'company': company.name, 'vacancies': vacancies_data})