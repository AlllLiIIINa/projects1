from django.http import HttpResponseRedirect
# from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from groups.forms import CreateGroupForm
from groups.forms import UpdateGroupForm
from groups.models import Group

from webargs.djangoparser import use_args
from webargs.fields import Str


@use_args(
    {
        'name': Str(required=False),
    },
    location='query'
)
def get_groups(request, args):
    groups = Group.objects.all()

    if 'name' in args:
        groups = groups.filter(name=args['name'])

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'title': 'List of groups',
            'groups': groups
        }
    )


def detail_groups(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def create_groups(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/create.html', {'form': form})


def update_groups(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/update.html', {'form': form})


def delete_groups(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
