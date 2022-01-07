from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
import datetime
import xlwt


def showTest(request):
	return JsonResponse("ok",safe=False)
	
	
@api_view(['GET'])
def listUser(request):
	users = User.objects.all()	
	serializer = UserSerializer(users, many=True)
	
	return Response({'status':status.HTTP_200_OK, 'data':serializer.data})
	
	
@api_view(['GET'])
def detailUser(request, pk):
	
	try:
	
		user = User.objects.get(id=pk)
		serializer = UserSerializer(user, many=False )
		
	except:
	
		return Response({'status':status.HTTP_404_NOT_FOUND, 'msg':'Não foi possível encontrar o usuário.' })	
		
		
	return Response({'status':status.HTTP_200_OK, 'data':serializer.data})

	
@api_view(['POST'])
def userCreate(request):
	
	serializer = UserSerializer(data=request.data)
	
	if serializer.is_valid(raise_exception=True):
		serializer.save()
				
		
	return Response({'status':status.HTTP_201_CREATED, 'data': serializer.data})
	
	
@api_view(['PUT'])
def userUpdate(request, pk):

	try:
	
		user = User.objects.get(id=pk)
		serializer = UserSerializer(instance=user, data=request.data)
		
		if serializer.is_valid():
			serializer.save()
	
	except:
		
		return Response({ 'status':status.HTTP_202_ACCEPTED, 'msg': "Não foi possível atualizar o usuário." }) 
	
	
	return Response({ 'status':status.HTTP_200_OK, 
	'msg': "Usuário atualizado com sucesso !", 'data': serializer.data }) 
	

@api_view(['DELETE'])
def userDelete(request, pk):
	
	try:

		user = User.objects.get(id=pk)
		user.delete()
	
	except:
	
		return Response({ 'status':status.HTTP_202_ACCEPTED, 'msg': "Não foi possível remover o usuário." }) 	
		
	
	return Response({ 'status':status.HTTP_200_OK, 'msg': "Usuário removido com sucesso !" })



def exportUsersxls(request):
	
	response=HttpResponse(content_type='application/ms-excel')
	response['Content-Disposition'] = 'attachment; filename=Usuários' + \
	str(datetime.datetime.now())+ '.xls'
	
	wb= xlwt.Workbook(encoding='utf-8')
	ws=wb.add_sheet('Usuarios')
	
	row_num=0  
	font_style=xlwt.XFStyle()
	font_style.font.bold=True
	
	columns=['Nome']
	
	for cols in  range( len(columns) ):
		ws.write(row_num, cols, columns[cols], font_style)		


	font_style=xlwt.XFStyle()
	
	rows=User.objects.values_list('login')
	
	for row in rows:
		row_num +=1
		
		for cols in range( len(row) ):
			ws.write(row_num, cols, str(row[cols]), font_style)
	
	
	wb.save(response)
	
	
	return response
	
	



