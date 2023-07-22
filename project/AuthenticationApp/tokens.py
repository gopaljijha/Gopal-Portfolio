from django.contrib.auth.tokens import PasswordResetTokenGenerator

from six import text_type
from django.utils import six  

# class TokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self,user,timestamp):
#         return (
#         text_type(user.pk) + text_type(timestamp) 
#         # text_type(user.profile.signup_confirmation)
#         )

# generate_token = TokenGenerator()


from django.contrib.auth.tokens import PasswordResetTokenGenerator  
from django.utils import six  
class TokenGen(PasswordResetTokenGenerator):  
    def _make_hash_value(self, user, timestamp):  
        return (  
            six.text_type(user.pk) + six.text_type(timestamp) +  
            six.text_type(user.is_active)  
        )  
account_activation_token = TokenGen()  