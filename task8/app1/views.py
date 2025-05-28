from django.shortcuts import render, reverse, NoReverseMatch
from django.http import HttpResponse, Http404
from django.template.loader import get_template, TemplateDoesNotExist
from django.views.generic import TemplateView, FormView, UpdateView
from django.views.generic.base import ContextMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import ApplicationModelForm
from .models import Application


# Create your views here.
class IndexView(TemplateView):
    template_name = 'app1/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['semester_numbers'] = [3, 4]
        return context


class JqueryTestView(TemplateView):
    template_name = 'app1/jquery_test.html'


class SemesterView(TemplateView):
    template_name = 'app1/semester.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semester_number = self.kwargs.get('semester_number')
        if semester_number == 3:
            context['semester_number'] = semester_number
            context['tasks'] = [
                {
                    'name': f'Задание {task_name}',
                    'url': reverse('app1:task',
                                   kwargs={"semester_number": semester_number,
                                           "task_name": task_name}
                                   )
                }
                for task_name in range(1, 9)
            ]

        elif semester_number == 4:
            context['semester_number'] = semester_number
            context['tasks'] = [
                {
                    'name': 'form',
                    'url': reverse('app1:task',
                                   kwargs={"semester_number": 4,
                                           "task_name": 'form'}
                                   )
                }
            ]

        else:
            raise Http404("Нет семестра с таким номером")

        return context


class TaskView(TemplateView):
    def get_template_names(self):
        semester_number = self.kwargs.get('semester_number')
        task_name = self.kwargs.get('task_name')
        template_name = f"app1/sem{semester_number}/task_{task_name}.html"
        try:
            return get_template(template_name)
        except TemplateDoesNotExist:
            raise Http404("Нет такой задачи")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        semester_number = self.kwargs.get('semester_number')
        task_name = self.kwargs.get('task_name')
        context['semester_number'] = semester_number
        context['task_name'] = task_name
        if task_name == "7":
            context["jpg_names"] = [f'app1/media/sem3/{i}.jpg' for i in range(1, 9)]
        return context


class TaskFormView(LoginRequiredMixin, UpdateView):
    template_name = 'app1/sem4/task_form.html'
    form_class = ApplicationModelForm
    model = Application
    login_url = 'account:sign_up'
    success_url = reverse_lazy('app1:task', kwargs={'semester_number': 4, 'task_name': 'form'})
    extra_context = {
        'semester_number': 4,
        'task_name': 'form'
    }

    def get_object(self, queryset=None):
        try:
            return self.model.objects.get(user=self.request.user)
        except self.model.DoesNotExist:
            return self.model(user=self.request.user)

    def form_valid(self, form):
        application = form.save(commit=False)
        application.user = self.request.user
        # application.save()
        messages.success(self.request, 'Данные успешно сохранены, спасибо!')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
