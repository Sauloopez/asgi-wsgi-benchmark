from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from django.contrib.auth.models import User
from django.views.i18n import JsonResponse

class SyncViews(View):

    def get(self, request: HttpRequest, *args, **kwargs):
        user_fields = 'username', 'first_name', 'date_joined', 'email', 'is_staff', 'is_superuser'
        users = User.objects.only(*user_fields).all()
        return render(request, 'list_users.html', context={'users': users, 'fields': user_fields})
    pass
