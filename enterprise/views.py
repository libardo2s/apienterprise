from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# MODELS
from enterprise.models import Enterprise

# SERIALIZSERS
from enterprise.enterprise import EnterpriseSerializer


# Create your views here.

def validate_nit(nit: str):
    """
    Valida si el nit es correcto.
    """
    nit = nit.strip()

    if not bool(nit):
        return False

    if len(nit) != 10:
        return False

    mult = [41, 37, 29, 23, 19, 17, 13, 7, 3]  # multiplicadores
    v = sum(list(map(lambda x, y: x * y, mult, [int(c) for c in nit[:-1]])))
    v = int(v) % 11

    if v >= 2:
        v = 11 - v

    return str(v) == nit[9]


class EnterpriseApi(APIView):
    def get(self, request, format=None):
        try:
            enterprises = Enterprise.objects.filter(active=True)
            enterprises_serializers = EnterpriseSerializer(enterprises, many=True)
            response = {
                'content': enterprises_serializers.data,
                'isOk': True,
                'message': '',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            name = request.data.get('name')
            nit = request.data.get('nit')
            address = request.data.get('address')
            phone = request.data.get('phone')

            nit_is_valid = validate_nit(nit)

            enterprise = Enterprise.objects.create(name=name, nit=nit, address=address, phone=phone)
            enterprise_serializer = EnterpriseSerializer(enterprise, many=False)

            response = {
                'content': enterprise_serializer.data,
                'isOk': True,
                'message': 'Empresa creada',
            }
            return Response(response, status=status.HTTP_200_OK)
        except IntegrityError:
            response = {
                'content': [],
                'isOk': False,
                'message': 'NIT ya registrado',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)

    def put(self, request, id=None, format=None):
        try:
            name = request.data.get('name')
            nit = request.data.get('nit')
            address = request.data.get('address')
            phone = request.data.get('phone')

            enterprise = Enterprise.objects.get(id=id)

            enterprise.name = name if name is not None else enterprise.name
            enterprise.nit = nit if nit is not None else enterprise.nit
            enterprise.address = address if address is not None else enterprise.address
            enterprise.phone = phone if phone is not None else enterprise.phone
            enterprise.save()

            enterprise_serializer = EnterpriseSerializer(enterprise, many=False)
            response = {
                'content': enterprise_serializer.data,
                'isOk': True,
                'message': 'Empresa actualizada correctamente',
            }
            return Response(response, status=status.HTTP_200_OK)
        except IntegrityError:
            response = {
                'content': [],
                'isOk': False,
                'message': 'NIT ya registrado',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, id=None, format=None):
        try:

            enterprise = Enterprise.objects.get(id=id)
            enterprise.active = False
            enterprise.save()

            response = {
                'content': [],
                'isOk': True,
                'message': 'Empresa eliminada correctamente',
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = {
                'content': [],
                'isOk': False,
                'message': str(e),
            }
            return Response(response, status=status.HTTP_200_OK)
