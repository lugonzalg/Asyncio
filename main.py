#!/bin/python3

import asyncio
import requests
import time

ps_url = "https://petstore.swagger.io/v2/pet/findByStatus?status=available"

ps_header = {
	"accept" : "application/json"
}

def	get_ps_data():
	res = requests.get(ps_url, headers=ps_header)
	print(res)

async def	asyncio_get_ps_data():
	res = requests.get(ps_url, headers=ps_header)
	print(res)

def main() -> None:
	#loop = asyncio.new_event_loop()
	now = time.time()
	get_ps_data()
	get_ps_data()
	get_ps_data()
	print(f"ELAPSED TIME = {time.time() - now}")

async def asyncio_main() -> None:
	#loop = asyncio.new_event_loop()
	now = time.time()
	await asyncio.gather(
		asyncio_get_ps_data(),
		asyncio_get_ps_data(),
		asyncio_get_ps_data()
	)
	print(f"ELAPSED TIME = {time.time() - now}")

if __name__ == "__main__":
	asyncio.run(asyncio_main())
	main()

