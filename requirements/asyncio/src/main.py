#!/bin/python3
import requests

import asyncio
import aiohttp
import time

ps_url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"

ps_headers = {
	"accept" : "application/json"
}

def	get_ps_data():
	res = requests.get(ps_url, headers=ps_headers)
	res.json()
	print(res)

async def	asyncio_get_ps_data(session: aiohttp.ClientSession):
	async with session.get(ps_url, headers=ps_headers) as res:
		print(res.status)
		await res.json()

def main() -> None:
	now = time.perf_counter()
	get_ps_data()
	get_ps_data()
	get_ps_data()
	print(f"ELAPSED TIME = {time.perf_counter() - now}")

async def asyncio_main() -> None:
	now = time.perf_counter()
	async with aiohttp.ClientSession() as session:
		tasks = [asyncio_get_ps_data(session) for _ in range(3)]
		await asyncio.gather(*tasks)
	print(f"ELAPSED TIME = {time.perf_counter() - now}")

if __name__ == "__main__":
	asyncio.run(asyncio_main())
	main()

