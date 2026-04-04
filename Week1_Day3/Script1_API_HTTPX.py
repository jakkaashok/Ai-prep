import requests
import httpx
import asyncio

#calling API and print Json
response = requests.get("https://api.github.com")
print(response.json())

#Async code to call multiple API's
urls = ["https://api.github.com","https://httpbin.org/get"]

async def fetch(url):
    async with httpx.AsyncClient() as client:
        return await client.get(url)


async def main():
    response = await asyncio.gather(*(fetch(url) for url in urls))
    for r in response:
        print(r.status_code)

asyncio.run(main())