from django.utils.deprecation import MiddlewareMixin
from utils.functions import request_allowed
from rest_framework.exceptions import Throttled


class RequestRestrictionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request_allowed():
            return None
        raise Throttled(detail=f"Access to API is throttled.")
