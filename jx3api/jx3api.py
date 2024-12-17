import json
import logging
import os
from contextlib import closing
from http import HTTPStatus
from typing import Any, Callable
from urllib.parse import urljoin
from urllib.request import Request, urlopen

import aiohttp

from .exception import APIError

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s][%(module)s:%(funcName)s:%(lineno)d]: %(message)s",
)


class JX3API:
    def __init__(
        self, *, token=None, ticket=None, base_url="https://www.jx3api.com"
    ):
        self.token = token or os.getenv("JX3API_TOKEN")
        self.ticket = ticket or os.getenv("JX3API_TICKET")

        self.base_url = base_url

        if not self.token:
            logging.warning(
                "The `token` parameter is not specified, only the free API can be used."
            )

    def request(self, *, endpoint: str, **kwargs):
        logging.debug(f"requesting: {endpoint=}, {kwargs=}")

        kwargs["ticket"] = self.ticket

        req = Request(
            urljoin(base=self.base_url, url=endpoint),
            data=json.dumps(kwargs).encode(encoding="utf-8"),
            headers={"token": token} if (token := self.token) else {},
        )

        with closing(urlopen(req)) as resp:
            if (data := json.loads(resp.read()))["code"] != HTTPStatus.OK:
                raise APIError(code=data["code"], msg=data["msg"])

        return data["data"]

    @staticmethod
    def require_token(func: Callable[..., Any]):
        def decorator(self, *args, **kwargs):
            if not self.token:
                raise ValueError(
                    "The `token` parameter is not specified, only the free API can be used."
                )

            return func(self, *args, **kwargs)

        return decorator

    @staticmethod
    def require_ticket(func: Callable[..., Any]):
        def decorator(self, *args, **kwargs):
            if not self.ticket:
                raise ValueError("The `ticket` parameter must be specified.")

            return func(self, *args, **kwargs)

        return decorator

    def active_calendar(self, *, server=None, num=0):
        return self.request(endpoint="/data/active/calendar", server=server, num=num)

    def active_celebs(self, *, name):
        return self.request(endpoint="/data/active/celebs", name=name)

    def active_list_calendar(self, *, num=15):
        return self.request(endpoint="/data/active/list/calendar", num=num)

    def home_furniture(self, *, name):
        return self.request(endpoint="/data/home/furniture", name=name)

    def home_travel(self, *, name):
        return self.request(endpoint="/data/home/travel", name=name)

    def news_allnews(self, *, limit=10):
        return self.request(endpoint="/data/news/allnews", limit=limit)

    def news_announce(self, *, limit=10):
        return self.request(endpoint="/data/news/announce", limit=limit)

    def server_master(self, *, name):
        return self.request(endpoint="/data/server/master", name=name)

    def server_check(self, *, server=None):
        return self.request(endpoint="/data/server/check", server=server)

    def server_status(self, *, server):
        return self.request(endpoint="/data/server/status", server=server)

    def home_flower(self, *, server, name, map):
        return self.request(
            endpoint="/data/home/flower", server=server, name=name, map=map
        )

    ##########
    # VIP  I #
    ##########

    @require_token
    @require_ticket
    def save_detailed(self, *, server, roleid):
        return self.request(
            endpoint="/data/save/detailed", server=server, roleid=roleid
        )

    @require_token
    @require_ticket
    def role_detailed(self, *, server, name):
        return self.request(endpoint="/data/role/detailed", server=server, name=name)

    @require_token
    def school_matrix(self, *, name):
        return self.request(endpoint="/data/school/matrix", name=name)

    @require_token
    def school_force(self, *, name):
        return self.request(endpoint="/data/school/force", name=name)

    @require_token
    def school_skills(self, *, name):
        return self.request(endpoint="/data/school/skills", name=name)

    @require_token
    def tieba_random(self, *, class_, server="-", limit=10):
        return self.request(
            endpoint="/data/tieba/random", class_=class_, server=server, limit=limit
        )

    @require_token
    @require_ticket
    def role_attribute(self, server, name):
        return self.request(endpoint="/data/role/attribute", server=server, name=name)

    @require_token
    @require_ticket
    def role_team_cd_list(self, *, server, name):
        return self.request(endpoint="/data/role/teamCdList", server=server, name=name)

    @require_token
    @require_ticket
    def luck_adventure(self, *, server, name):
        return self.request(endpoint="/data/luck/adventure", server=server, name=name)

    @require_token
    def luck_statistical(self, *, server, name, limit=20):
        return self.request(
            endpoint="/data/luck/statistical", server=server, name=name, limit=limit
        )

    @require_token
    def luck_server_statistical(self, *, name, limit=10):
        return self.request(
            endpoint="/data/luck/server/statistical", name=name, limit=limit
        )

    @require_token
    def luck_collect(self, *, server, num=7):
        return self.request(endpoint="/data/luck/collect", server=server, num=num)

    @require_token
    @require_ticket
    def role_achievement(self, *, server, role, name):
        return self.request(
            endpoint="/data/role/achievement", server=server, role=role, name=name
        )

    @require_token
    @require_ticket
    def arena_recent(self, *, server, name, mode=None):
        return self.request(
            endpoint="/data/arena/recent", server=server, name=name, mode=mode
        )

    @require_token
    @require_ticket
    def arena_awesome(self, *, mode=33, limit=20):
        return self.request(endpoint="/data/arena/awesome", mode=mode, limit=limit)

    @require_token
    @require_ticket
    def arena_schools(self, *, mode=33):
        return self.request(endpoint="/data/arena/schools", mode=mode)

    @require_token
    def member_recruit(self, *, server, keyword=None, table=1):
        return self.request(
            endpoint="/data/member/recruit", server=server, keyword=keyword, table=table
        )

    @require_token
    def member_teacher(self, *, server, keyword=None):
        return self.request(
            endpoint="/data/member/teacher", server=server, keyword=keyword
        )

    @require_token
    def member_student(self, *, server, keyword=None):
        return self.request(
            endpoint="/data/member/student", server=server, keyword=keyword
        )

    @require_token
    def server_sand(self, *, server):
        return self.request(endpoint="/data/server/sand", server=server)

    @require_token
    def server_event(self, *, name=None, limit):
        return self.request(endpoint="/data/server/event", name=name, limit=limit)

    @require_token
    def table_records(self, *, name):
        return self.request(endpoint="/data/table/records", name=name)

    @require_token
    def trade_demon(self, *, server=None, limit=10):
        return self.request(endpoint="/data/trade/demon", server=server, limit=limit)

    @require_token
    def trade_records(self, *, name, server=None):
        return self.request(endpoint="/data/trade/records", server=server, name=name)

    @require_token
    def tieba_item_records(self, *, server="-", name, limit=10):
        return self.request(
            endpoint="/data/tieba/item/records", server=server, name=name, limit=limit
        )

    @require_token
    def valuables_statistical(self, *, server, name, limit=20):
        return self.request(
            endpoint="/data/valuables/statistical",
            server=server,
            name=name,
            limit=limit,
        )

    @require_token
    def valuables_server_statistical(self, *, name, limit=10):
        return self.request(
            endpoint="/data/valuables/server/statistical", name=name, limit=limit
        )

    @require_token
    def server_antivice(self, *, server=None):
        return self.request(endpoint="/data/server/antivice", server=server)

    @require_token
    def rank_statistical(self, *, server, table, name):
        return self.request(
            endpoint="/data/rank/statistical", server=server, table=table, name=name
        )

    @require_token
    def rank_server_statistical(self, *, table, name):
        return self.request(
            endpoint="/data/rank/server/statistical", table=table, name=name
        )

    @require_token
    @require_ticket
    def school_rank_statistical(self, *, school="ALL", server="ALL"):
        return self.request(
            endpoint="/data/school/rank/statistical", school=school, server=server
        )

    @require_token
    def fraud_detailed(self, *, uid):
        return self.request(endpoint="/data/fraud/detailed", uid=uid)

    ##########
    # VIP II #
    ##########

    @require_token
    def active_monster(self):
        return self.request(endpoint="/data/active/monster")

    @require_token
    def horse_records(self, *, server):
        return self.request(endpoint="/data/horse/records", server=server)

    @require_token
    def horse_ranch(self, *, server):
        return self.request(endpoint="/data/horse/ranch", server=server)

    def fireworks_records(self, *, server, name):
        return self.request(
            endpoint="/data/fireworks/records", server=server, name=name
        )

    @require_token
    def fireworks_statistical(self, *, server, name, limit=20):
        return self.request(
            endpoint="/data/fireworks/statistical",
            server=server,
            name=name,
            limit=limit,
        )

    @require_token
    def fireworks_collect(self, *, server, num=7):
        return self.request(endpoint="/data/fireworks/collect", server=server, num=num)

    @require_token
    def fireworks_rank_statistical(self, *, server, column, this_time, that_time):
        return self.request(
            endpoint="/data/fireworks/rank/statistical",
            server=server,
            column=column,
            this_time=this_time,
            that_time=that_time,
        )

    @require_token
    def show_card(self, *, server, name):
        return self.request(endpoint="/data/show/card", server=server, name=name)

    @require_token
    def show_cache(self, *, server, name):
        return self.request(endpoint="/data/show/cache", server=server, name=name)

    @require_token
    def show_random(self, *, server, body=None, force=None):
        return self.request(
            endpoint="/data/show/random", server=server, body=body, force=force
        )

    #############
    #    VRF    #
    #############
    @require_token
    def mixed_chat(self, *, name, text):
        return self.request(endpoint="/data/mixed/chat", name=name, text=text)

    def music_tencent(self, *, name):
        return self.request(endpoint="/data/music/tencent", name=name)

    def music_netease(self, *, name):
        return self.request(endpoint="/data/music/netease", name=name)

    def music_kugou(self, *, name):
        return self.request(endpoint="/data/music/kugou", name=name)

    def idiom_solitaire(self, *, name):
        return self.request(endpoint="/data/idiom/solitaire", name=name)

    def saohua_random(self):
        return self.request(endpoint="/data/saohua/random")

    def saohua_content(self):
        return self.request(endpoint="/data/saohua/content")

    def sound_converter(
        self,
        *,
        appkey,
        access,
        secret,
        text,
        voice="Aitong",
        format="MP3",
        sample_rate=16000,
        volume=50,
        speech_rate=0,
        pitch_rate=0,
    ):
        return self.request(
            endpoint="/data/sound/converter",
            appkey=appkey,
            access=access,
            secret=secret,
            text=text,
            voice=voice,
            format=format,
            sample_rate=sample_rate,
            volume=volume,
            speech_rate=speech_rate,
            pitch_rate=pitch_rate,
        )


class AsyncJX3API:
    def __init__(
        self, *, token=None, ticket=None, base_url="https://www.jx3api.com"
    ):
        self.token = token or os.getenv("JX3API_TOKEN")
        self.ticket = ticket or os.getenv("JX3API_TICKET")

        self.base_url = base_url

        if not self.token:
            logging.warning(
                "The `token` parameter is not specified, only the free API can be used."
            )

    async def request(self, *, endpoint: str, **kwargs):
        logging.debug(f"requesting: {endpoint=}, {kwargs=}")

        kwargs["ticket"] = self.ticket

        async with aiohttp.request(
            "GET",
            urljoin(base=self.base_url, url=endpoint),
            data=json.dumps(kwargs).encode(encoding="utf-8"),
            headers={"token": token} if (token := self.token) else {},
        ) as resp:
            if (data := await resp.json(loads=json.loads))["code"] != HTTPStatus.OK:
                raise APIError(code=data["code"], msg=data["msg"])

        return data["data"]

    @staticmethod
    def require_token(func: Callable[..., Any]):
        async def decorator(self, *args, **kwargs):
            if not self.token:
                raise ValueError(
                    "The `token` parameter is not specified, only the free API can be used."
                )

            return await func(self, *args, **kwargs)

        return decorator

    @staticmethod
    def require_ticket(func: Callable[..., Any]):
        def decorator(self, *args, **kwargs):
            if not self.ticket:
                raise ValueError("The `ticket` parameter must be specified.")

            return func(self, *args, **kwargs)

        return decorator

    async def active_calendar(self, *, server=None, num=0):
        return await self.request(
            endpoint="/data/active/calendar", server=server, num=num
        )

    async def active_celebs(self, *, name):
        return await self.request(endpoint="/data/active/celebs", name=name)

    async def active_list_calendar(self, *, num=15):
        return await self.request(endpoint="/data/active/list/calendar", num=num)

    async def exam_answer(self, *, subject, limit=10):
        return await self.request(
            endpoint="/data/exam/answer", subject=subject, limit=limit
        )

    async def home_furniture(self, *, name):
        return await self.request(endpoint="/data/home/furniture", name=name)

    async def home_travel(self, *, name):
        return await self.request(endpoint="/data/home/travel", name=name)

    async def news_allnews(self, *, limit=10):
        return await self.request(endpoint="/data/news/allnews", limit=limit)

    async def news_announce(self, *, limit=10):
        return await self.request(endpoint="/data/news/announce", limit=limit)

    async def server_master(self, *, name):
        return await self.request(endpoint="/data/server/master", name=name)

    async def server_check(self, *, server=None):
        return await self.request(endpoint="/data/server/check", server=server)

    async def server_status(self, *, server):
        return await self.request(endpoint="/data/server/status", server=server)

    async def home_flower(self, *, server, name=None, map=None):
        return await self.request(
            endpoint="/data/home/flower", server=server, name=name, map=map
        )

    ##########
    # VIP  I #
    ##########

    @require_token
    @require_ticket
    async def save_detailed(self, *, server, roleid):
        return await self.request(
            endpoint="/data/save/detailed", server=server, roleid=roleid
        )

    @require_token
    @require_ticket
    async def role_detailed(self, *, server, name):
        return await self.request(
            endpoint="/data/role/detailed", server=server, name=name
        )

    @require_token
    async def school_matrix(self, *, name):
        return await self.request(endpoint="/data/school/matrix", name=name)

    @require_token
    async def school_force(self, *, name):
        return await self.request(endpoint="/data/school/force", name=name)

    @require_token
    async def school_skills(self, *, name):
        return await self.request(endpoint="/data/school/skills", name=name)

    @require_token
    async def tieba_random(self, *, class_, server="-", limit=10):
        return await self.request(
            endpoint="/data/tieba/random", class_=class_, server=server, limit=limit
        )

    @require_token
    @require_ticket
    async def role_attribute(self, server, name):
        return await self.request(
            endpoint="/data/role/attribute", server=server, name=name
        )

    @require_token
    @require_ticket
    async def role_team_cd_list(self, *, server, name):
        return await self.request(
            endpoint="/data/role/teamCdList", server=server, name=name
        )

    @require_token
    @require_ticket
    async def luck_adventure(self, *, server, name):
        return await self.request(
            endpoint="/data/luck/adventure", server=server, name=name
        )

    @require_token
    async def luck_statistical(self, *, server, name, limit=20):
        return await self.request(
            endpoint="/data/luck/statistical", server=server, name=name, limit=limit
        )

    @require_token
    async def luck_server_statistical(self, *, name, limit=10):
        return await self.request(
            endpoint="/data/luck/server/statistical", name=name, limit=limit
        )

    @require_token
    async def luck_collect(self, *, server, num=7):
        return await self.request(endpoint="/data/luck/collect", server=server, num=num)

    async def role_achievement(self, *, server, role, name):
        return await self.request(
            endpoint="/data/role/achievement", server=server, role=role, name=name
        )

    @require_token
    @require_ticket
    async def arena_recent(self, *, server, name, mode=None):
        return await self.request(
            endpoint="/data/arena/recent", server=server, name=name, mode=mode
        )

    @require_token
    @require_ticket
    async def arena_awesome(self, *, mode=33, limit=20):
        return await self.request(
            endpoint="/data/arena/awesome", mode=mode, limit=limit
        )

    @require_token
    @require_ticket
    async def arena_schools(self, *, mode=33):
        return await self.request(endpoint="/data/arena/schools", mode=mode)

    @require_token
    async def member_recruit(self, *, server, keyword=None, table=1):
        return await self.request(
            endpoint="/data/member/recruit", server=server, keyword=keyword, table=table
        )

    @require_token
    async def member_teacher(self, *, server, keyword=None):
        return await self.request(
            endpoint="/data/member/teacher", server=server, keyword=keyword
        )

    @require_token
    async def member_student(self, *, server, keyword=None):
        return await self.request(
            endpoint="/data/member/student", server=server, keyword=keyword
        )

    @require_token
    async def server_sand(self, *, server):
        return await self.request(endpoint="/data/server/sand", server=server)

    @require_token
    async def server_event(self, *, name=None, limit):
        return await self.request(endpoint="/data/server/event", name=name, limit=limit)

    @require_token
    async def table_records(self, *, name):
        return await self.request(endpoint="/data/table/records", name=name)

    @require_token
    async def trade_demon(self, *, server=None, limit=10):
        return await self.request(
            endpoint="/data/trade/demon", server=server, limit=limit
        )

    @require_token
    async def trade_records(self, *, name, server=None):
        return await self.request(
            endpoint="/data/trade/records", server=server, name=name
        )

    @require_token
    async def tieba_item_records(self, *, server="-", name, limit=10):
        return await self.request(
            endpoint="/data/tieba/item/records", server=server, name=name, limit=limit
        )

    @require_token
    async def valuables_statistical(self, *, server, name, limit=20):
        return await self.request(
            endpoint="/data/valuables/statistical",
            server=server,
            name=name,
            limit=limit,
        )

    @require_token
    async def valuables_server_statistical(self, *, name, limit=10):
        return await self.request(
            endpoint="/data/valuables/server/statistical", name=name, limit=limit
        )

    @require_token
    async def server_antivice(self, *, server=None):
        return await self.request(endpoint="/data/server/antivice", server=server)

    @require_token
    async def rank_statistical(self, *, server, table, name):
        return await self.request(
            endpoint="/data/rank/statistical", server=server, table=table, name=name
        )

    @require_token
    async def rank_server_statistical(self, *, table, name):
        return await self.request(
            endpoint="/data/rank/server/statistical", table=table, name=name
        )

    @require_token
    @require_ticket
    async def school_rank_statistical(self, *, school="ALL", server="ALL"):
        return await self.request(
            endpoint="/data/school/rank/statistical", school=school, server=server
        )

    @require_token
    async def fraud_detailed(self, *, uid):
        return await self.request(endpoint="/data/fraud/detailed", uid=uid)

    ##########
    # VIP II #
    ##########

    @require_token
    async def active_monster(
        self,
    ):
        return await self.request(endpoint="/data/active/monster")

    @require_token
    async def horse_records(self, *, server):
        return await self.request(endpoint="/data/horse/records", server=server)

    @require_token
    async def horse_ranch(self, *, server):
        return await self.request(endpoint="/data/horse/ranch", server=server)

    @require_token
    async def fireworks_records(self, *, server, name):
        return await self.request(
            endpoint="/data/fireworks/records", server=server, name=name
        )

    @require_token
    async def fireworks_statistical(self, *, server, name, limit=20):
        return await self.request(
            endpoint="/data/fireworks/statistical",
            server=server,
            name=name,
            limit=limit,
        )

    @require_token
    async def fireworks_collect(self, *, server, num=7):
        return await self.request(
            endpoint="/data/fireworks/collect", server=server, num=num
        )

    @require_token
    async def fireworks_rank_statistical(self, *, server, column, this_time, that_time):
        return await self.request(
            endpoint="/data/fireworks/rank/statistical",
            server=server,
            column=column,
            this_time=this_time,
            that_time=that_time,
        )

    @require_token
    async def show_card(self, *, server, name):
        return await self.request(endpoint="/data/show/card", server=server, name=name)

    @require_token
    async def show_cache(self, *, server, name):
        return await self.request(endpoint="/data/show/cache", server=server, name=name)

    @require_token
    async def show_random(self, *, server, body=None, force=None):
        return await self.request(
            endpoint="/data/show/random", server=server, body=body, force=force
        )

    #############
    #    VRF    #
    #############
    @require_token
    async def mixed_chat(self, *, name, text):
        return await self.request(endpoint="/data/mixed/chat", name=name, text=text)

    async def music_tencent(self, *, name):
        return await self.request(endpoint="/data/music/tencent", name=name)

    async def music_netease(self, *, name):
        return await self.request(endpoint="/data/music/netease", name=name)

    async def music_kugou(self, *, name):
        return await self.request(endpoint="/data/music/kugou", name=name)

    async def idiom_solitaire(self, *, name):
        return await self.request(endpoint="/data/idiom/solitaire", name=name)

    async def saohua_random(self):
        return await self.request(endpoint="/data/saohua/random")

    async def saohua_content(self):
        return await self.request(endpoint="/data/saohua/content")

    async def sound_converter(
        self,
        *,
        appkey,
        access,
        secret,
        text,
        voice="Aitong",
        format="MP3",
        sample_rate=16000,
        volume=50,
        speech_rate=0,
        pitch_rate=0,
    ):
        return await self.request(
            endpoint="/data/sound/converter",
            appkey=appkey,
            access=access,
            secret=secret,
            text=text,
            voice=voice,
            format=format,
            sample_rate=sample_rate,
            volume=volume,
            speech_rate=speech_rate,
            pitch_rate=pitch_rate,
        )

    #############
    # Websocket #
    #############

    @require_token
    async def socket(self):
        async with (
            aiohttp.ClientSession(
                headers={"token": token} if (token := self.token) else {}
            ) as session,
            session.ws_connect("wss://event.jx3api.com") as ws,
        ):
            logging.info("websocket connected")

            async for msg in ws:
                if (data := json.loads(msg.data))["action"] == 10000:
                    logging.info(data["message"])
                    continue

                yield data
