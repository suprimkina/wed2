from django.shortcuts import render, reverse, NoReverseMatch
from django.http import HttpResponse, Http404
from django.template.loader import get_template, TemplateDoesNotExist

from .forms import ApplicationModelForm


# Create your views here.
def index(request):
    context = {
        "semester_numbers": [3, 4]
    }
    return render(request, template_name="app1/index.html", context=context)


def jquery_test(request):
    return render(request, template_name="app1/jquery_test.html")


def semester(request, semester_number):
    context = {
        "semester_number": semester_number
    }
    if 3 <= semester_number <= 4:
        if semester_number == 3:
            context['tasks'] = [
                {
                    'name': f'Задание {task_number}',
                    'url': reverse('app1:task',
                                   kwargs=
                                   {"semester_number": semester_number,
                                    "task_name": task_number}
                                   )
                }
                for task_number in range(1, 9)
            ]
        elif semester_number == 4:
            context['tasks'] = [
                {
                    'name': f'{task_name}',
                    'url': reverse('app1:task',
                                   kwargs=
                                   {"semester_number": semester_number,
                                    "task_name": task_name}
                                   )
                }
                for task_name in ['form']
            ]
    else:
        raise Http404("Нет семестра с таким номером")
    return render(request,
                  template_name="app1/semester.html",
                  context=context)


def task(request, semester_number, task_name):
    context = {
        "semester_number": semester_number
    }
    if task_name == "7":
        context["jpg_names"] = [f'app1/media/sem3/{i}.jpg' for i in range(1, 9)]

    if task_name == "form":
        if request.method == 'POST':
            form = ApplicationModelForm(request.POST)
            if form.is_valid():
                form.save()
                context.update({'form': ApplicationModelForm(), "success_status": True})
            else:
                context.update({'form': form, 'success_status': False})
        else:
            form = ApplicationModelForm()
            context.update({'form': form, 'success_status': None})

    template_name = f"app1/sem{semester_number}/task_{task_name}.html"
    try:
        return render(request,
                      template_name=template_name,
                      context=context)
    except TemplateDoesNotExist:
        raise Http404("Нет такой задачи")
