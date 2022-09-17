from ninja import Schema

class AccountIn(Schema):# wanted by SginUp
    name:str
    phone: str
    password1: str
    password2: str

class AothorizationOut(Schema): #Given By SignUp
    detail: str
    
class SignIn(Schema): #Wanted by SginIn
    phone: str
    password: str
    
class AccountOut(Schema): #given by SginIn
    detail: str
    id: int
    token: str
    name:str
    phone: str
    
