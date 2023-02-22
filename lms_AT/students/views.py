from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render  # noqa

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateStudentForm
from .models import Student
from .utils import qs2html


# HttpRequest
def index(request):
    return HttpResponse('Welcome to LMS!')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query'
)
def get_students(request, args):
    students = Student.objects.all()

    if len(args) != 0 and args.get('first_name') or args.get('last_name'):
        students = students.filter(
            Q(first_name=args.get('first_name', '')) | Q(last_name=args.get('last_name', ''))
        )

    # if 'first_name' in args:
    # if 'last_name' in args:
    #     students = students.filter(first_name=args['first_name'])
    #
    #     students = students.filter(last_name=args['last_name'])

    html = qs2html(students)

    # HttpResponse
    response = HttpResponse(html)
    return response


def create_student(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f"""
            <form method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
                <table>
                    {form.as_table()}
                </table>
                <input type="submit" value="Submit">
            </form>
        """

    return HttpResponse(html_form)
