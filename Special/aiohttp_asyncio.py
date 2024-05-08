import asyncio

import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://httpbin.org/get") as response:
            print("Status:", response.status)
            print("Content-type:", response.headers["content-type"])

            data = await response.json()
            print("Data:", data)

            # html = await response.text()
            # print("Body:", html[:15], "...")


asyncio.run(main())
