from django.core import serializers
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from django.db import models


def models_to_dict(models):
    result = [model_to_dict(model) for model in models]
    return result


def ajax_return(fn):
    def exec(*args, **kwargs):
        result = fn(*args, **kwargs)
        result = serializers.serialize('geojson')
        return JsonResponse(
            {
                'status': 200,
                'data': json.loads(result),
                'message': ''
            },
            safe=False
        )
    return exec
