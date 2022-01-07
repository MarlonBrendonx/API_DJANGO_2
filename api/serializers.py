from rest_framework import serializers
from .models import User
import secrets
import string

class UserSerializer(serializers.ModelSerializer):
	


	def validate(self, data):	
		"""
			Se o campo senha for vazio, aplica a geração de senha aleatória de 4-20 caracteres
		"""
		if data['password'] == '':				
			
			alphabet = string.ascii_letters + string.digits
			password = ''.join(secrets.choice(alphabet) for i in range(4,21))
			data['password']=password
			
		return data


	class Meta:
		model  = User
		fields = '__all__'
