import logging
import os
from collections.abc import Callable
from functools import wraps
from http import HTTPStatus
from typing import Any

import httpx

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s][%(module)s:%(funcName)s:%(lineno)d]: %(message)s",
)


class APIError(BaseException):
    def __init__(self, *, code: int, msg: str) -> None:
        self.code = code
        self.msg = msg


class JX3API:
    def __init__(
        self,
        *,
        token: str | None = None,
        ticket: str | None = None,
        base_url="https://www.jx3api.com",
        **kwargs,
    ):
        self.token = token or os.getenv("JX3API_TOKEN")
        self.ticket = ticket or os.getenv("JX3API_TICKET")

        self.client = httpx.Client(base_url=base_url, **kwargs)

        if not self.token:
            logging.warning(
                "The `token` parameter is not specified, only the free API can be used."
            )

    def request(self, *, endpoint: str, **kwargs):
        logging.debug(f"requesting: {endpoint=}, {kwargs=}")

        payload = {key: value for key, value in kwargs.items() if value is not None}

        if self.token:
            payload["token"] = self.token

        if self.ticket:
            payload["ticket"] = self.ticket

        try:
            resp = self.client.get(endpoint, params=payload)
        except httpx.RequestError as exc:
            raise APIError(code=0, msg=str(exc)) from exc

        try:
            resp.raise_for_status()
            data = resp.json()

        except httpx.HTTPStatusError as exc:
            raise APIError(
                code=exc.response.status_code, msg=exc.response.text
            ) from exc

        except ValueError as exc:
            raise APIError(code=resp.status_code, msg="Invalid JSON response.") from exc

        if data.get("code") != HTTPStatus.OK:
            raise APIError(
                code=data.get("code", resp.status_code),
                msg=data.get("msg", "Unknown API error."),
            )

        return data.get("data")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()

    @staticmethod
    def require_token(func: Callable[..., Any]):
        @wraps(func)
        def decorator(self, *args, **kwargs):
            if not self.token:
                raise ValueError(
                    "The `token` parameter is not specified, only the free API can be used."
                )

            return func(self, *args, **kwargs)

        return decorator

    @staticmethod
    def require_ticket(func: Callable[..., Any]):
        @wraps(func)
        def decorator(self, *args, **kwargs):
            if not self.ticket:
                raise ValueError("The `ticket` parameter must be specified.")

            return func(self, *args, **kwargs)

        return decorator

    def active_calendar(self, *, num=0, mode="day"):
        return self.request(endpoint="/active/calendar", num=num, mode=mode)

    def active_celebs(self, *, name):
        return self.request(endpoint="/active/celebs", name=name)

    def battle_records(self, *, server):
        return self.request(endpoint="/battle/records", server=server)

    def duowan_statistics(self, *, server=None):
        return self.request(endpoint="/duowan/statistics", server=server)

    def exam_search(self, *, subject, limit=10):
        return self.request(endpoint="/exam/search", subject=subject, limit=limit)

    def food_list(self, *, name=None):
        return self.request(endpoint="/food/list", name=name)

    def home_flower(self, *, server, name="", map=""):
        return self.request(endpoint="/home/flower", server=server, name=name, map=map)

    def home_furniture(self, *, name):
        return self.request(endpoint="/home/furniture", name=name)

    def home_travel(self, *, name):
        return self.request(endpoint="/home/travel", name=name)

    def news_announce(self, *, limit=10):
        return self.request(endpoint="/news/announce", limit=limit)

    def news_records(self, *, limit=10):
        return self.request(endpoint="/news/records", limit=limit)

    def saohua_content(self):
        return self.request(endpoint="/saohua/content")

    def saohua_random(self):
        return self.request(endpoint="/saohua/random")

    def server_status_check(self, *, server=None):
        return self.request(endpoint="/server/status/check", server=server)

    def skill_rework(self):
        return self.request(endpoint="/skill/rework")

    def sound_converter(
        self,
        *,
        appkey,
        access,
        secret,
        voice="Aitong",
        format="mp3",
        sample_rate=16000,
        volume="50",
        speech_rate="0",
        pitch_rate="0",
        text,
    ):
        return self.request(
            endpoint="/sound/converter",
            appkey=appkey,
            access=access,
            secret=secret,
            voice=voice,
            format=format,
            sample_rate=sample_rate,
            volume=volume,
            speech_rate=speech_rate,
            pitch_rate=pitch_rate,
            text=text,
        )

    ##########
    # VIP  I #
    ##########

    @require_token
    @require_ticket
    def arena_awesome(self, *, mode=33, limit=20):
        return self.request(endpoint="/arena/awesome", mode=mode, limit=limit)

    @require_token
    @require_ticket
    def arena_recent(self, *, server, name, mode=0):
        return self.request(
            endpoint="/arena/recent", server=server, name=name, mode=mode
        )

    @require_token
    @require_ticket
    def arena_schools(self, *, mode=33):
        return self.request(endpoint="/arena/schools", mode=mode)

    @require_token
    def event_collect(self, *, server, num=7):
        return self.request(endpoint="/event/collect", server=server, num=num)

    @require_token
    def event_missing(self, *, server, name):
        return self.request(endpoint="/event/missing", server=server, name=name)

    @require_token
    def event_recent(self, *, server, limit=20):
        return self.request(endpoint="/event/recent", server=server, limit=limit)

    @require_token
    def event_records(self, *, server, name, full=0):
        return self.request(
            endpoint="/event/records", server=server, name=name, full=full
        )

    @require_token
    def event_statistics(self, *, server=None, name, limit=20):
        return self.request(
            endpoint="/event/statistics", server=server, name=name, limit=limit
        )

    @require_token
    def event_strategy(self, *, name):
        return self.request(endpoint="/event/strategy", name=name)

    @require_token
    def fraud_detail(self, *, server="", uid):
        return self.request(endpoint="/fraud/detail", server=server, uid=uid)

    @require_token
    def mech_decrypt(self):
        return self.request(endpoint="/mech/decrypt")

    @require_token
    def mentor_search(self, *, label=1, server, keyword=None, limit=50):
        return self.request(
            endpoint="/mentor/search",
            label=label,
            server=server,
            keyword=keyword,
            limit=limit,
        )

    @require_token
    def raid_records(self, *, server, name):
        return self.request(endpoint="/raid/records", server=server, name=name)

    @require_token
    def ranch_records(self, *, server, expired=0):
        return self.request(endpoint="/ranch/records", server=server, expired=expired)

    @require_token
    def rank_statistics(self, *, server=None, name):
        return self.request(endpoint="/rank/statistics", server=server, name=name)

    @require_token
    def rank_trials(self, *, server=None, name):
        return self.request(endpoint="/rank/trials", server=server, name=name)

    @require_token
    def recruit_search(self, *, server, label=1, keyword=None, limit=50):
        return self.request(
            endpoint="/recruit/search",
            server=server,
            label=label,
            keyword=keyword,
            limit=limit,
        )

    @require_token
    def reward_statistics(self, *, server=None, name, limit=20):
        return self.request(
            endpoint="/reward/statistics", server=server, name=name, limit=limit
        )

    @require_token
    def role_detail(self, *, server, name, history=0):
        return self.request(
            endpoint="/role/detail", server=server, name=name, history=history
        )

    @require_token
    def sand_records(self, *, server):
        return self.request(endpoint="/sand/records", server=server)

    @require_token
    @require_ticket
    def school_matrix(self, *, name):
        return self.request(endpoint="/school/matrix", name=name)

    @require_token
    @require_ticket
    def school_seniority(self, *, server="ALL", school="ALL"):
        return self.request(endpoint="/school/seniority", school=school, server=server)

    @require_token
    @require_ticket
    def school_skills(self, *, name, update=0):
        return self.request(endpoint="/school/skills", name=name, update=update)

    @require_token
    @require_ticket
    def school_talent(self, *, name, update=0):
        return self.request(endpoint="/school/talent", name=name, update=update)

    @require_token
    def tieba_item_records(self, *, server=None, name, limit=10):
        return self.request(
            endpoint="/tieba/item/records", server=server, name=name, limit=limit
        )

    @require_token
    def tieba_random(self, *, tags, server=None, limit=10):
        return self.request(
            endpoint="/tieba/random", tags=tags, server=server, limit=limit
        )

    @require_token
    def trade_demon(self, *, server=None, limit=10):
        return self.request(endpoint="/trade/demon", server=server, limit=limit)

    @require_token
    def trade_item_records(self, *, name, server=None):
        return self.request(endpoint="/trade/item/records", name=name, server=server)

    @require_token
    def trade_item_search(self, *, name):
        return self.request(endpoint="/trade/item/search", name=name)

    @require_token
    def trade_records(self, *, name, server=None):
        return self.request(endpoint="/trade/records", name=name, server=server)

    ##########
    # VIP II #
    ##########

    @require_token
    def auction_records(self, *, server, name=None, limit=50):
        return self.request(
            endpoint="/auction/records", server=server, name=name, limit=limit
        )

    @require_token
    def card_cached(self, *, server, name):
        return self.request(endpoint="/card/cached", server=server, name=name)

    @require_token
    @require_ticket
    def card_preset(self, *, server, name):
        return self.request(endpoint="/card/preset", server=server, name=name)

    @require_token
    def card_random(self, *, server=None, force=None, body=None):
        return self.request(
            endpoint="/card/random", server=server, force=force, body=body
        )

    @require_token
    def card_record(self, *, server, name):
        return self.request(endpoint="/card/record", server=server, name=name)

    @require_token
    def card_records(self, *, server, name, like=False):
        return self.request(
            endpoint="/card/records", server=server, name=name, like=like
        )

    @require_token
    def castle_status(self):
        return self.request(endpoint="/castle/status")

    @require_token
    def chitu_records(self):
        return self.request(endpoint="/chitu/records")

    @require_token
    def chitu_week_records(self):
        return self.request(endpoint="/chitu/week/records")

    @require_token
    def fenxian_records(self, *, name=None, limit=100):
        return self.request(endpoint="/fenxian/records", name=name, limit=limit)

    @require_token
    def firework_records(self, *, server, name):
        return self.request(endpoint="/firework/records", server=server, name=name)

    @require_token
    def monster_records(self, *, server, name):
        return self.request(endpoint="/monster/records", server=server, name=name)

    @require_token
    def monster_weekly(self):
        return self.request(endpoint="/monster/weekly")

    @require_token
    def ranch_chat(self, *, server):
        return self.request(endpoint="/ranch/chat", server=server)

    @require_token
    def rank_arena(self, *, server=None, mode=0):
        return self.request(endpoint="/rank/arena", server=server, mode=mode)

    @require_token
    def rank_championship(self, *, server=None, camp=1):
        return self.request(endpoint="/rank/championship", server=server, camp=camp)

    @require_token
    def rank_constable(self, *, server=None):
        return self.request(endpoint="/rank/constable", server=server)

    @require_token
    def rank_outlaw(self, *, server=None):
        return self.request(endpoint="/rank/outlaw", server=server)

    @require_token
    def rank_wanted(self, *, server=None, mode=1):
        return self.request(endpoint="/rank/wanted", server=server, mode=mode)

    @require_token
    def role_achievement(self, *, server, role, name):
        return self.request(
            endpoint="/role/achievement", server=server, role=role, name=name
        )

    @require_token
    def saohua_context(self, *, name):
        return self.request(endpoint="/saohua/context", name=name)

    @require_token
    @require_ticket
    def school_search(self, *, name, mode=None):
        return self.request(endpoint="/school/search", name=name, mode=mode)

    @require_token
    def skill_calculate(self, *, cooldown=1.5):
        return self.request(endpoint="/skill/calculate", cooldown=cooldown)

    @require_token
    def steed_records(self, *, server=None):
        return self.request(endpoint="/steed/records", server=server)

    @require_token
    def trade_manufacture(self, *, server, name, source=0):
        return self.request(
            endpoint="/trade/manufacture",
            server=server,
            name=name,
            source=source,
        )

    @require_token
    def trade_wanbaolou(self, *, id):
        return self.request(endpoint="/trade/wanbaolou", id=id)

    @require_token
    def tuilan_achievement(self, *, server, name, class_=1, subclass=None):
        return self.request(
            endpoint="/tuilan/achievement",
            **{
                "server": server,
                "name": name,
                "class": class_,
                "subclass": subclass,
            },
        )

    @require_token
    def wicked_records(self, *, server=None, limit=20):
        return self.request(endpoint="/wicked/records", server=server, limit=limit)


class AsyncJX3API:
    def __init__(
        self,
        *,
        token: str | None = None,
        ticket: str | None = None,
        base_url: str = "https://www.jx3api.com",
        **kwargs,
    ):
        self.token = token or os.getenv("JX3API_TOKEN")
        self.ticket = ticket or os.getenv("JX3API_TICKET")

        self.client = httpx.AsyncClient(base_url=base_url, **kwargs)

        if not self.token:
            logging.warning(
                "The `token` parameter is not specified, only the free API can be used."
            )

    async def request(self, *, endpoint: str, **kwargs):
        logging.debug(f"requesting: {endpoint=}, {kwargs=}")

        payload = {key: value for key, value in kwargs.items() if value is not None}

        if self.token:
            payload["token"] = self.token

        if self.ticket:
            payload["ticket"] = self.ticket

        try:
            resp = await self.client.get(endpoint, params=payload)
        except httpx.RequestError as exc:
            raise APIError(code=0, msg=str(exc)) from exc

        try:
            resp.raise_for_status()
            data = resp.json()
        except httpx.HTTPStatusError as exc:
            raise APIError(
                code=exc.response.status_code, msg=exc.response.text
            ) from exc
        except ValueError as exc:
            raise APIError(code=resp.status_code, msg="Invalid JSON response.") from exc

        if not isinstance(data, dict):
            raise APIError(code=resp.status_code, msg="Unexpected API response.")

        if data.get("code") != HTTPStatus.OK:
            raise APIError(
                code=data.get("code", resp.status_code),
                msg=data.get("msg", "Unknown API error."),
            )

        return data.get("data")

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        await self.client.aclose()

    @staticmethod
    def require_token(func: Callable[..., Any]):
        @wraps(func)
        async def decorator(self, *args, **kwargs):
            if not self.token:
                raise ValueError(
                    "The `token` parameter is not specified, only the free API can be used."
                )

            return await func(self, *args, **kwargs)

        return decorator

    @staticmethod
    def require_ticket(func: Callable[..., Any]):
        @wraps(func)
        async def decorator(self, *args, **kwargs):
            if not self.ticket:
                raise ValueError("The `ticket` parameter must be specified.")

            return await func(self, *args, **kwargs)

        return decorator

    async def active_calendar(self, *, num=0, mode="day"):
        return await self.request(endpoint="/active/calendar", num=num, mode=mode)

    async def active_celebs(self, *, name):
        return await self.request(endpoint="/active/celebs", name=name)

    async def battle_records(self, *, server):
        return await self.request(endpoint="/battle/records", server=server)

    async def duowan_statistics(self, *, server=None):
        return await self.request(endpoint="/duowan/statistics", server=server)

    async def exam_search(self, *, subject, limit=10):
        return await self.request(endpoint="/exam/search", subject=subject, limit=limit)

    async def food_list(self, *, name=None):
        return await self.request(endpoint="/food/list", name=name)

    async def home_flower(self, *, server, name="", map=""):
        return await self.request(
            endpoint="/home/flower", server=server, name=name, map=map
        )

    async def home_furniture(self, *, name):
        return await self.request(endpoint="/home/furniture", name=name)

    async def home_travel(self, *, name):
        return await self.request(endpoint="/home/travel", name=name)

    async def news_announce(self, *, limit=10):
        return await self.request(endpoint="/news/announce", limit=limit)

    async def news_records(self, *, limit=10):
        return await self.request(endpoint="/news/records", limit=limit)

    async def saohua_content(self):
        return await self.request(endpoint="/saohua/content")

    async def saohua_random(self):
        return await self.request(endpoint="/saohua/random")

    async def server_status_check(self, *, server=None):
        return await self.request(endpoint="/server/status/check", server=server)

    async def skill_rework(self):
        return await self.request(endpoint="/skill/rework")

    async def sound_converter(
        self,
        *,
        appkey,
        access,
        secret,
        voice="Aitong",
        format="mp3",
        sample_rate=16000,
        volume="50",
        speech_rate="0",
        pitch_rate="0",
        text,
    ):
        return await self.request(
            endpoint="/sound/converter",
            appkey=appkey,
            access=access,
            secret=secret,
            voice=voice,
            format=format,
            sample_rate=sample_rate,
            volume=volume,
            speech_rate=speech_rate,
            pitch_rate=pitch_rate,
            text=text,
        )

    ##########
    # VIP  I #
    ##########

    @require_token
    @require_ticket
    async def arena_awesome(self, *, mode=33, limit=20):
        return await self.request(endpoint="/arena/awesome", mode=mode, limit=limit)

    @require_token
    @require_ticket
    async def arena_recent(self, *, server, name, mode=0):
        return await self.request(
            endpoint="/arena/recent", server=server, name=name, mode=mode
        )

    @require_token
    @require_ticket
    async def arena_schools(self, *, mode=33):
        return await self.request(endpoint="/arena/schools", mode=mode)

    @require_token
    async def event_collect(self, *, server, num=7):
        return await self.request(endpoint="/event/collect", server=server, num=num)

    @require_token
    async def event_missing(self, *, server, name):
        return await self.request(endpoint="/event/missing", server=server, name=name)

    @require_token
    async def event_recent(self, *, server, limit=20):
        return await self.request(endpoint="/event/recent", server=server, limit=limit)

    @require_token
    async def event_records(self, *, server, name, full=0):
        return await self.request(
            endpoint="/event/records", server=server, name=name, full=full
        )

    @require_token
    async def event_statistics(self, *, server=None, name, limit=20):
        return await self.request(
            endpoint="/event/statistics", server=server, name=name, limit=limit
        )

    @require_token
    async def event_strategy(self, *, name):
        return await self.request(endpoint="/event/strategy", name=name)

    @require_token
    async def fraud_detail(self, *, server="", uid):
        return await self.request(endpoint="/fraud/detail", server=server, uid=uid)

    @require_token
    async def mech_decrypt(self):
        return await self.request(endpoint="/mech/decrypt")

    @require_token
    async def mentor_search(self, *, label=1, server, keyword=None, limit=50):
        return await self.request(
            endpoint="/mentor/search",
            label=label,
            server=server,
            keyword=keyword,
            limit=limit,
        )

    @require_token
    async def raid_records(self, *, server, name):
        return await self.request(endpoint="/raid/records", server=server, name=name)

    @require_token
    async def ranch_records(self, *, server, expired=0):
        return await self.request(
            endpoint="/ranch/records", server=server, expired=expired
        )

    @require_token
    async def rank_statistics(self, *, server=None, name):
        return await self.request(endpoint="/rank/statistics", server=server, name=name)

    @require_token
    async def rank_trials(self, *, server=None, name):
        return await self.request(endpoint="/rank/trials", server=server, name=name)

    @require_token
    async def recruit_search(self, *, server, label=1, keyword=None, limit=50):
        return await self.request(
            endpoint="/recruit/search",
            server=server,
            label=label,
            keyword=keyword,
            limit=limit,
        )

    @require_token
    async def reward_statistics(self, *, server=None, name, limit=20):
        return await self.request(
            endpoint="/reward/statistics",
            server=server,
            name=name,
            limit=limit,
        )

    @require_token
    async def role_detail(self, *, server, name, history=0):
        return await self.request(
            endpoint="/role/detail", server=server, name=name, history=history
        )

    @require_token
    async def sand_records(self, *, server):
        return await self.request(endpoint="/sand/records", server=server)

    @require_token
    @require_ticket
    async def school_matrix(self, *, name):
        return await self.request(endpoint="/school/matrix", name=name)

    @require_token
    @require_ticket
    async def school_seniority(self, *, server="ALL", school="ALL"):
        return await self.request(
            endpoint="/school/seniority", school=school, server=server
        )

    @require_token
    @require_ticket
    async def school_skills(self, *, name, update=0):
        return await self.request(endpoint="/school/skills", name=name, update=update)

    @require_token
    @require_ticket
    async def school_talent(self, *, name, update=0):
        return await self.request(endpoint="/school/talent", name=name, update=update)

    @require_token
    async def tieba_item_records(self, *, server=None, name, limit=10):
        return await self.request(
            endpoint="/tieba/item/records", server=server, name=name, limit=limit
        )

    @require_token
    async def tieba_random(self, *, tags, server=None, limit=10):
        return await self.request(
            endpoint="/tieba/random", tags=tags, server=server, limit=limit
        )

    @require_token
    async def trade_demon(self, *, server=None, limit=10):
        return await self.request(endpoint="/trade/demon", server=server, limit=limit)

    @require_token
    async def trade_item_records(self, *, name, server=None):
        return await self.request(
            endpoint="/trade/item/records", name=name, server=server
        )

    @require_token
    async def trade_item_search(self, *, name):
        return await self.request(endpoint="/trade/item/search", name=name)

    @require_token
    async def trade_records(self, *, name, server=None):
        return await self.request(endpoint="/trade/records", name=name, server=server)

    ##########
    # VIP II #
    ##########

    @require_token
    async def auction_records(self, *, server, name=None, limit=50):
        return await self.request(
            endpoint="/auction/records", server=server, name=name, limit=limit
        )

    @require_token
    async def card_cached(self, *, server, name):
        return await self.request(endpoint="/card/cached", server=server, name=name)

    @require_token
    @require_ticket
    async def card_preset(self, *, server, name):
        return await self.request(endpoint="/card/preset", server=server, name=name)

    @require_token
    async def card_random(self, *, server=None, force=None, body=None):
        return await self.request(
            endpoint="/card/random", server=server, force=force, body=body
        )

    @require_token
    async def card_record(self, *, server, name):
        return await self.request(endpoint="/card/record", server=server, name=name)

    @require_token
    async def card_records(self, *, server, name, like=False):
        return await self.request(
            endpoint="/card/records", server=server, name=name, like=like
        )

    @require_token
    async def castle_status(self):
        return await self.request(endpoint="/castle/status")

    @require_token
    async def chitu_records(self):
        return await self.request(endpoint="/chitu/records")

    @require_token
    async def chitu_week_records(self):
        return await self.request(endpoint="/chitu/week/records")

    @require_token
    async def fenxian_records(self, *, name=None, limit=100):
        return await self.request(endpoint="/fenxian/records", name=name, limit=limit)

    @require_token
    async def firework_records(self, *, server, name):
        return await self.request(
            endpoint="/firework/records", server=server, name=name
        )

    @require_token
    async def monster_records(self, *, server, name):
        return await self.request(endpoint="/monster/records", server=server, name=name)

    @require_token
    async def monster_weekly(self):
        return await self.request(endpoint="/monster/weekly")

    @require_token
    async def ranch_chat(self, *, server):
        return await self.request(endpoint="/ranch/chat", server=server)

    @require_token
    async def rank_arena(self, *, server=None, mode=0):
        return await self.request(endpoint="/rank/arena", server=server, mode=mode)

    @require_token
    async def rank_championship(self, *, server=None, camp=1):
        return await self.request(
            endpoint="/rank/championship", server=server, camp=camp
        )

    @require_token
    async def rank_constable(self, *, server=None):
        return await self.request(endpoint="/rank/constable", server=server)

    @require_token
    async def rank_outlaw(self, *, server=None):
        return await self.request(endpoint="/rank/outlaw", server=server)

    @require_token
    async def rank_wanted(self, *, server=None, mode=1):
        return await self.request(endpoint="/rank/wanted", server=server, mode=mode)

    @require_token
    async def role_achievement(self, *, server, role, name):
        return await self.request(
            endpoint="/role/achievement", server=server, role=role, name=name
        )

    @require_token
    async def saohua_context(self, *, name):
        return await self.request(endpoint="/saohua/context", name=name)

    @require_token
    @require_ticket
    async def school_search(self, *, name, mode=None):
        return await self.request(endpoint="/school/search", name=name, mode=mode)

    @require_token
    async def skill_calculate(self, *, cooldown=1.5):
        return await self.request(endpoint="/skill/calculate", cooldown=cooldown)

    @require_token
    async def steed_records(self, *, server=None):
        return await self.request(endpoint="/steed/records", server=server)

    @require_token
    async def trade_manufacture(self, *, server, name, source=0):
        return await self.request(
            endpoint="/trade/manufacture",
            server=server,
            name=name,
            source=source,
        )

    @require_token
    async def trade_wanbaolou(self, *, id):
        return await self.request(endpoint="/trade/wanbaolou", id=id)

    @require_token
    async def tuilan_achievement(self, *, server, name, class_=1, subclass=None):
        return await self.request(
            endpoint="/tuilan/achievement",
            **{
                "server": server,
                "name": name,
                "class": class_,
                "subclass": subclass,
            },
        )

    @require_token
    async def wicked_records(self, *, server=None, limit=20):
        return await self.request(
            endpoint="/wicked/records", server=server, limit=limit
        )
