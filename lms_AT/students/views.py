# from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

# from webargs.djangoparser import use_args
# from webargs.fields import Str

from .forms import StudentCreateForm
from .forms import StudentFilterForm
from .forms import StudentUpdateForm
from .models import Student


# @use_args(
#     {
#         'first_name': Str(required=False),
#         'last_name': Str(required=False),
#     },
#     location='query'
# )
def get_students(request):
    students = Student.objects.all()

    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    # if len(args) != 0 and args.get('first_name') or args.get('last_name'):
    #     students = students.filter(
    #         Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
    #     )
    #
    # # if 'first_name' in args:
    # # if 'last_name' in args:
    # #     students = students.filter(first_name=args['first_name'])
    # #
    # #     students = students.filter(last_name=args['last_name'])
    #
    return render(request, 'students/list.html', {'filter_form': filter_form})


def detail_students(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'students/detail.html', {'student': student})


def create_students(request):
    if request.method == 'GET':
        form = StudentCreateForm()
    elif request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/create.html', {'form': form})


def update_students(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentUpdateForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    form = StudentUpdateForm(instance=student)
    return render(request, 'students/update.html', {'form': form, 'student': student})


def delete_students(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return HttpResponseRedirect(reverse('students:list'))

    return render(request, 'students/delete.html', {'student': student})
