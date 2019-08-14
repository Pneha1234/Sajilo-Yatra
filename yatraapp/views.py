from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# class BaseView(TemplateView):
#     template_name = 'base.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['active'] = 'base'
#
#         return context
#
#
# class HomeView(TemplateView):
#    template_name = 'home.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['active'] = 'home'

#        return context

#
# class FoodView(TemplateView):
#     template_name = 'food.html'
#
#     def get_context_data(self, **kwargs):
#         # get all food value
#         allFoods = Food.objects.all();
#
#         # get template
#         template = loader.get_template('food.html')
#
#         context = {
#             'foodData': allFoods,
#         }
#
#         return HttpResponse(template.render(context))
#
#         # context = super().get_context_data(**kwargs)
#         # context['active'] = 'food'
#         #
#         # return context
#
#     # def searchfood(selfrequest):
#     #  if request.method == 'POST':
#     #  if request.POST.get(location)
#
#
# class FestivalView(TemplateView):
#     template_name = 'festival.html']]
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['active'] = 'festival'
#
#         return context
#
#
# class Contact_View(TemplateView):
#    template_name = 'contact.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['active'] = 'contact'

#        return context

def foodview(request):
    food = Food.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(food, 6)
    try:
        food = paginator.page(page)
    except PageNotAnInteger:
        food = paginator.page(1)
    except EmptyPage:
        food = paginator.page(paginator.num_pages)
    return render(request, 'food.html', {'food': food})


def categoryview(request):
    breakfast = Food.objects.filter(category='Breakfast')
    return render(request, 'category.html', {'breakfast': breakfast})

# def ethnicview(request):
#    newari = Festivals.objects.filter(category='newari')
#   return render(request,'ethnic.html',{'newari':newari})


def festivalview(request):
    festival = Festival.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(festival, 6)
    try:
        festival = paginator.page(page)
    except PageNotAnInteger:
        festival = paginator.page(1)
    except EmptyPage:
        festival = paginator.page(paginator.num_pages)
    return render(request, 'festival.html', {'festival': festival})


def HomeView(request):

    return render(request, 'home.html')
