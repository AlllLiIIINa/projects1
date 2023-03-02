from django.http import HttpResponseRedirect
# from django.middleware.csrf import get_token
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from groups.forms import GroupCreateForm
from groups.forms import GroupUpdateForm
from groups.models import Group

# from webargs.djangoparser import use_args
# from webargs.fields import Str


def get_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups/list.html', {'groups': groups})


def detail_groups(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(request, 'groups/detail.html', {'group': group})


def create_groups(request):
    if request.method == 'GET':
        form = GroupCreateForm()
    elif request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/create.html', {'form': form})


def update_groups(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        form = GroupUpdateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    form = GroupUpdateForm(instance=group)
    return render(request, 'groups/update.html', {'form': form, 'group': group})


def delete_groups(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))

    return render(request, 'groups/delete.html', {'group': group})
