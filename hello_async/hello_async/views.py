from django.http import HttpResponse
import asyncio
from time import sleep
import httpx 
from typing import List
import random

# helpers

async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)

async def get_smokables():
    print("Getting smokeables...")
    await asyncio.sleep(2)
    async with httpx.AsyncClient() as client:
        await client.get("https://httpbin.org/")
        print(client)

        print("Returing smokeables")
        return [
            "ribs",
            "brisket",
            "lemon chicken",
            "salmon",
            "bison sirloin",
            "sausage",
        ]

async def get_flavor():
    print("Getting flavour...")

    await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        await client.get("https://httpbin.org/")

    print ("Returing flavour")
    return random.choice(
        [
            "Sweet Baby Ray's",
            "Stubb's Original",
            "Famous Dave's",
        
        ]
    )

# views

async def index(request):
    return HttpResponse("Hello, async Django!")


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")

async def smoke(smokables:List[str]=None, flavour:str= "Sweet Baby Ray's")->List[str]:
    """ Smokes some meats and applies the Sweet Baby Ray's """
    for smokable in smokables:
        print(f"Smoking some {smokable}...")
        print(f"Applying the {flavour}...")
        print(f"{smokable.capitalize()} smoked")
    return len(smokables)    


def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")

async def smoke_some_meats(request):
    results = await asyncio.gather(*[get_smokables(), get_flavor()])
    total = await asyncio.gather(*[smoke(results[0], results[1])])
    return HttpResponse(f"Smoked {total[0]} meats with {results[1]}!")