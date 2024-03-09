from rest_framework.routers import SimpleRouter
from restapi.views import BookOperations

simplerouter = SimpleRouter()
simplerouter.register('book/v1/',BookOperations)
urlpatterns = simplerouter.urls

#http://localhost:8000/api/book/v1   ----> GET ---->single
#http://localhost:8000/api/book/v1   ----> POST ---->Create
#http://localhost:8000/api/book/v1   ----> Delete ---->Delete and so on