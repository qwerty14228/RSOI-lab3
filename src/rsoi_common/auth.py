from rest_framework import authentication


class RsoiUser:

    is_active = True
    is_authenticated = True

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class RsoiAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = request.headers.get('X-User-Name')
        if not username:
            return None

        user = RsoiUser(username=username)

        return (user, None)
