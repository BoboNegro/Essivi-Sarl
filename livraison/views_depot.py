from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from api import settings
from .serializer import DepotSerializer
from rest_framework import status, permissions, authentication
import uuid


DB = settings.db

class DepotController(APIView):

    @api_view(['GET'])
    #@authentication_classes([authentication.SessionAuthentication])
    #@permission_classes([permissions.AllowAny])
    def api_view_get_all(request):

        if request.method != 'GET':
            return Response({'error': 'Méthode non autorisée'}, status=405)

        try:
            query = DB.child("Depot").get()
            if query:
                data = query.val()
                depots = [data[i] for i in data]

                return Response({'Depot': depots})
            else:
                return Response({'error': 'Aucun depot trouvé avec ce code'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @api_view(['GET'])
    def api_view_get_code(request, code):
        if request.method != 'GET':
            return Response({'error': 'Méthode non autorisée'}, status=405)

        if not code:
            return Response({'error': 'Code manquant'}, status=400)

        try:
            query = DB.child("Depot").order_by_child("code").equal_to(code).get()
            if query:
                data = query.val()
                depot = [data[i] for i in data]

                return Response({'Depôts': depot})
            else:
                return Response({'error': 'Aucun depôt trouvé avec ce code'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @api_view(['POST'])
    def api_view_post(request):
        serializer = DepotSerializer(data=request.data)
        if serializer.is_valid():
            try:
                
                # La clé n'est plus générée, La clé de chaque donnée enregistrée est le code
                DB.child("Depot").push(serializer.data)
                return Response(serializer.data)
            except Exception as e:
                return Response({'details': f'An error occurred while saving data to the database: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['PUT'])
    def api_view_put(request, code):

        serializer = DepotSerializer(data=request.data)
        if serializer.is_valid():
            try:
                DB.child("Depot").child(code).update(serializer.data)
                # db.child("Depots").push(serializer.data)
                return Response(serializer.data)
            except Exception as e:
                return Response({'details': f'An error occurred while saving data to the database: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





