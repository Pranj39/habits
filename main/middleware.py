from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
import pytz
class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            tzname = None

            tz_cookie = request.COOKIES.get('tz')
            if tz_cookie in pytz.all_timezones:
                tzname = tz_cookie
                profile = getattr(request.user, 'profile', None)
                if profile and profile.timezone != tzname:
                    profile.timezone = tzname
                    profile.save()

            if tzname:
                print(timezone.get_current_timezone_name())
                timezone.activate(tzname)
                print(timezone.get_current_timezone_name())
            else:
                print("NOT")
                timezone.deactivate()