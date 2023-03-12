from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from api import settings
from .serializer import MarqueSerializer
from rest_framework import status
DB = settings.db

class MarqueController(APIView):

    @api_view(['GET'])
    def api_view_get_all(request):

        if request.method != 'GET':
            return Response({'error': 'Méthode non autorisée'}, status=405)

        try:
            query = DB.child("Marque").get()
            if query:
                data = query.val()
                Marques = [data[i] for i in data]

                return Response({'Marque': Marques})
            else:
                return Response({'error': 'Aucun Marque trouvé avec ce code'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @api_view(['GET'])
    def api_view_get_code(request, code):
        if request.method != 'GET':
            return Response({'error': 'Méthode non autorisée'}, status=405)

        if not code:
            return Response({'error': 'Code manquant'}, status=400)

        try:
            query = DB.child("Marque").order_by_child("code").equal_to(code).get()
            if query:
                data = query.val()
                Marque = [data[i] for i in data]

                return Response({'Depôts': Marque})
            else:
                return Response({'error': 'Aucun depôt trouvé avec ce code'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @api_view(['POST'])
    def api_view_post(request):
        serializer = MarqueSerializer(data=request.data)
        if serializer.is_valid():
            try:
                
                # La clé n'est plus générée, La clé de chaque donnée enregistrée est le code
                DB.child("Marque").push(serializer.data)
                return Response(serializer.data)
            except Exception as e:
                return Response({'details': f'An error occurred while saving data to the database: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['PUT'])
    def api_view_put(request, code):

        serializer = MarqueSerializer(data=request.data)
        if serializer.is_valid():
            try:
                DB.child("Marque").child(code).update(serializer.data)
                # db.child("Marques").push(serializer.data)
                return Response(serializer.data)
            except Exception as e:
                return Response({'details': f'An error occurred while saving data to the database: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






