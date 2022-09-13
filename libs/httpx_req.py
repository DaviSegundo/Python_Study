import time
import httpx
import asyncio

base_url = "https://pokeapi.co/api/v2/pokemon"


def normal_request():
    with httpx.Client() as client:
        pokemons = []
        for idx in range(1, 100):
            response = client.get(f"{base_url}/{idx}")
            body = response.json()
            name = body.get("name")
            pokemons.append(name)

        return pokemons


async def get_pokemon(client, url):
    resp = await client.get(url)
    return resp.json()["name"]


async def async_request():
    async with httpx.AsyncClient() as client:
        tasks = []
        for idx in range(1, 100):
            url = f"{base_url}/{idx}"
            tasks.append(asyncio.create_task(get_pokemon(client, url)))

        pokemons = await asyncio.gather(*tasks)
        return pokemons


if __name__ == "__main__":
    start_time = time.time()
    pokemons = normal_request()
    print(f"Normal Requests: {time.time() - start_time} seconds")

    start_time = time.time()
    pokemons = asyncio.run(async_request())
    print(f"Async Requests: {time.time() - start_time} seconds")
