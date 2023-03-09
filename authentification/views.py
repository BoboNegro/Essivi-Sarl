from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from api import settings
from firebase_admin import auth
import firebase_admin
from rest_framework.permissions import IsAuthenticated
from firebase_admin import credentials
from .serializer import AuthSerializer, UtilisateurSerializer, UtilisateurSerializerGet
from rest_framework import status
import uuid
from .authentication import JWTTokenAuthentication
import jwt
import datetime

# Create your views here.
# Ivan 91 12 09 24


DB = settings.db
AUTH = settings.auth
cred = credentials.Certificate('C:/Users/fabri/Desktop/A.P.Y/backend/credentials.json')
firebase_admin.initialize_app(cred)

class UtilisateursControllers(APIView):

    @api_view(['GET'])
    @authentication_classes([JWTTokenAuthentication])
    @permission_classes([IsAuthenticated])
    def api_view_get_all(request):

        if request.method != 'GET':
            return Response({'errors': 'Méthode non autorisée'}, status=405)

        try:
            query = DB.child("Utilisateurs").get()
            if query:
                data = query.val()
                users = []
                for key in data:
                    users.append(data[key])
                return Response({'utilisateurs': users})
            else:
                return Response({'error': 'Aucun utilisateur trouvé avec ce code'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)

    @api_view(['GET'])
    def api_view_get_code(request, code):
        if request.method != 'GET':
            return Response({'error': 'Méthode non autorisée'}, status=405)

        if not code:
            return Response({'error': 'Code manquant'}, status=400)

        try:
            query = DB.child("Utilisateurs").order_by_child("code").equal_to(code).get()
            if query:
                data = query.val()
                users = [data[i] for i in data]

                return Response({'utilisateurs': users})
            else:
                return Response({'error': 'Aucun utilisateur trouvé avec ce code'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


    @api_view(['GET'])
    def api_view_get_email(request, email):
        if request.method != 'GET':
            return Response({'error': 'Méthode non autorisée'}, status=405)

        if not email:
            return Response({'error': 'Mail manquant'}, status=400)

        try:
            query = DB.child("Utilisateurs").order_by_child("email").equal_to(email).get()
            if query:
                data = query.val()
                users = [data[i] for i in data]

                return Response({'currentUser': users[0]})
            else:
                return Response({'error': 'Aucun utilisateur trouvé avec cet mail'}, status=404)
        except Exception as e:
            return Response({'error': str(e)}, status=500)


    @api_view(['POST'])
    def api_view_post(request):
        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            try:
                new_user = auth.create_user(
                    email=serializer.data['email'],
                    email_verified=False,
                    password=serializer.data['password'],
                    phone_number=serializer.data['phone_number'],
                    display_name=serializer.data['username'],
                    disabled=False)
                # La clé n'est plus générée, La clé de chaque donnée enregistrée est le code
                serializer.data['code'] = uuid.uuid4()
                DB.child("Utilisateurs").push(serializer.data)
                return Response(serializer.data)
            except Exception as e:
                return Response({'details': f'An error occurred while saving data to the database: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['POST'])
    def api_view_post_login(request):
        serializer = AuthSerializer(data=request.data)
        serializerGet = UtilisateurSerializerGet(data=request.data)
        if serializer.is_valid():
            try:
                email = serializer.data['email']
                password = serializer.data['password']
                userf = DB.child("Utilisateurs").order_by_child("email").equal_to(email).get()
                data = userf.val()
                var = [data[i] for i in data]
                password = var[0]['password']
                user =  user = auth.get_user_by_email(email)
                if user and password == serializer.data['password']:
                  
                  secret_key = settings.SECRET_KEY
                    # Définir la date d'expiration du token
                  expires_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=3000)

                    # Créer le token JWT
                  token = jwt.encode({'user': var[0], 'exp': expires_at}, secret_key, algorithm='HS256')
                  reponse = {'token': token, 'data': var[0]}
                  return Response(reponse)
                else :
                     return Response({'details': f'The user don''t in the database: {str(e)}'},
                                status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'details': f': {str(e)}'},
                                status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @api_view(['PUT'])
    def api_view_put(request, code):

        serializer = UtilisateurSerializer(data=request.data)
        if serializer.is_valid():
            try:
                DB.child("Utilisateur").child(code).update(serializer.data)
                # db.child("Utilisateurs").push(serializer.data)
                return Response(serializer.data)
            except Exception as e:
                return Response({'details': f'An error occurred while saving data to the database: {str(e)}'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






