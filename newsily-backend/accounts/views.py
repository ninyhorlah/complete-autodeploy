from rest_framework.views import APIView
from rest_framework import status, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, UserLoginSerializer, UserRegistrationSerializer

from requests import Session
import json


User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()

        response = {
            'success' : 'True',
            'message' : 'User created successfully'
        }
        
        return Response(response, status=status.HTTP_201_CREATED)


class UserLoginView(generics.RetrieveAPIView):

    queryset = User.objects.all
    permissions_classes = (AllowAny, )
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        response = {
            'success' : 'True',
            'message' : 'User logged in successfully',
            'user' : serializer.validated_data['username'],
            'token' : serializer.validated_data['token']
        }

        return Response(response, status=status.HTTP_200_OK)
        

class AdminListUserView(generics.ListAPIView):

    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        user = User.objects.all()

        data = []
        
        for items in user:
            data.append({
                'id' : items.id,
                'username' : items.username,
                'email' : items.email
            })
        
        if data == []:
            response = {
                'success' : 'True',
                'message' : 'No user in the database'
            }
            return Response(response, status=status.HTTP_200_OK)
        
        return Response(data, status=status.HTTP_200_OK)



class SetCookiesRepubblica(APIView):

    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):

        s = Session()

        headers = {
            'authority': 'eulogin.repubblica.it',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': '*/*',
            'origin': 'https://quotidiano.repubblica.it',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://quotidiano.repubblica.it/edicola/funnel/login.jsp?service=repubblica.it&backurl=https^%^3A^%^2F^%^2Fwww.repubblica.it^%^2Fsocial^%^2Fsites^%^2Frepubblica^%^2Fnazionale^%^2Floader.php^%^3Fforward^%^3Dfalse^%^26origin^%^3DRIT_SLIM^%^26urlToken^%^3Drepnzfree^%^26mClose^%^3D2^%^26backUrl^%^3Dhttps^%^253A^%^2F^%^2Fwww.repubblica.it^%^2F&productId=all&origin=RIT_SLIM&cid=OLD&urlToken=repnzfree',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': 'kw_1pc_enableds=true; pw_vdW=0; wt_nv=1; wt_nv_s=1; gmid=gmid.ver4.AcbHae7tnA.Wi1sUdwdodQcN0YsYs-9-E3EmJS2e3pZA6b3QheHQOkvLTlCO1Zexc5csyOsDbkW._lwVudblO0TuWLWL69oLoy-3ZeNxEbenAAueRHOas_us19DIT5unvZjfm9aD6SgAhH6CHZlCkqz8QqS1rGfv7w.sc3; ucid=YP25G2X2LAaqpD75O2Djcw; hasGmid=ver4; gig_bootstrap_3_1LA7c1Tgh8TOu8RyhRNltE6n6Avs4pEXj5bhyQNpnpC3KHJ60mcdJ6xOubYt6iUJ=eulogin_ver4; wt_geid=68934a3e9455fa72420237eb; _iub_cs-23960187=^%^7B^%^22timestamp^%^22^%^3A^%^222021-03-18T11^%^3A50^%^3A55.119Z^%^22^%^2C^%^22version^%^22^%^3A^%^221.28.1^%^22^%^2C^%^22consent^%^22^%^3Atrue^%^2C^%^22id^%^22^%^3A23960187^%^7D; euconsent-v2=CPDQG4fPDQHI4B7D6BITBRCsAP_AAH_AAAAAHmNf_X__b39j-_59_9t0eY1f9_7_v-0zjhfds-8N2f_X_L8X42M7vF36pq4KuR4Eu3LBIQFlHOHUTUmw6okVrTPsak2Mr7NKJ7LEinMbe2dYGHtfn91TuZKYr_7s_9_z__-__v__79f_r-3_3_vp9X---_e_V399xLv9QPKAJMNS-AizEscCSaNKoUQIQriQ6AUAFFCMLRNYQMrgp2VwEeoIGACA1ARgRAgxBRiwCAAACAJKIgJADwQCIAiAQAAgBUgIQAETAILACwMAgAFANCxAigCECQgyOCo5TAgIkWignkrAEou9jDCEMosAKBR_RUYCJQggWAAA; kwdnt=0,1616068255280^#0x4793020563212875rtgh7734458267279519ne52gs; _fbp=fb.1.1616068255739.1890163849; __gads=ID=8db049a25be1c98e:T=1616068255:S=ALNI_MbzX_FITXU_t99nfybwCgMfT8PUdw; _ga=GA1.2.1201241989.1616068266; customerly_jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiIsImp0aSI6IjRkN2ZiMzAyLTg3ZTAtMTFlYi1hZDNmLTAyNDIwYTAwMDAwNCJ9.eyJpc3MiOiJodHRwczpcL1wvY3VzdG9tZXJseS5pbyIsImp0aSI6IjRkN2ZiMzAyLTg3ZTAtMTFlYi1hZDNmLTAyNDIwYTAwMDAwNCIsImlhdCI6MTYxNjA2ODMwMCwibmJmIjoxNjE2MDY4MzAwLCJleHAiOjI1OTM2ODQzMDAsInR5cGUiOjEsImFwcCI6ImEyMTVkZTAzIiwiaWQiOm51bGx9.O3e0pTVovNbJEGCAybjSHqH9gIChvcadVx_DGjtpDAo; customerly_welcome_message_visitors_seen=true; _gid=GA1.2.1600629729.1616177886; wt_mcp_optin=^%^7B^%^2235^%^22^%^3A^%^221^%^22^%^7D; cto_bundle=iu9PK18lMkIzQlFDMllYJTJGTkd4ZjBZWXpRR1JqYU1aeW9pUkhXWlcxQU02NWRmcHNSRXdmNE9QZHBobkpkTDJJNDJzQ01OTmtERUVpaWFFb1FsJTJCWFNLcmFKaHg4TGNQaEhKcEhwRDh4NyUyRkxwQVhiQkw1MTU3MkliUzg5b1JGemU1RFM5Z0h3U296SzhoYTkwemNwNTdIWDQzZjVIUSUzRCUzRA; wt_mcp_sid=1813837979; wt_cdbeid=1; _iub_cs-23960187-granular=^%^7B^%^22gac^%^22^%^3A^%^22MX4mAQMBAgEIAQUBBAEDAQwBBQEDAQ4BCAEEAQEBBgEDAgYCAgEBAQkBAgEEAQMBFAEDAQUBCAEGAQkBAQEIAQEBCwEFAQYBBQENAQQBEwEFAQQCAgIKARwBAwENAQMBBAECAQkBBQEBAQgBBQEFAQMBBAECAgMBHAEDAQQBAgIFAQEBAQEQAhABCQEIAgcBBQEBAQcBAgEDAcKNAQMBBwEiAQYBDgINAQICBwEJAQ0BCgECAQYBGAEEAREBCAEGASgBAQEDAREBFAECAQMBAQIFAQUBBAEBAQ0BEQEGAQIBAQEBAQcBEwEHAQcBBQECAQkBAwETAQEBAwEIAQICBQEDAQoCAgEVAQ8BAQEFAQcBAQEDAQoBBQEEARABDwEKAQcCCQEbAQcBAwICARQBAQEGAQUCCAEdARABAwEIAQ4BBwEGAQIBBQEFAQYBAQEDAgYBCwEMARUBDAEBAQsBAQEDAQUCAwEOAQEBAwEIAQMBBAICAQYBDAEEAQIBCwEDAQwBAwENAQcBAQEOAQEBBAEEAgEBAQIBAQ0BBgEDAQcBAQEIAQkBEQELAQwBAQERAwIDCAEYAQMBEwEHAQMBBAEBAgQBAwEHAQMBAQEBAQEBDQEBAQwBAwEBAQUBCAEFAQIBAwECAQQBAQECAQUBCQEKAQEBAwECAQ8BAgEKAQICAQECAQgBEgEKAQ4BAgEJAQYBBQEDAQIBAwEIAQIBAgECBAUBCgECAwYBAwEFAgkBBAEBAQUBAgEBAQEBAwECAQEBAQEDAQIBAQEMAQYBCwEBAgUBAwEEAQMBAgEBAQEBAwICBAEBCAIFAQgCBAEBAgYBAQEHAQoCAgMBAgIBAQEFAgQBBQIEAQICAgMBAQEBBgEGAgMCAQEFAgEDAgMDAwECBwICAQMBAwECAQECAgIDAQIBCAEFAg4BCQEbAgEDCwECAQMCBQECAQMBBgICAwICBAECAgIBAQEBAwMBAQIBBAEBAQEDAQECAQEBAQEBAwQBDAEBAQMBAgECBgIBBAEFAQMCAQEDAQEFBAQBAQIFAQQGAQEBAQIDAwMBAQEDAwEBAwEBAgEBAgEBAgUDBAQCCAECAgQDAgEDAgEBAgIDAQECAQEBAQEHCgICAwEBAQIDAQEBAgEBAgMGAgEBAwEBBAICAQUBAwMCAgMBAgIDAQQCBgEBBAEEAgIBAgsDAgIBAQEBAgICAwEBAQEBAQED^%^22^%^7D; wt_rla=253822047730481^%^2C20^%^2C1616219073986; FCCDCF=^[^[^\\^AKsRol_GIuDNJcYWu9cGp7n7F_hJzmY5XtQK9jSZ5tObdXALCzae8v7HKx6XgXr4KfAqilRbPzA4AD7qp15mlsJxQ24NBz7CU-1nVTH-F5iS9DpULLOgidgaaw-n6QptYvMbRzDnuWfpkxlEJcmSreXijlNJ67qhTg==^\\^^],null,^[^\\^^[^[^],^[^],^[^],^[^],null,null,true^]^\\^,1616220344849^]^]',
        }

        data = {
        'loginID': 'phemmylintry@gmail.com',
        'password': 'Faithmygf@1',
        'sessionExpiration': '0',
        'targetEnv': 'jssdk',
        'include': 'profile^%^2Cdata^%^2Cemails^%^2Csubscriptions^%^2Cpreferences^%^2C',
        'includeUserInfo': 'true',
        'loginMode': 'standard',
        'lang': 'it',
        'APIKey': '3_1LA7c1Tgh8TOu8RyhRNltE6n6Avs4pEXj5bhyQNpnpC3KHJ60mcdJ6xOubYt6iUJ',
        'cid': 'OLD',
        'source': 'showScreenSet',
        'sdk': 'js_latest',
        'authMode': 'cookie',
        'pageURL': 'https^%^3A^%^2F^%^2Fquotidiano.repubblica.it^%^2Fedicola^%^2Ffunnel^%^2Flogin.jsp^%^3Fservice^%^3Drepubblica.it^%^26backurl^%^3Dhttps^%^253A^%^252F^%^252Fwww.repubblica.it^%^252Fsocial^%^252Fsites^%^252Frepubblica^%^252Fnazionale^%^252Floader.php^%^253Fforward^%^253Dfalse^%^2526origin^%^253DRIT_SLIM^%^2526urlToken^%^253Drepnzfree^%^2526mClose^%^253D2^%^2526backUrl^%^253Dhttps^%^25253A^%^252F^%^252Fwww.repubblica.it^%^252F^%^26productId^%^3Dall^%^26origin^%^3DRIT_SLIM^%^26cid^%^3DOLD^%^26urlToken^%^3Drepnzfree',
        'sdkBuild': '11903',
        'format': 'json'
        }

        response = s.post('https://eulogin.repubblica.it/accounts.login', headers=headers, data=data)
        # print(response.cookies)
        
        json_response = response.json()

        data = {
            "session_token" : json_response,
        }

        return Response(data)