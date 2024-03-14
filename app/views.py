from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class Templatehtml(TemplateView):
    template_name='Templatehtml.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Sona'
        ECDO['age']=23
        return ECDO

class InsertSchoolByTv(TemplateView):
    template_name='InsertSchoolByTv.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['SFO']=SchoolForm
        return ECDO

    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolByTv is done')

class InsertSchoolByFv(FormView):
    template_name='InsertSchoolByFv.html'
    form_class=SchoolForm

    def form_valid(self,form):
        form.save()
        return HttpResponse('InsertSchoolByFv is done')