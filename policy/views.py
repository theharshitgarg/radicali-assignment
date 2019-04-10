# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


from .models import Policy

# Create your views here.


@require_http_methods(["GET"])
def details_view(request, p_id):
    policy = get_object_or_404(Policy, pk=p_id)

    kwargs = locals()
    return render(request, 'policy/details.html', kwargs)


def list_view(request):
    # TODO : handle pagination
    policies = Policy.objects.all()
    kwargs = locals()

    return render(request, 'policy/list.html', kwargs)


@csrf_protect
@require_http_methods(["POST"])
def update_policy(request, p_id):

    success = False
    data = ""
    try:
        data = request.POST['policy_text']
        policy = get_object_or_404(Policy, pk=p_id)
        policy.text = data
        policy.save()

        success = True
    except Exception as e:
        print "Error occurred : " + str(e)
        success = False

    json = {
        "data": data,
        "success": True,
    }

    return JsonResponse(json)
