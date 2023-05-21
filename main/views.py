from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Contact
from main.serializer import ContactSerializer
from main.tasks import send_email


# Create your views here.
class ContactView(APIView):
    model = Contact

    def post(self, request):
        print(request.data)
        serializer = ContactSerializer(data=request.data, many=False)
        serializer.is_valid(raise_exception=True)

        Contact.objects.create(
            email=request.data.get('email'),
            name=request.data.get('name'),
        ).save()

        send_email.delay(request.data.get('email'))

        return Response(serializer.data)
