from django.http import HttpResponse
import asyncio
from time import sleep
import httpx

async def index(request):
    return HttpResponse("Hello async Django")

