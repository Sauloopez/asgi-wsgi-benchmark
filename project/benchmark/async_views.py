from asgiref.sync import sync_to_async
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from django.contrib.auth.models import User

class AsyncViews(View):

    async def get(self, request: HttpRequest, *args, **kwargs):
        user_fields = 'username', 'first_name', 'date_joined', 'email', 'is_staff', 'is_superuser'
        users = await sync_to_async(iter)(User.objects.only(*user_fields).all())
        return await sync_to_async(render)(request, 'list_users.html', context={'users': users, 'fields': user_fields})
    pass
