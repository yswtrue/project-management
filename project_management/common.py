from django.core import serializers
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict


def models_to_dict(models):
    result = [model_to_dict(model) for model in models]
    return result


def ajax_return(fn):
    def exec(*args, **kwargs):
        try:
            result = fn(*args, **kwargs)
            result = serializers.serialize('json', result)
            return JsonResponse({
                'status': 200,
                'data': json.loads(result),
                'message': ''
            })
        except Exception as e:
            if hasattr(e, 'message'):
                result = e.message
            else:
                result = str(e)

            return JsonResponse({
                'status': 500,
                'data': None,
                'message': result
            }, status=500)

    return exec
