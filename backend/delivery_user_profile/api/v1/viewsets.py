from rest_framework import authentication
from delivery_user_profile.models import Profile, ContactInfo
from .serializers import ProfileSerializer, ContactInfoSerializer
from rest_framework import viewsets


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Profile.objects.all()


class ContactInfoViewSet(viewsets.ModelViewSet):
    serializer_class = ContactInfoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = ContactInfo.objects.all()
