from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api import settings
from .serializer import ProduitSerializer
from rest_framework import status, permissions, authentication

DB = settings.db

class ProduitController(APIView):

    @api_view(['GET'])
    def api_view_get_all(request):

        if request.method != 'GET':
            return Response({'error': 'Méthode non autorisée'}, status=405)

        try:
            query = DB.child("produit").get()
            if query:
                data = query.val()
                produits = [data[i] for i in data]

                return Response({'Produits': produits})
            else:
                return Response({'error': 'Aucun Produit trouvé avec ce code'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @api_view(['GET'])
    def api_view_get_code(request, code):
        if request.method != 'GET':
            return Response({'error': 'Méthode non autorisée'}, status=405)

        if not code:
            return Response({'error': 'Code manquant'}, status=400)

        try:
            query = DB.child("produit").order_by_child("code").equal_to(code).get()
            if query:
                data = query.val()
                produit = [data[i] for i in data]

                return Response({'Produits': produit})
            else:
                return Response({'error': 'Aucun depôt trouvé avec ce code'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @api_view(['POST'])
    def api_view_post(request):
        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid():
            try:
                
                # La clé n'est plus générée, La clé de chaque donnée enregistrée est le code
                DB.child("produit").push(serializer.data)
                return Response(serializer.data)
            except Exception as e:
                return Response({'details': f'An error occurred while saving data to the database: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['PUT'])
    def api_view_put(request, code):

        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid():
            try:
                DB.child("produit").child(code).update(serializer.data)
                return Response(serializer.data)
            except Exception as e:
                return Response({'details': f'An error occurred while saving data to the database: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






