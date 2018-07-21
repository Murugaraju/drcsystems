from .models import *
import re
import json
from urllib2 import urlopen
# from ipware import get_client_ip
from user_management.config import *


class UsersController:

    def __init__(self):
        pass

    def save_location(self, request, user):
        """
        Function to save the
        :param request: the request object received on the web server
        :return: the status
        """
        try:
            ip_addr = request.META.get("REMOTE_ADDR")
            # ip, is_routable = get_client_ip(request)

            url = 'http://ipinfo.io/%s/json' %ip_addr
            response = urlopen(url)
            data = json.load(response)
            country = 'India'
            if 'bogon' in data.keys():
                # return
                pass
            else:
                ip_addr = data['ip']
                # org = data['org']
                # city = data['city']
                country = data['country']
                # region = data['region']

            user_prof_obj = UserProfile()
            user_prof_obj.country = country
            user_prof_obj.user = user
            user_prof_obj.user_email = user.email
            user_prof_obj.save()

        except Exception, e:
            print "error---fetching the location", e
        return True

    def get_country_code(self, request):
        """
        Function to get country code
        :param request: the request object
        :return: country code
        """
        try:
            country = 'India'
            user_id = request.user.id
            if user_id:
                user_obj = UserProfile.objects.filter(user_id=user_id)
                if len(user_obj)>0:
                    country = user_obj[0].get("country")

            country_code = COUNTRY_CODE_MAP.get('%s' % country)
        except Exception, e:
            print "error---fetching the code", e
        return country_code

