# Add filters here

import django_filters
from .models import Profile


class FriendFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name="username",lookup_expr="icontains")
    class Meta:
        model = Profile
        fields = ['username']
        #exclude = ['friends','img',"user_id"]
