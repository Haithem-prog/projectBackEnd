from ast import List, Str
from hashlib import new
from ninja import Router
from django.contrib.auth import get_user_model
from backend.schemas import ErrorMesssage
from custom_user.models import CustomUser
from custom_user.schema import AccountIn, AccountOut, AothorizationOut
from custom_user.schema import SignIn
from custom_user.authorization import create_token_for_user

authorization_router = Router(tags=['authorization'])
User = get_user_model()


@authorization_router.post('signup', auth=None, response={200: AothorizationOut, 201: ErrorMesssage})
def signup(request, account_in: AccountIn):
    if str(User.objects.filter(phone=account_in.phone)) != "<QuerySet []>":
        return 201, {'detail': 'Account Already Exists'}
    if account_in.password1 != account_in.password2:
        return 201, {'detail': 'Passwords should look alike'}
    User.objects.create_user(
        name=account_in.name,
        phone=account_in.phone,
        password=account_in.password1
    )
    return 200, {
        'detail': 'Registered Successfully'
    }


@authorization_router.post('signin', auth=None, response={200: AccountOut, 201: ErrorMesssage})
def signin(request, signin_in: SignIn):
    try: 
        user = User.objects.get(phone=signin_in.phone)
        print(user)
        if user.check_password(signin_in.password):
            token = create_token_for_user(user)
            return 200, {
                'detail': 'logged in Successfully',
                'id': user.id,
                'token': token,
                'name': user.name,
                'phone': user.phone,
            }
        else:
            return 201, {'detail': 'Incorrect Password'}
    except:
        return 201, {'detail': 'No Account With This Number'}

# from ninja import Router
# from django.contrib.auth import get_user_model
# from custom_user.schema import AccountIn
# from custom_user.schema import SignIn
# from custom_user.authorization import create_token_for_user

# authorization_router = Router(tags=['authorization'])
# User = get_user_model()


# @authorization_router.post('Signup',auth=None)
# def signup(request, account_in: AccountIn):
#     if account_in.password1 != account_in.password2:
#         return 400, {'detail': 'Passwords should look alike'}

#     try:
#         User.objects.get(phone=account_in.phone)
#     except:
#         new_user = User.objects.create_user(
#             name=account_in.name,
#             phone = account_in.phone,
#             password=account_in.password1
#         )

#         token = create_token_for_user(new_user)

#         return {
#                 'token': token,
#                 'account': {
#                     'name':new_user.name,
#                     'phone': new_user.phone,
#                     'user_id':new_user.id
#                     }
#             }

#     return 404, {'detail':'there was an error'}



# @authorization_router.post('signin',auth=None)
# def signin(request, signin_in: SignIn):
#     try:
#         user = User.objects.get(phone=signin_in.phone)
#     except User.DoesNotExist:
#         user = None

#     else:
#         if user.check_password(signin_in.password):
#             token = create_token_for_user(user)
#             return {
#                 'token': token,
#                 'UserAccount': {
#                     'name':user.name,
#                     'phone': user.phone,
#                     'user_id': user.id
#                     }
#             }

#     if not user:
#         return 404, {'detail':'there was an error'}


 