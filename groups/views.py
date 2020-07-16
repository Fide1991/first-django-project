from django.shortcuts import render
from .models import GroupModel

# Create your views here.
def GetGroups(request):
    agroups = GroupModel.objects.all()
    template_name = 'groups/list.html'
    context = {
        'all_groups':agroups
    }
    return render(request, template_name, context)

def GetGroup(request, id):
    group = GroupModel.objects.get(id=id)
    template_name = 'groups/detail.html'
    context = {
        'group':group
    }
    return render(request, template_name, context)

    