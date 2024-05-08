import asyncio

import aiohttp

BASE_URL = "https://dummyjson.com/products"


async def async_get_requests():
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL) as response:
            return await response.json()


async def main():
    response = await async_get_requests()
    print(response)


asyncio.run(main())
