from django.core import serializers
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict


def models_to_dict(models):
    result = [model_to_dict(model) for model in models]
    return result


def ajax_return(fn):
    def exec(*args, **kwargs):
        result = fn(*args, **kwargs)
        # result = serializers.serialize('json', result)
        return JsonResponse({
            'status': 200,
            'data': result
        })
    return exec
