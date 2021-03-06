from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_object': obj,
                                                       'detail': True})

class ObjectCreateMixin:
    model = None
    model_form = None
    template = 'airtickets/create_form.html'

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form, 'type_obj': self.model.__name__.lower()})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)

        return render(request, self.template, context={'form': bound_form, 'type_obj': self.model.__name__.lower()})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = 'airtickets/update_form.html'

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, 'obj': obj, 'type_obj': self.model.__name__.lower()})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)

        return render(request, self.template, context={'form': bound_form, 'obj': obj, 'type_obj': self.model.__name__.lower()})


class ObjectDeleteMixin:
    model = None
    template = 'airtickets/delete_form.html'
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        return render(request, self.template, context={'obj': obj, 'type_obj': self.model.__name__.lower()})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))