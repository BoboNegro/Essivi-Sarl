from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from api import settings
from .serializer import CommandeSerializer
from rest_framework import status, permissions, authentication
import uuid

# Create your views here.
# Ivan 91 12 09 24


DB = settings.db

class CommandeController(APIView):

    @api_view(['GET'])
    #@authentication_classes([authentication.SessionAuthentication])
    #@permission_classes([permissions.AllowAny])
    def api_view_get_all(request):

        if request.method != 'GET':
            return Response({'error': 'Méthode non autorisée'}, status=405)

        try:
            query = DB.child("Commande").get()
            if query:
                data = query.val()
                Commandes = [data[i] for i in data]

                return Response({'Commande': Commandes})
            else:
                return Response({'error': 'Aucun Commande trouvé avec ce code'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @api_view(['GET'])
    def api_view_get_code(request, code):
        if request.method != 'GET':
            return Response({'error': 'Méthode non autorisée'}, status=405)

        if not code:
            return Response({'error': 'Code manquant'}, status=400)

        try:
            query = DB.child("Commande").order_by_child("code").equal_to(code).get()
            if query:
                data = query.val()
                Commande = [data[i] for i in data]

                return Response({'Depôts': Commande})
            else:
                return Response({'error': 'Aucun depôt trouvé avec ce code'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @api_view(['POST'])
    def api_view_post(request):
        serializer = CommandeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                
                # La clé n'est plus générée, La clé de chaque donnée enregistrée est le code
                DB.child("Commande").push(serializer.data)
                return Response(serializer.data)
            except Exception as e:
                return Response({'details': f'An error occurred while saving data to the database: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['PUT'])
    def api_view_put(request, code):

        serializer = CommandeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                DB.child("Commande").child(code).update(serializer.data)
                # db.child("Commandes").push(serializer.data)
                return Response(serializer.data)
            except Exception as e:
                return Response({'details': f'An error occurred while saving data to the database: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






