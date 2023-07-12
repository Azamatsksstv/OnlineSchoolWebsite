from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, VerifyAccountSerializer
from accounts.emails import send_otp_via_email


class RegisterAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message': 'Registration successfully check email',
                    'data': serializer.data,
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)


class VerifyOTP(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyAccountSerializer(data=data)

            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']

                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': 'invalid email'
                    })

                if user[0].otp != otp:
                    return Response({
                        'status': 400,
                        'message': 'Something went wrong',
                        'data': 'wrong otp'
                    })
                user = user.first()
                user.is_verified = True
                user.save()

                return Response({
                    'status': 200,
                    'message': 'account verified',
                    'data': {},
                })

        except Exception as e:
            print(e)