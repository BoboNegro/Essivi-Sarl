from rest_framework.authentication import BaseAuthentication, get_authorization_header, TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings
from typing import Tuple
from .models import Utilisateur


class JWTTokenAuthentication(BaseAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        auth_header = get_authorization_header(request).split()
        if not auth_header or auth_header[0].lower() != self.keyword.lower().encode():
            return None
        if len(auth_header) == 1:
            raise AuthenticationFailed('Invalid token header. No credentials provided.')
        elif len(auth_header) > 2:
            raise AuthenticationFailed('Invalid token header. Token string should not contain spaces.')
        try:
            token = auth_header[1].decode()
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            print(decoded_token)
            user = decoded_token.get('user')
            if user is None:
                raise AuthenticationFailed('Invalid token. User not found.')
            return user, token
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token signature has expired.')
        except jwt.DecodeError:
            raise AuthenticationFailed('Invalid token signature.')
        except Utilisateur.DoesNotExist:
            raise AuthenticationFailed('User not found.')
        except Exception as e:
            raise AuthenticationFailed('Unable to verify token: {}'.format(str(e)))



class CustomIsAuthenticated():
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.data)
