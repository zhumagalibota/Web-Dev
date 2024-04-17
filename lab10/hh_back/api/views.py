from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Company, Vacancy
from django.core import serializers
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



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


def vacancy_detail(request, vacancy_id):
    vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
    data = serializers.serialize('json', [vacancy])
    return HttpResponse(data, content_type='application/json')


def vacancy_sorted(request):
    vacancies = Vacancy.objects.order_by('-salary')  
    data = serializers.serialize('json', vacancies)
    return HttpResponse(data, content_type='application/json')


def vacancies_by_company(request, company_id):
    company = Company.objects.get(pk=company_id)
    vacancies = Vacancy.objects.filter(company=company).values('name', 'description', 'salary')
    vacancies_data = list(vacancies) 
    return JsonResponse({'company': company.name, 'vacancies': vacancies_data})


#--------CLASS BASED

# Companies
class CompanyListView(ListView):
    model = Company

    def render_to_response(self, context, **response_kwargs):
        companies = list(context['object_list'].values())
        return JsonResponse({'companies': companies})

class CompanyDetailView(DetailView):
    model = Company

    def render_to_response(self, context, **response_kwargs):
        company = context['object']
        return JsonResponse({'company': {
            'id': company.id,
            'name': company.name,
            'description': company.description,
            'city': company.city,
            'address': company.address
        }})

# class CompanyCreateView(CreateView):
#     model = Company
#     fields = ['name', 'description', 'city', 'address']

#     def form_valid(self, form):
#         self.object = form.save()
#         data = {
#             'id': self.object.id,
#             'name': self.object.name,
#             'description': self.object.description,
#             'city': self.object.city,
#             'address': self.object.address
#         }
#         return JsonResponse({'company': data})

#     def form_invalid(self, form):
#         return JsonResponse({'errors': form.errors}, status=400)

# class CompanyUpdateView(UpdateView):
#     model = Company
#     fields = ['name', 'description', 'city', 'address']

#     def form_valid(self, form):
#         self.object = form.save()
#         data = {
#             'id': self.object.id,
#             'name': self.object.name,
#             'description': self.object.description,
#             'city': self.object.city,
#             'address': self.object.address
#         }
#         return JsonResponse({'company': data})

#     def form_invalid(self, form):
#         return JsonResponse({'errors': form.errors}, status=400)

# class CompanyDeleteView(DeleteView):
#     model = Company
#     success_url = reverse_lazy('company_list')

#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         return JsonResponse({'success': 'Company deleted'}, status=204)

# Vacancies
class VacancyListView(ListView):
    model = Vacancy

    def render_to_response(self, context, **response_kwargs):
        vacancies = list(context['object_list'].values())
        return JsonResponse({'vacancies': vacancies})

class VacancyDetailView(DetailView):
    model = Vacancy

    def render_to_response(self, context, **response_kwargs):
        vacancy = context['object']
        return JsonResponse({'vacancy': {
            'id': vacancy.id,
            'name': vacancy.name,
            'description': vacancy.description,
            'salary': vacancy.salary,
            'company': vacancy.company.name
        }})

# class VacancyCreateView(CreateView):
#     model = Vacancy
#     fields = ['name', 'description', 'salary', 'company']

#     def form_valid(self, form):
#         self.object = form.save()
#         data = {
#             'id': self.object.id,
#             'name': self.object.name,
#             'description': self.object.description,
#             'salary': self.object.salary,
#             'company': self.object.company.name
#         }
#         return JsonResponse({'vacancy': data})

#     def form_invalid(self, form):
#         return JsonResponse({'errors': form.errors}, status=400)

# class VacancyUpdateView(UpdateView):
#     model = Vacancy
#     fields = ['name', 'description', 'salary', 'company']

#     def form_valid(self, form):
#         self.object = form.save()
#         data = {
#             'id': self.object.id,
#             'name': self.object.name,
#             'description': self.object.description,
#             'salary': self.object.salary,
#             'company': self.object.company.name
#         }
#         return JsonResponse({'vacancy': data})

#     def form_invalid(self, form):
#         return JsonResponse({'errors': form.errors}, status=400)

# class VacancyDeleteView(DeleteView):
#     model = Vacancy
#     success_url = reverse_lazy('vacancy_list')

#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#         self.object.delete()
#         return JsonResponse({'success': 'Vacancy deleted'}, status=204)


#-------------------using serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CompanySerializer, VacancySerializer

# Companies
class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
