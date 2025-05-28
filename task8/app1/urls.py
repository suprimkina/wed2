from django.urls import include, path

from . import views

app_name = "app1"


def task_dispatcher(request, semester_number, task_name):
    if task_name == 'form':
        view_class = views.TaskFormView.as_view()
    else:
        view_class = views.TaskView.as_view()

    return view_class(request, semester_number=semester_number, task_name=task_name)


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('semester/<int:semester_number>/', views.SemesterView.as_view(), name="semester"),
    path('semester/<int:semester_number>/task/<str:task_name>/', task_dispatcher, name="task"),
    path('jquery_test/', views.JqueryTestView.as_view(), name="jquery_test")
]
