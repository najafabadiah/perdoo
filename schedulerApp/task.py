from .models import Request

def reverse_request_title(request_id):
    request = Request.objects.get(id=request_id)
    request.title = request.title[::-1]
    request.changeStatus('completed')
    request.save()
    return request