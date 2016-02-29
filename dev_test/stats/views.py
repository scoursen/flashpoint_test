from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
import json
from stats import models
from django.utils import timezone

def get_stats(request):
    try:
        time_start = timezone.now() - timezone.timedelta(minutes=1)
        latest = models.Messages.objects.filter(create_time__gte=time_start).aggregate(num_cities=Count('city'), num_users=Count('username'))
        response = {
            'result': 'success',
            'cities': latest['num_cities'],
            'users': latest['num_users']
        }
    except Exception as e:
        response = {
            'result': 'error',
            'error': e.message
        }
    return HttpResponse(json.dumps(response), content_type='application/json')
