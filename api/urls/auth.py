from api.views.auth.login import login_api
from api.views.auth.register import new_user
from api.views.auth.logout import logout_api
from django.urls import path


urlpatterns = [
    path('login/', login_api, name='login'),
    path('register/', new_user, name='new_user'),
    path('logout/', logout_api, name='logout'),

]