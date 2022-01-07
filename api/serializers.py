from rest_framework import serializers
from django.contrib.auth.hashers import make_password, check_password
from .models import User
import secrets
import string

class UserSerializer(serializers.ModelSerializer):
	


	def validate(self, data):	
		"""
			*Se o campo senha for vazio, aplica a geração de senha aleatória de 4-20 caracteres
			*Aplica SHA256 na senha
		"""
		if data['password'] == '':				
			
			alphabet = string.ascii_letters + string.digits
			password = ''.join(secrets.choice(alphabet) for i in range(4,21))
			data['password']=password
			
		
		data['password']=make_password(data['password'])
		
		return data


	class Meta:
		model  = User
		fields = '__all__'
