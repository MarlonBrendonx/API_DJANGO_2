2-API_DJANGO_2

Na segunda implementação da API, foi realizado a construção das rotas e métodos manualmente. Dessa forma, temos
as seguintes rotas:

GET  	localhost:8000/api/user-list/ 		  -> Obter lista de todos os usuários
GET  	localhost:8000/api/user-detail/<str:pk>/  -> Obter detalhes de um específico usuário (id)
POST 	localhost:8000/api/user-create/		  -> Cadastrar usuário
PUT  	localhost:8000/api/user-update/<str:pk>/  -> Atualizar específico usuário (id)
DELETE  localhost:8000/api/user-delete/<str:pk>/  -> Remover específico usuário (id)
GET  	localhost:8000/api/users-export/	  -> Exportar todos usuários em xls

