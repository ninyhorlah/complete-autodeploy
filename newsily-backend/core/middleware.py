from core.models import StoreRequestInfoInEpoch
from django.utils.deprecation import MiddlewareMixin

class CheckEveryRequestAndSaveToDatabase(MiddlewareMixin):
    
    def process_request(self, request):
        new_request_info = str(request)

        # datetime now in epoch time
        import datetime

        now_in_epoch = int(datetime.datetime.now().timestamp())

        # save to database
        StoreRequestInfoInEpoch.objects.create(
            epoch_time=now_in_epoch, request_info=new_request_info
        )
