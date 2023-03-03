# from django.db.models import Q
from django.http import HttpResponseRedirect
# from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from teachers.forms import TeacherCreateForm
from teachers.forms import TeacherFilterForm
from teachers.forms import TeacherUpdateForm
from teachers.models import Teacher

# from webargs.djangoparser import use_args
# from webargs.fields import Str


def get_teachers(request):
    teachers = Teacher.objects.all()

    filter_form = TeacherFilterForm(data=request.GET, queryset=teachers)
    return render(request, 'teachers/list.html', {'filter_form': filter_form})


def detail_teachers(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request, 'teachers/detail.html', {'teacher': teacher})


def create_teachers(request):
    if request.method == 'GET':
        form = TeacherCreateForm()
    elif request.method == 'POST':
        form = TeacherCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/create.html', {'form': form})


def update_teachers(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        form = TeacherUpdateForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('teachers:list'))

    form = TeacherUpdateForm(instance=teacher)
    return render(request, 'teachers/update.html', {'form': form, 'teacher': teacher})


def delete_teachers(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))

    return render(request, 'teachers/delete.html', {'teacher': teacher})
