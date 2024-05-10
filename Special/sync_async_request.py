import asyncio

import aiohttp
import requests

BASE_URL = "https://dummyjson.com/products"


# Asynchronous function to make an HTTP GET request using aiohttp
async def async_get_requests():
    # Create a ClientSession for making HTTP requests asynchronously
    async with aiohttp.ClientSession() as session:
        # Use session.get to make an asynchronous GET request to BASE_URL
        async with session.get(BASE_URL) as response:
            # Return the JSON response after converting it from bytes to Python object
            return await response.json()


# Synchronous function to make an HTTP GET request using requests
def send_sync_request():
    # Make a synchronous GET request to BASE_URL using requests.get
    response = requests.get(BASE_URL)
    # Return the response object JSON format
    return response.json()


# Asynchronous main function to execute the asynchronous request and print the response
async def main():
    # Await the asynchronous GET request and store the response
    response = await async_get_requests()
    # Print the response
    print(response)


# Run the asynchronous event loop with the main coroutine
asyncio.run(main())

# Print the synchronous request function (this will not execute the request)
print(send_sync_request())
