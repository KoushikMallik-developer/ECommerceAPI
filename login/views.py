from rest_framework.decorators import api_view
from rest_framework.response import Response
from login.models import User
from login.serializers import UserSerializer


# Create your views here.

@api_view(('GET',))
def get_all_users(request):
    if request.method == "GET":
        all_products = User.objects.all()
        all_products_serialized = UserSerializer(all_products, many=True)
        return Response(all_products_serialized.data)
