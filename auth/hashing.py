from curses.ascii import CR
from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash:
    def bcrypt(password):
        return pwd_cxt.hash(password)
    
    def verify(plan_passwd, hash_passwd):
        return pwd_cxt.verify(plan_passwd,hash_passwd)