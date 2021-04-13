# Вашей задачей будет создать сервер агрегатор (он выполнит несколько запросов на адреса сторонних сайтов).
# Количество сайтов и сами сайты на которые вы будете слать реквесты вы определяете сами (вот например по ссылке
# ниже найдете список популярных ресурсов, но, как правило, они требуют регистрации, после чего они предоставят вам
# что-то типа ключа с которым вы сможете запросить информацию)
#
# 1) Познакомиться с фреймворком AIOHTTP (https://docs.aiohttp.org/en/stable/).
#
# 2)Создать сервер который мог бы принимать GET запросы на адрес (http://localhost/collect_info)
#
# 3) В ответе должна быть агрегирована информация полученная от сторонних ресурсов.
#
#
#
import asyncio
from aiohttp import web, ClientSession
import time

url_list = [('https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/'
             '?query=Odessa',
             {'rapidapi-key': "3e06ab0b61msh85e2172b269c576p1fcbacjsnb1ca9382d5e6"}
             ),
            ('https://weatherbit-v1-mashape.p.rapidapi.com/current?lon=30.73&lat=46.46',
             {'rapidapi-key': "3e06ab0b61msh85e2172b269c576p1fcbacjsnb1ca9382d5e6"}
            ),
            ('https://hotels4.p.rapidapi.com/locations/search?query=odessa&locale=en_US',
             {'rapidapi-key': "3e06ab0b61msh85e2172b269c576p1fcbacjsnb1ca9382d5e6"}
            )
           ]


async def fetch(session, url, params):
    async with session.get(url, params=params) as response:
        return await response.json()


async def fetch_all(url_list, loop):
    async with ClientSession(loop=loop) as session:
        results = await asyncio.gather(*[fetch(session, url, params) for url, params in url_list])
        return results


async def index_view(request):
    return web.Response(text='This is an index page.')


async def collect_info_view(request):
    text = str(data)
    return web.Response(text=text)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(fetch_all(url_list, loop))
    my_server = web.Application()
    my_server.add_routes([web.get('/', index_view)])
    my_server.add_routes([web.get('/collect_info', collect_info_view)])
    web.run_app(my_server)
