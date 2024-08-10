import logging
import os
from contextlib import closing
from functools import partial
from http import HTTPStatus
from typing import (
    Annotated,
    Any,
    AsyncGenerator,
    Awaitable,
    Callable,
    Dict,
    Literal,
    Sequence,
)
from urllib.parse import urljoin
from urllib.request import Request, urlopen

import aiohttp

from .exception import APIError
from .response import (
    ResponseActiveCalendar,
    ResponseActiveCelebs,
    ResponseActiveListCalendar,
    ResponseActiveMonster,
    ResponseExamAnswer,
    ResponseFireworkCollect,
    ResponseFireworkRankStatistical,
    ResponseFireworkRecord,
    ResponseFireworkStatistical,
    ResponseHomeFlower,
    ResponseHomeFurniture,
    ResponseHomeTravel,
    ResponseHorseRanch,
    ResponseHorseRecord,
    ResponseLuckAdventure,
    ResponseLuckCollect,
    ResponseLuckServerStatistical,
    ResponseLuckStatistical,
    ResponseMatchAwesome,
    ResponseMatchRecent,
    ResponseMatchSchools,
    ResponseMemberRecruit,
    ResponseMemberStudent,
    ResponseMemberTeacher,
    ResponseNewsAllnews,
    ResponseNewsAnnounce,
    ResponseRankServerStatistical,
    ResponseRankStatistical,
    ResponseRoleAchievement,
    ResponseRoleDetailed,
    ResponseRoleTeamCdList,
    ResponseSaveDetailed,
    ResponseSchoolForce,
    ResponseSchoolMatrix,
    ResponseSchoolRankStatistical,
    ResponseSchoolSkills,
    ResponseServerAntivice,
    ResponseServerCheck,
    ResponseServerEvent,
    ResponseServerMaster,
    ResponseServerSand,
    ResponseServerStatus,
    ResponseTiebaItemRecords,
    ResponseTiebaRandom,
    ResponseTradeDemon,
    ResponseTradeRecord,
    ResponseValuablesServerStatistical,
    ResponseValuablesStatistical,
)

try:
    import ujson as json

    json.dumps = partial(json.dumps, ensure_ascii=False, sort_keys=False)

except ImportError:
    import json

    json.dumps = partial(
        json.dumps, ensure_ascii=False, separators=(",", ":"), sort_keys=False
    )

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s][%(module)s:%(funcName)s:%(lineno)d]: %(message)s",
)


class JX3API:
    def __init__(
        self,
        *,
        token: Annotated[str | None, "推栏 token"] = None,
        ticket: Annotated[str | None, "站点标识"] = None,
        base_url: str = "https://www.jx3api.com",
    ) -> None:
        self.token = token or os.getenv("JX3API_TOKEN")
        self.ticket = ticket or os.getenv("JX3API_TICKET")

        self.base_url = base_url

        if not self.token:
            logging.warning(
                "The `token` parameter is not specified, only the free API can be used."
            )

    def request(self, *, endpoint: str, **kwargs) -> Any:
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
    def require_token(func: Callable[..., Any]) -> Callable[..., Any]:
        def decorator(self, *args, **kwargs) -> Callable[..., Any]:
            if not self.token:
                raise ValueError(
                    "The `token` parameter is not specified, only the free API can be used."
                )

            return func(self, *args, **kwargs)

        return decorator

    @staticmethod
    def require_ticket(func: Callable[..., Any]) -> Callable[..., Any]:
        def decorator(self, *args, **kwargs) -> Callable[..., Any]:
            if not self.ticket:
                raise ValueError("The `ticket` parameter must be specified.")

            return func(self, *args, **kwargs)

        return decorator

    ############
    # FREE API #
    ############

    def active_calendar(
        self,
        *,
        server: Annotated[str | None, "区服名称，查找该区服的记录。"] = None,
        num: Annotated[
            int,
            "指定日期，查询指定日期的日常，默认值 : ``0`` 为当天，``1`` 为明天，以此类推。",
        ] = 0,
    ) -> Annotated[ResponseActiveCalendar, "今天、明天、后天、日常任务"]:
        """
        active_calendar 活动日历

        今天、明天、后天、日常任务。
        只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键对值。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。
            num (int, optional): 指定日期，查询指定日期的日常，默认值 : ``0`` 为当天，``1`` 为明天，以此类推。

        Returns:
            ResponseActiveCalendar: 今天、明天、后天、日常任务。
        """
        return self.request(endpoint="/data/active/calendar", server=server, num=num)

    def active_list_calendar(
        self,
        *,
        num: Annotated[
            int, "预测时间，查询指定时间内的月历，默认值 : ``15`` 为前后15天的月历"
        ] = 15,
    ) -> Annotated[ResponseActiveListCalendar, "预测每天的日常任务"]:
        """
        active_list_calendar 活动月历

        预测每天的日常任务。
        只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键对值。

        Args:
            num (int, optional): 预测时间，查询指定时间内的月历，默认值 : ``15`` 为前后15天的月历。

        Returns:
            ResponseActiveListCalendar: 预测每天的日常任务。
        """
        return self.request(endpoint="/data/active/list/calendar", num=num)

    def active_celebs(
        self,
        *,
        name: Annotated[str, "名称，查询指定事件的记录"],
    ) -> Annotated[Sequence[ResponseActiveCelebs], "当前时间的楚天社/云从社进度"]:
        """
        active_celebs 行侠事件

        当前时间的楚天社/云从社进度。

        Args:
            name (str): 名称，查询指定事件的记录。

        Returns:
            Sequence[ResponseActiveCelebs]: 当前时间的楚天社/云从社进度。
        """
        return self.request(endpoint="/data/active/celebs", name=name)

    def exam_answer(
        self,
        *,
        subject: Annotated[str, "科举试题，支持首字母，支持模糊查询"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Sequence[ResponseExamAnswer], "科举答题"]:
        """
        exam_answer 科举试题

        科举答题

        Args:
            subject (str): 科举试题，支持首字母，支持模糊查询。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[ResponseExamAnswer]: 科举答题。
        """
        return self.request(endpoint="/data/exam/answer", subject=subject, limit=limit)

    def home_furniture(
        self,
        *,
        name: Annotated[str, "指定装饰，查找该装饰的详细记录"],
    ) -> Annotated[ResponseHomeFurniture, "装饰详情"]:
        """
        home_furniture 家园装饰

        装饰详情

        Args:
            name (str): 指定装饰，查找该装饰的详细记录。

        Returns:
            ResponseHomeFurniture: 装饰详情。
        """
        return self.request(endpoint="/data/home/furniture", name=name)

    def home_travel(
        self,
        *,
        name: Annotated[str, "地图，查找该地图的装饰产出"],
    ) -> Annotated[Sequence[ResponseHomeTravel], "器物谱地图产出装饰"]:
        """
        home_travel 器物图谱

        器物谱地图产出装饰

        Args:
            name (str): 地图，查找该地图的装饰产出。

        Returns:
            Sequence[ResponseHomeTravel]: 器物谱地图产出装饰。
        """
        return self.request(endpoint="/data/home/travel", name=name)

    def news_allnews(
        self,
        *,
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Sequence[ResponseNewsAllnews], "官方最新公告及新闻"]:
        """
        news_allnews 新闻资讯

        官方最新公告及新闻

        Args:
            limit (int, optional): 限制查询结果的数量，默认值 10.

        Returns:
            Sequence[ResponseNewsAllnews]: 官方最新公告及新闻。
        """
        return self.request(endpoint="/data/news/allnews", limit=limit)

    def news_announce(
        self,
        *,
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Sequence[ResponseNewsAnnounce], "官方最新维护公告"]:
        """
        news_announce 维护公告

        官方最新维护公告

        Args:
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[ResponseNewsAnnounce]: 官方最新维护公告。
        """
        return self.request(endpoint="/data/news/announce", limit=limit)

    def server_master(
        self,
        *,
        name: Annotated[str, "指定区服，查找该区服的相关记录"],
    ) -> Annotated[ResponseServerMaster, "简称搜索主次服务器"]:
        """
        server_master 搜索区服

        简称搜索主次服务器

        Args:
            name (str): 指定区服，查找该区服的相关记录。

        Returns:
            ResponseServerMaster: 简称搜索主次服务器。
        """
        return self.request(endpoint="/data/server/master", name=name)

    def server_check(
        self,
        *,
        server: Annotated[
            str | None,
            "可选的服务器名称，查找该区服的相关记录；未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)",
        ] = None,
    ) -> Annotated[ResponseServerCheck, "服务器当前状态 [ 已开服/维护中 ]"]:
        """
        server_check 开服检查

        服务器当前状态 [ 已开服/维护中 ]

        Args:
            server (str, optional): 可选的服务器名称，查找该区服的相关记录；未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)。

        Returns:
            ResponseServerCheck: 服务器当前状态 [ 已开服/维护中 ]
        """
        return self.request(endpoint="/data/server/check", server=server)

    def server_status(
        self,
        *,
        server: Annotated[str, "指定区服，查找该区服的相关记录"],
    ) -> Annotated[ResponseServerStatus, "服务器当前状态"]:
        """
        server_status 查看状态

        服务器当前状态 [ 维护/正常/繁忙/爆满 ]

        Args:
            server (str): 指定区服，查找该区服的相关记录。

        Returns:
            ResponseServerStatus: 服务器当前状态。
        """
        return self.request(endpoint="/data/server/status", server=server)

    def home_flower(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str | None, "鲜花，查找该鲜花的相关记录"] = None,
        map: Annotated[str | None, "地图，查找该地图的相关记录"] = None,
    ) -> Annotated[ResponseHomeFlower, "家园鲜花最高价格线路"]:
        """
        home_flower 鲜花价格

        家园鲜花最高价格线路。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str, optional): 鲜花，查找该鲜花的相关记录。
            map (str, optional): 地图，查找该地图的相关记录。

        Returns:
            ResponseHomeFlowerData: 家园鲜花最高价格线路。
        """
        return self.request(
            endpoint="/data/home/flower", server=server, name=name, map=map
        )

    ##########
    # VIP  I #
    ##########

    @require_token
    @require_ticket
    def save_detailed(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        roleid: Annotated[str, "角色UID，保存该角色的详细记录"],
    ) -> Annotated[ResponseSaveDetailed, "自动更新角色信息"]:
        """
        save_detailed 角色更新

        自动更新角色信息。

        Args:
            server (str): 区服，查找该区服的相关记录。
            roleid (str): 角色UID，保存该角色的详细记录。

        Returns:
            ResponseSaveDetailed: 自动更新角色信息。
        """
        return self.request(
            endpoint="/data/save/detailed", server=server, roleid=roleid
        )

    @require_token
    @require_ticket
    def role_detailed(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找目标角色的相关记录"],
    ) -> Annotated[ResponseRoleDetailed, "角色详细信息"]:
        """
        role_detailed 角色信息

        角色详细信息

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找目标角色的相关记录。

        Returns:
            ResponseRoleDetailed: 角色详细信息。
        """
        return self.request(endpoint="/data/role/detailed", server=server, name=name)

    @require_token
    def school_matrix(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[ResponseSchoolMatrix, "职业阵眼效果"]:
        """
        school_matrix 阵眼效果

        职业阵眼效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            ResponseSchoolMatrix: 职业阵眼效果。
        """
        return self.request(endpoint="/data/school/matrix", name=name)

    @require_token
    def school_force(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[Sequence[ResponseSchoolForce], "奇穴详细效果"]:
        """
        school_force 奇穴效果

        奇穴详细效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            Sequence[ResponseSchoolForce]: 奇穴详细效果。
        """
        return self.request(endpoint="/data/school/force", name=name)

    @require_token
    def school_skills(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[Sequence[ResponseSchoolSkills], "技能详细效果"]:
        """
        school_skills 技能效果

        技能详细效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            Sequence[ResponseSchoolSkills]: 技能详细效果。
        """
        return self.request(endpoint="/data/school/skills", name=name)

    @require_token
    def tieba_random(
        self,
        *,
        class_: Annotated[
            str,
            "帖子分类，可选范围：``818`` ``616`` ``鬼网三`` ``鬼网3`` ``树洞`` ``记录`` ``教程`` ``街拍`` ``故事`` ``避雷`` ``吐槽`` ``提问``",
        ],
        server: Annotated[
            str, "区服名称，查找该区服的相关记录，默认值：``-`` 为全区服"
        ] = "-",
        limit: Annotated[int, "限制查询结果的数量，默认值 ``10``"] = 10,
    ) -> Annotated[Sequence[ResponseTiebaRandom], "随机搜索贴吧 : 818/616...."]:
        """
        tieba_random 八卦帖子

        禁止轮询，随机搜索贴吧 : 818/616....

        Args:
            class (str): 帖子分类，可选范围：``818`` ``616`` ``鬼网三`` ``鬼网3`` ``树洞`` ``记录`` ``教程`` ``街拍`` ``故事`` ``避雷`` ``吐槽`` ``提问``
            server (str, optional): 区服名称，查找该区服的相关记录，默认值：``-`` 为全区服。
            limit (int, optional): 限制查询结果的数量，默认值 ``10``。

        Returns:
            Sequence[ResponseTiebaRandom]: 随机搜索贴吧 : 818/616....
        """
        return self.request(
            endpoint="/data/tieba/random", class_=class_, server=server, limit=limit
        )

    @require_token
    @require_ticket
    def role_attribute(
        self, server: Annotated[str, "服务器"], name: Annotated[str, "角色名"]
    ) -> Dict:
        """
        role_attribute 角色装备

        角色装备属性详情

        Args:
            server (str): 服务器。
            name (str): 角色名。

        Returns:
            Dict: 角色装备属性详情。
        """
        return self.request(endpoint="/role/attribute", server=server, name=name)

    @require_token
    @require_ticket
    def role_team_cd_list(
        self,
        *,
        server: Annotated[str, "区服名称，查找该区服的记录"],
        name: Annotated[str, "角色名称，查找该角色的记录"],
    ) -> Annotated[ResponseRoleTeamCdList, "角色副本记录"]:
        """
        role_team_cd_list 副本记录

        角色副本记录

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            ResponseRoleTeamCdList: 角色副本记录。
        """
        return self.request(endpoint="/data/role/teamCdList", server=server, name=name)

    @require_token
    @require_ticket
    def luck_adventure(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
    ) -> Annotated[Sequence[ResponseLuckAdventure], "角色奇遇触发记录(不保证遗漏)"]:
        """
        luck_adventure 奇遇记录

        角色奇遇触发记录(不保证遗漏)

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。

        Returns:
            Sequence[ResponseLuckAdventure]: 角色奇遇触发记录(不保证遗漏)。
        """
        return self.request(endpoint="/data/luck/adventure", server=server, name=name)

    @require_token
    def luck_statistical(
        self,
        *,
        server: Annotated[str, "区服名称，查找该区服的记录"],
        name: Annotated[str, "奇遇名称，查找该奇遇的记录"],
        limit: Annotated[int, "单页数量，单页返回的数量，默认值 : 20"] = 20,
    ) -> Annotated[Sequence[ResponseLuckStatistical], "奇遇近期触发统计"]:
        """
        luck_statistical 奇遇统计

        奇遇近期触发统计

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 奇遇名称，查找该奇遇的记录。
            limit (int, optional): 单页数量，单页返回的数量，默认值 : 20。

        Returns:
            Sequence[ResponseLuckStatistical]: 奇遇近期触发统计。
        """
        return self.request(
            endpoint="/data/luck/statistical", server=server, name=name, limit=limit
        )

    @require_token
    def luck_server_statistical(
        self,
        *,
        name: Annotated[str, "奇遇名称，查找该奇遇的全服统计"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[
        Sequence[ResponseLuckServerStatistical], "统计全服近期奇遇记录，不区分区服"
    ]:
        """
        luck_server_statistical 全服统计

        统计全服近期奇遇记录，不区分区服。

        Args:
            name (str): 奇遇名称，查找该奇遇的全服统计。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[ResponseLuckServerStatistical]: 统计全服近期奇遇记录，不区分区服。
        """
        return self.request(
            endpoint="/data/luck/server/statistical", name=name, limit=limit
        )

    @require_token
    def luck_collect(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        num: Annotated[int, "汇总时间，汇总指定天数内的记录，默认值 : 7"] = 7,
    ) -> Annotated[Sequence[ResponseLuckCollect], "统计奇遇近期触发角色记录"]:
        """
        luck_collect 奇遇汇总

        统计奇遇近期触发角色记录

        Args:
            server (str): 区服，查找该区服的相关记录。
            num (int, optional): 汇总时间，汇总指定天数内的记录，默认值 : 7。

        Returns:
            Sequence[ResponseLuckCollect]: 统计奇遇近期触发角色记录。
        """
        return self.request(endpoint="/data/luck/collect", server=server, num=num)

    @require_token
    @require_ticket
    def role_achievement(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        role: Annotated[str, "角色名称，查找该角色的成就记录"],
        name: Annotated[str, "成就/系列名称，查询该成就/系列的完成进度"],
    ) -> Annotated[ResponseRoleAchievement, "角色成就进度"]:
        """
        role_achievement 成就百科

        角色成就进度

        Args:
            server (str): 区服，查找该区服的相关记录。
            role (str): 角色名称，查找该角色的成就记录。
            name (str): 成就/系列名称，查询该成就/系列的完成进度。

        Returns:
            ResponseRoleAchievement: 角色成就进度。
        """
        return self.request(
            endpoint="/data/role/achievement", server=server, role=role, name=name
        )

    @require_token
    @require_ticket
    def match_recent(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
        mode: Annotated[int | None, "比赛模式，查找该模式的相关记录"] = None,
    ) -> Annotated[ResponseMatchRecent, "角色近期战绩记录"]:
        """
        match_recent 名剑战绩

        角色近期战绩记录

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。
            mode (int, optional): 比赛模式，查找该模式的相关记录。

        Returns:
            ResponseMatchRecent: 角色近期战绩记录。
        """
        return self.request(
            endpoint="/data/match/recent", server=server, name=name, mode=mode
        )

    @require_token
    @require_ticket
    def match_awesome(
        self,
        *,
        mode: Annotated[int, "比赛模式，查找该模式的相关记录，默认值 : 33"] = 33,
        limit: Annotated[int, "限制查询结果的数量，默认值 20"] = 20,
    ) -> Annotated[Sequence[ResponseMatchAwesome], "角色近期战绩记录"]:
        """
        match_awesome 名剑排行

        角色近期战绩记录。

        Args:
            mode (int, optional): 比赛模式，查找该模式的相关记录，默认值 : 33. Defaults to 33.
            limit (int, optional): 限制查询结果的数量，默认值 20。

        Returns:
            Sequence[ResponseMatchAwesome]: 角色近期战绩记录。
        """
        return self.request(endpoint="/data/match/awesome", mode=mode, limit=limit)

    @require_token
    @require_ticket
    def match_schools(
        self,
        *,
        mode: Annotated[int, "比赛模式，查找该模式的相关记录，默认值 : 33"] = 33,
    ) -> Annotated[Sequence[ResponseMatchSchools], "角色近期战绩记录"]:
        """
        match_schools 名剑统计

        角色近期战绩记录

        Args:
            mode (int, optional): 比赛模式，查找该模式的相关记录，默认值 : 33。

        Returns:
            Sequence[ResponseMatchSchools]: 角色近期战绩记录.
        """
        return self.request(endpoint="/data/match/schools", mode=mode)

    @require_token
    def member_recruit(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        keyword: Annotated[
            str | None, "关键字，模糊匹配记录，用``=关键字``完全匹配记录"
        ] = None,
        table: Annotated[
            int,
            "指定表记录，``1``=``本服+跨服``，``2``=``本服``，``3``=``跨服``，默认值：``1``",
        ] = 1,
    ) -> Annotated[ResponseMemberRecruit, "团队招募信息"]:
        """
        member_recruit 团队招募

        团队招募信息

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，模糊匹配记录，用``=关键字``完全匹配记录。
            table (int, optional): 指定表记录，``1``=``本服+跨服``，``2``=``本服``，``3``=``跨服``，默认值：``1``。

        Returns:
            ResponseMemberRecruit: 团队招募信息。
        """
        return self.request(
            endpoint="/data/member/recruit", server=server, keyword=keyword, table=table
        )

    @require_token
    def member_teacher(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        keyword: Annotated[str | None, "关键字，查找该关键字的相关记录"] = None,
    ) -> Annotated[ResponseMemberTeacher, "师父列表"]:
        """
        member_teacher 师父列表

        客户端师徒系统

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，查找该关键字的相关记录。

        Returns:
            ResponseMemberTeacher: 师父列表。
        """
        return self.request(
            endpoint="/data/member/teacher", server=server, keyword=keyword
        )

    @require_token
    def member_student(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        keyword: Annotated[str | None, "关键字，查找该关键字的相关记录"] = None,
    ) -> Annotated[ResponseMemberStudent, "徒弟列表"]:
        """
        member_student 徒弟列表

        客户端师徒系统

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，查找该关键字的相关记录。

        Returns:
            ResponseMemberStudent: 徒弟列表。
        """
        return self.request(
            endpoint="/data/member/student", server=server, keyword=keyword
        )

    @require_token
    def server_sand(
        self, *, server: Annotated[str, "区服，查找该区服的相关记录"]
    ) -> Annotated[ResponseServerSand, "阵营沙盘信息"]:
        """
        server_sand 沙盘信息

        查看阵营沙盘信息。

        Args:
            server (str): 区服，查找该区服的相关记录。

        Returns:
            ResponseServerSand: 阵营沙盘信息。
        """
        return self.request(endpoint="/data/server/sand", server=server)

    @require_token
    def server_event(
        self,
        *,
        name: Annotated[str | None, "阵营名称，查找该阵营的相关记录"] = None,
        limit: Annotated[int, "限制查询结果的数量，默认值 100", 100],
    ) -> Annotated[Sequence[ResponseServerEvent], "全服阵营大事件"]:
        """
        server_event 阵营事件

        全服阵营大事件

        Args:
            name (str, optional): 阵营名称，查找该阵营的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 100。

        Returns:
            Sequence[ResponseServerEvent]: 全服阵营大事件。
        """
        return self.request(endpoint="/data/server/event", name=name, limit=limit)

    @require_token
    def trade_demon(
        self,
        *,
        server: Annotated[str | None, "指定区服，查找该区服的相关记录，可选"] = None,
        limit: Annotated[int, "限制查询结果的数量，默认值 10，可选"] = 10,
    ) -> Annotated[Sequence[ResponseTradeDemon], "金价比例信息"]:
        """
        trade_demon 金币比例

        金价比例信息

        Args:
            server (str, optional): 指定区服，查找该区服的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[ResponseTradeDemon]: 金价比例信息
        """
        return self.request(endpoint="/data/trade/demon", server=server, limit=limit)

    @require_token
    def trade_record(
        self,
        *,
        name: Annotated[str, "外观名称，查找该外观的记录"],
        server: Annotated[str | None, "区服，查找该区服的相关记录"] = None,
    ) -> Annotated[ResponseTradeRecord, "黑市物品价格统计"]:
        """
        trade_record 物品价格

        黑市物品价格统计

        Args:
            name (str): 外观名称，查找该外观的记录。
            server (str, optional): 区服，查找该区服的相关记录。

        Returns:
            ResponseTradeRecord: 黑市物品价格统计。
        """
        return self.request(endpoint="/data/trade/record", server=server, name=name)

    @require_token
    def tieba_item_records(
        self,
        *,
        server: Annotated[
            str, "区服，查找该区服的相关记录，默认值：``-`` 为全区服"
        ] = "-",
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 ``10``"] = 10,
    ) -> Annotated[Sequence[ResponseTiebaItemRecords], "来自贴吧的外观记录"]:
        """
        tieba_item_records 贴吧记录

        来自贴吧的外观记录。

        Args:
            server (str, optional): 区服，查找该区服的相关记录，默认值：``-`` 为全区服。
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 ``10``。

        Returns:
            Sequence[ResponseTiebaItemRecords]: 来自贴吧的外观记录。
        """
        return self.request(
            endpoint="/data/tieba/item/records", server=server, name=name, limit=limit
        )

    @require_token
    def valuables_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 20"] = 20,
    ) -> Annotated[Sequence[ResponseValuablesStatistical], "统计副本掉落的贵重物品"]:
        """
        valuables_statistical 掉落统计

        统计副本掉落的贵重物品。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 20。

        Returns:
            Sequence[ResponseValuablesStatistical]: 统计副本掉落的贵重物品。
        """
        return self.request(
            endpoint="/data/valuables/statistical",
            server=server,
            name=name,
            limit=limit,
        )

    @require_token
    def valuables_server_statistical(
        self,
        *,
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[
        Sequence[ResponseValuablesServerStatistical], "统计当前赛季副本掉落的特殊物品"
    ]:
        """
        valuables_server_statistical 全服掉落

        统计当前赛季副本掉落的特殊物品。

        Args:
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[ResponseValuablesServerStatistical]: 统计当前赛季副本掉落的特殊物品。
        """
        return self.request(
            endpoint="/data/valuables/server/statistical", name=name, limit=limit
        )

    @require_token
    def server_antivice(
        self, *, server: Annotated[str | None, "服务器"] = None
    ) -> Annotated[Sequence[ResponseServerAntivice], "诛恶事件历史记录(不允许轮询)"]:
        """
        server_antivice 诛恶事件

        诛恶事件历史记录(不允许轮询)

        Args:
            server (str, optional): 服务器。

        Returns:
            Sequence[ResponseServerAntivice]: 诛恶事件历史记录(不允许轮询)。
        """
        return self.request(endpoint="/data/server/antivice", server=server)

    @require_token
    def rank_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        table: Annotated[str, "榜单类型"],
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[Sequence[ResponseRankStatistical], "客户端战功榜与风云录"]:
        """
        rank_statistical 风云榜单

        客户端战功榜与风云录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            table (str): 榜单类型。
            name (str): 榜单名称。

        Returns:
            Sequence[ResponseRankStatistical]: 客户端战功榜与风云录。
        """
        return self.request(
            endpoint="/data/rank/statistical", server=server, table=table, name=name
        )

    @require_token
    def rank_server_statistical(
        self,
        *,
        table: Annotated[str, "榜单类型，个人/帮会/阵营/试炼"],
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[Sequence[ResponseRankServerStatistical], "客户端战功榜与风云录"]:
        """
        rank_server_statistical 全服榜单

        客户端战功榜与风云录。

        Args:
            table (str): 榜单类型，个人/帮会/阵营/试炼。
            name (str): 榜单名称。

        Returns:
            Sequence[ResponseRankServerStatistical]: 客户端战功榜与风云录。
        """
        return self.request(
            endpoint="/data/rank/server/statistical", table=table, name=name
        )

    @require_token
    @require_ticket
    def school_rank_statistical(
        self,
        *,
        school: Annotated[str, "门派简称，查找该心法的相关记录，默认值 : ALL"] = "ALL",
        server: Annotated[str, "指定区服，查找该区服的相关记录，默认值 : ALL"] = "ALL",
    ) -> Annotated[Sequence[ResponseSchoolRankStatistical], "游戏资历榜单"]:
        """
        school_rank_statistical 资历榜单

        游戏资历榜单

        Args:
            school (str, optional): 门派简称，查找该心法的相关记录，默认值 : ALL。
            server (str, optional): 指定区服，查找该区服的相关记录，默认值 : ALL。

        Returns:
            Sequence[ResponseSchoolRankStatistical]: 游戏资历榜单。
        """
        return self.request(
            endpoint="/data/school/rank/statistical", school=school, server=server
        )

    ##########
    # VIP II #
    ##########

    @require_token
    def active_monster(
        self,
    ) -> Annotated[ResponseActiveMonster, "本周百战异闻录刷新的首领以及特殊效果"]:
        """
        active_monster 百战首领

        本周百战异闻录刷新的首领以及特殊效果。

        Returns:
            ResponseActiveMonster: 本周百战异闻录刷新的首领以及特殊效果。
        """
        return self.request(endpoint="/data/active/monster")

    @require_token
    def horse_record(
        self, *, server: Annotated[str, "可选的服务器，查找该区服的相关记录"]
    ) -> Annotated[Sequence[ResponseHorseRecord], "客户端的卢刷新记录"]:
        """
        horse_record 的卢统计

        客户端的卢刷新记录。

        Args:
            server (str): 可选的服务器，查找该区服的相关记录。

        Returns:
            Sequence[ResponseHorseRecord]: 客户端的卢刷新记录。
        """
        return self.request(endpoint="/data/horse/record", server=server)

    @require_token
    def horse_ranch(
        self, *, server: Annotated[str, "区服，查找该区服的相关记录"]
    ) -> Annotated[ResponseHorseRanch, "客户端马场刷新记录"]:
        """
        horse_ranch 马场事件

        客户端马场刷新记录。

        Args:
            server (str): 区服，查找该区服的相关记录。

        Returns:
            ResponseHorseRanch: 客户端马场刷新记录。
        """
        return self.request(endpoint="/data/horse/ranch", server=server)

    def firework_record(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
    ) -> Annotated[
        Sequence[ResponseFireworkRecord], "烟花赠送与接收的历史记录，不保证遗漏"
    ]:
        """
        firework_record 烟花记录

        烟花赠送与接收的历史记录，不保证遗漏。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。

        Returns:
            Sequence[ResponseFireworkRecord]: 烟花赠送与接收的历史记录，不保证遗漏。
        """
        return self.request(endpoint="/data/firework/record", server=server, name=name)

    @require_token
    def firework_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "烟花名称，查找该烟花的相关统计"],
        limit: Annotated[int, "单页数量，设置返回的数量，默认值 : 20"] = 20,
    ) -> Annotated[Sequence[ResponseFireworkStatistical], "统计烟花记录"]:
        """
        firework_statistical 烟花统计

        统计烟花记录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 烟花名称，查找该烟花的相关统计。
            limit (int, optional): 单页数量，设置返回的数量，默认值 : 20。

        Returns:
            Sequence[ResponseFireworkStatistical]: 统计烟花记录。
        """
        return self.request(
            endpoint="/data/firework/statistical", server=server, name=name, limit=limit
        )

    @require_token
    def firework_collect(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        num: Annotated[int, "统计时间，默认值：7 天"] = 7,
    ) -> Annotated[Sequence[ResponseFireworkCollect], "汇总烟花记录"]:
        """
        firework_collect 烟花汇总

        汇总烟花记录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            num (int, optional): 统计时间，默认值：7 天。

        Returns:
            Sequence[ResponseFireworkCollect]: 汇总烟花记录。
        """
        return self.request(endpoint="/data/firework/collect", server=server, num=num)

    @require_token
    def firework_rank_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        column: Annotated[str, "可选范围：[sender recipient name]"],
        this_time: Annotated[int, "统计开始的时间，与结束的时间不得超过3个月"],
        that_time: Annotated[int, "统计结束的时间，与开始的时间不得超过3个月"],
    ) -> Annotated[Sequence[ResponseFireworkRankStatistical], "烟花赠送与接收的榜单"]:
        """
        firework_rank_statistical 烟花排行

        烟花赠送与接收的榜单。

        Args:
            server (str): 区服，查找该区服的相关记录。
            column (str): 可选范围：[sender recipient name]。
            this_time (int): 统计开始的时间，与结束的时间不得超过3个月。
            that_time (int): 统计结束的时间，与开始的时间不得超过3个月。

        Returns:
            Sequence[ResponseFireworkRankStatistical]: 烟花赠送与接收的榜单。
        """
        return self.request(
            endpoint="/data/firework/rank/statistical",
            server=server,
            column=column,
            this_time=this_time,
            that_time=that_time,
        )


class AsyncJX3API:
    def __init__(
        self,
        *,
        token: Annotated[str | None, "推栏 token"] = None,
        ticket: Annotated[str | None, "站点标识"] = None,
        base_url: str = "https://www.jx3api.com",
    ) -> None:
        if not token:
            logging.warning(
                "The `token` parameter is not specified, only the free API can be used."
            )

        self.token = token or os.getenv("JX3API_TOKEN")
        self.ticket = ticket or os.getenv("JX3API_TICKET")

        self.base_url = base_url

    async def request(self, *, endpoint: str, **kwargs) -> Any:
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
    def require_token(func: Callable[..., Any]) -> Callable[..., Any]:
        async def decorator(self, *args, **kwargs) -> Awaitable[Callable[..., Any]]:
            if not self.token:
                raise ValueError(
                    "The `token` parameter is not specified, only the free API can be used."
                )

            return await func(self, *args, **kwargs)

        return decorator

    @staticmethod
    def require_ticket(func: Callable[..., Any]) -> Callable[..., Any]:
        def decorator(self, *args, **kwargs) -> Awaitable[Callable[..., Any]]:
            if not self.ticket:
                raise ValueError("The `ticket` parameter must be specified.")

            return func(self, *args, **kwargs)

        return decorator

    ############
    # FREE API #
    ############

    async def active_calendar(
        self,
        *,
        server: Annotated[str | None, "区服名称，查找该区服的记录。"] = None,
        num: Annotated[
            int,
            "指定日期，查询指定日期的日常，默认值 : ``0`` 为当天，``1`` 为明天，以此类推。",
        ] = 0,
    ) -> Annotated[Awaitable[ResponseActiveCalendar], "今天、明天、后天、日常任务"]:
        """
        active_calendar 活动日历

        今天、明天、后天、日常任务。
        只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键对值。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。
            num (int, optional): 指定日期，查询指定日期的日常，默认值 : ``0`` 为当天，``1`` 为明天，以此类推。

        Returns:
            Awaitable[ResponseActiveCalendar]: 今天、明天、后天、日常任务。
        """
        return await self.request(
            endpoint="/data/active/calendar", server=server, num=num
        )

    async def active_list_calendar(
        self,
        *,
        num: Annotated[
            int, "预测时间，查询指定时间内的月历，默认值 : ``15`` 为前后15天的月历"
        ] = 15,
    ) -> Annotated[Awaitable[ResponseActiveListCalendar], "预测每天的日常任务"]:
        """
        active_list_calendar 活动月历

        预测每天的日常任务。
        只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键对值。

        Args:
            num (int, optional): 预测时间，查询指定时间内的月历，默认值 : ``15`` 为前后15天的月历。

        Returns:
            Awaitable[ResponseActiveListCalendar]: 预测每天的日常任务。
        """
        return await self.request(endpoint="/data/active/list/calendar", num=num)

    async def active_celebs(
        self,
        *,
        name: Annotated[str, "名称，查询指定事件的记录"],
    ) -> Annotated[
        Awaitable[Sequence[ResponseActiveCelebs]], "当前时间的楚天社/云从社进度"
    ]:
        """
        active_celebs 行侠事件

        当前时间的楚天社/云从社进度。

        Args:
            name (str): 名称，查询指定事件的记录。

        Returns:
            Awaitable[Sequence[ResponseActiveCelebs]]: 当前时间的楚天社/云从社进度。
        """
        return await self.request(endpoint="/data/active/celebs", name=name)

    async def exam_answer(
        self,
        *,
        subject: Annotated[str, "科举试题，支持首字母，支持模糊查询"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Awaitable[Sequence[ResponseExamAnswer]], "科举答题"]:
        """
        exam_answer 科举试题

        科举答题

        Args:
            subject (str): 科举试题，支持首字母，支持模糊查询。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Awaitable[Sequence[ResponseExamAnswer]]: 科举答题。
        """
        return await self.request(
            endpoint="/data/exam/answer", subject=subject, limit=limit
        )

    async def home_furniture(
        self,
        *,
        name: Annotated[str, "指定装饰，查找该装饰的详细记录"],
    ) -> Annotated[Awaitable[ResponseHomeFurniture], "装饰详情"]:
        """
        home_furniture 家园装饰

        装饰详情

        Args:
            name (str): 指定装饰，查找该装饰的详细记录。

        Returns:
            Awaitable[ResponseHomeFurniture]: 装饰详情。
        """
        return await self.request(endpoint="/data/home/furniture", name=name)

    async def home_travel(
        self,
        *,
        name: Annotated[str, "地图，查找该地图的装饰产出"],
    ) -> Annotated[Awaitable[Sequence[ResponseHomeTravel]], "器物谱地图产出装饰"]:
        """
        home_travel 器物图谱

        器物谱地图产出装饰

        Args:
            name (str): 地图，查找该地图的装饰产出。

        Returns:
            Awaitable[Sequence[ResponseHomeTravel]]: 器物谱地图产出装饰。
        """
        return await self.request(endpoint="/data/home/travel", name=name)

    async def news_allnews(
        self,
        *,
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Awaitable[Sequence[ResponseNewsAllnews]], "官方最新公告及新闻"]:
        """
        news_allnews 新闻资讯

        官方最新公告及新闻

        Args:
            limit (int, optional): 限制查询结果的数量，默认值 10.

        Returns:
            Awaitable[Sequence[ResponseNewsAllnews]]: 官方最新公告及新闻。
        """
        return await self.request(endpoint="/data/news/allnews", limit=limit)

    async def news_announce(
        self,
        *,
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Awaitable[Sequence[ResponseNewsAnnounce]], "官方最新维护公告"]:
        """
        news_announce 维护公告

        官方最新维护公告

        Args:
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Awaitable[Sequence[ResponseNewsAnnounce]]: 官方最新维护公告。
        """
        return await self.request(endpoint="/data/news/announce", limit=limit)

    async def server_master(
        self,
        *,
        name: Annotated[str, "指定区服，查找该区服的相关记录"],
    ) -> Annotated[Awaitable[ResponseServerMaster], "简称搜索主次服务器"]:
        """
        server_master 搜索区服

        简称搜索主次服务器

        Args:
            name (str): 指定区服，查找该区服的相关记录。

        Returns:
            Awaitable[ResponseServerMaster]: 简称搜索主次服务器。
        """
        return await self.request(endpoint="/data/server/master", name=name)

    async def server_check(
        self,
        *,
        server: Annotated[
            str | None,
            "可选的服务器名称，查找该区服的相关记录；未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)",
        ] = None,
    ) -> Annotated[Awaitable[ResponseServerCheck], "服务器当前状态 [ 已开服/维护中 ]"]:
        """
        server_check 开服检查

        服务器当前状态 [ 已开服/维护中 ]

        Args:
            server (str, optional): 可选的服务器名称，查找该区服的相关记录；未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)。

        Returns:
            Awaitable[ResponseServerCheck]: 服务器当前状态 [ 已开服/维护中 ]
        """
        return await self.request(endpoint="/data/server/check", server=server)

    async def server_status(
        self,
        *,
        server: Annotated[str, "指定区服，查找该区服的相关记录"],
    ) -> Annotated[Awaitable[ResponseServerStatus], "服务器当前状态"]:
        """
        server_status 查看状态

        服务器当前状态 [ 维护/正常/繁忙/爆满 ]

        Args:
            server (str): 指定区服，查找该区服的相关记录。

        Returns:
            Awaitable[ResponseServerStatus]: 服务器当前状态。
        """
        return await self.request(endpoint="/data/server/status", server=server)

    async def home_flower(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str | None, "鲜花，查找该鲜花的相关记录"] = None,
        map: Annotated[str | None, "地图，查找该地图的相关记录"] = None,
    ) -> Annotated[Awaitable[ResponseHomeFlower], "家园鲜花最高价格线路"]:
        """
        home_flower 鲜花价格

        家园鲜花最高价格线路。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str, optional): 鲜花，查找该鲜花的相关记录。
            map (str, optional): 地图，查找该地图的相关记录。

        Returns:
            Awaitable[ResponseHomeFlowerData]: 家园鲜花最高价格线路。
        """
        return await self.request(
            endpoint="/data/home/flower", server=server, name=name, map=map
        )

    ##########
    # VIP  I #
    ##########

    @require_token
    @require_ticket
    async def save_detailed(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        roleid: Annotated[str, "角色UID，保存该角色的详细记录"],
    ) -> Annotated[Awaitable[ResponseSaveDetailed], "自动更新角色信息"]:
        """
        save_detailed 角色更新

        自动更新角色信息。

        Args:
            server (str): 区服，查找该区服的相关记录。
            roleid (str): 角色UID，保存该角色的详细记录。

        Returns:
            Awaitable[ResponseSaveDetailed]: 自动更新角色信息。
        """
        return await self.request(
            endpoint="/data/save/detailed", server=server, roleid=roleid
        )

    @require_token
    @require_ticket
    async def role_detailed(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找目标角色的相关记录"],
    ) -> Annotated[Awaitable[ResponseRoleDetailed], "角色详细信息"]:
        """
        role_detailed 角色信息

        角色详细信息

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找目标角色的相关记录。

        Returns:
            Awaitable[ResponseRoleDetailed]: 角色详细信息。
        """
        return await self.request(
            endpoint="/data/role/detailed", server=server, name=name
        )

    @require_token
    async def school_matrix(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[Awaitable[ResponseSchoolMatrix], "职业阵眼效果"]:
        """
        school_matrix 阵眼效果

        职业阵眼效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            Awaitable[ResponseSchoolMatrix]: 职业阵眼效果。
        """
        return await self.request(endpoint="/data/school/matrix", name=name)

    @require_token
    async def school_force(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[Awaitable[Sequence[ResponseSchoolForce]], "奇穴详细效果"]:
        """
        school_force 奇穴效果

        奇穴详细效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            Awaitable[Sequence[ResponseSchoolForce]]: 奇穴详细效果。
        """
        return await self.request(endpoint="/data/school/force", name=name)

    @require_token
    async def school_skills(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[Awaitable[Sequence[ResponseSchoolSkills]], "技能详细效果"]:
        """
        school_skills 技能效果

        技能详细效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            Awaitable[Sequence[ResponseSchoolSkills]]: 技能详细效果。
        """
        return await self.request(endpoint="/data/school/skills", name=name)

    @require_token
    async def tieba_random(
        self,
        *,
        class_: Annotated[
            Literal[
                "818",
                "616",
                "鬼网三",
                "鬼网3",
                "树洞",
                "记录",
                "教程",
                "街拍",
                "故事",
                "避雷",
                "吐槽",
                "提问",
            ],
            "帖子分类",
        ],
        server: Annotated[
            str, "区服名称，查找该区服的相关记录，默认值：``-`` 为全区服"
        ] = "-",
        limit: Annotated[int, "限制查询结果的数量，默认值 ``10``"] = 10,
    ) -> Annotated[
        Awaitable[Sequence[ResponseTiebaRandom]], "随机搜索贴吧 : 818/616...."
    ]:
        """
        tieba_random 八卦帖子

        禁止轮询，随机搜索贴吧 : 818/616....

        Args:
            class (str): 帖子分类，可选范围：``818`` ``616`` ``鬼网三`` ``鬼网3`` ``树洞`` ``记录`` ``教程`` ``街拍`` ``故事`` ``避雷`` ``吐槽`` ``提问``
            server (str, optional): 区服名称，查找该区服的相关记录，默认值：``-`` 为全区服。
            limit (int, optional): 限制查询结果的数量，默认值 ``10``。

        Returns:
            Awaitable[Sequence[ResponseTiebaRandom]]: 随机搜索贴吧 : 818/616....
        """
        return await self.request(
            endpoint="/data/tieba/random", class_=class_, server=server, limit=limit
        )

    @require_token
    @require_ticket
    async def role_attribute(
        self, server: Annotated[str, "服务器"], name: Annotated[str, "角色名"]
    ) -> Awaitable[Dict]:
        """
        role_attribute 角色装备

        角色装备属性详情

        Args:
            server (Annotated[str, ): 服务器。
            name (Annotated[str,): 角色名。

        Returns:
            Awaitable[Dict]: 角色装备属性详情。
        """
        return await self.request(endpoint="/role/attribute", server=server, name=name)

    @require_token
    @require_ticket
    async def role_team_cd_list(
        self,
        *,
        server: Annotated[str, "区服名称，查找该区服的记录"],
        name: Annotated[str, "角色名称，查找该角色的记录"],
    ) -> Annotated[Awaitable[ResponseRoleTeamCdList], "角色副本记录"]:
        """
        role_team_cd_list 副本记录

        角色副本记录

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            Awaitable[ResponseRoleTeamCdList]: 角色副本记录。
        """
        return await self.request(
            endpoint="/data/role/teamCdList", server=server, name=name
        )

    @require_token
    @require_ticket
    async def luck_adventure(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
    ) -> Annotated[
        Awaitable[Sequence[ResponseLuckAdventure]], "角色奇遇触发记录(不保证遗漏)"
    ]:
        """
        luck_adventure 奇遇记录

        角色奇遇触发记录(不保证遗漏)

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。

        Returns:
            Awaitable[Sequence[ResponseLuckAdventure]]: 角色奇遇触发记录(不保证遗漏)。
        """
        return await self.request(
            endpoint="/data/luck/adventure", server=server, name=name
        )

    @require_token
    async def luck_statistical(
        self,
        *,
        server: Annotated[str, "区服名称，查找该区服的记录"],
        name: Annotated[str, "奇遇名称，查找该奇遇的记录"],
        limit: Annotated[int, "单页数量，单页返回的数量，默认值 : 20"] = 20,
    ) -> Annotated[Awaitable[Sequence[ResponseLuckStatistical]], "奇遇近期触发统计"]:
        """
        luck_statistical 奇遇统计

        奇遇近期触发统计

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 奇遇名称，查找该奇遇的记录。
            limit (int, optional): 单页数量，单页返回的数量，默认值 : 20。

        Returns:
            Awaitable[Sequence[ResponseLuckStatistical]]: 奇遇近期触发统计。
        """
        return await self.request(
            endpoint="/data/luck/statistical", server=server, name=name, limit=limit
        )

    @require_token
    async def luck_server_statistical(
        self,
        *,
        name: Annotated[str, "奇遇名称，查找该奇遇的全服统计"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[
        Awaitable[Sequence[ResponseLuckServerStatistical]],
        "统计全服近期奇遇记录，不区分区服",
    ]:
        """
        luck_server_statistical 全服统计

        统计全服近期奇遇记录，不区分区服。

        Args:
            name (str): 奇遇名称，查找该奇遇的全服统计。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Awaitable[Sequence[ResponseLuckServerStatistical]]: 统计全服近期奇遇记录，不区分区服。
        """
        return await self.request(
            endpoint="/data/luck/server/statistical", name=name, limit=limit
        )

    @require_token
    async def luck_collect(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        num: Annotated[int, "汇总时间，汇总指定天数内的记录，默认值 : 7"] = 7,
    ) -> Annotated[
        Awaitable[Sequence[ResponseLuckCollect]], "统计奇遇近期触发角色记录"
    ]:
        """
        luck_collect 奇遇汇总

        统计奇遇近期触发角色记录

        Args:
            server (str): 区服，查找该区服的相关记录。
            num (int, optional): 汇总时间，汇总指定天数内的记录，默认值 : 7。

        Returns:
            Awaitable[Sequence[ResponseLuckCollect]]: 统计奇遇近期触发角色记录。
        """
        return await self.request(endpoint="/data/luck/collect", server=server, num=num)

    async def role_achievement(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        role: Annotated[str, "角色名称，查找该角色的成就记录"],
        name: Annotated[str, "成就/系列名称，查询该成就/系列的完成进度"],
    ) -> Annotated[Awaitable[ResponseRoleAchievement], "角色成就进度"]:
        """
        role_achievement 成就百科

        角色成就进度

        Args:
            server (str): 区服，查找该区服的相关记录。
            role (str): 角色名称，查找该角色的成就记录。
            name (str): 成就/系列名称，查询该成就/系列的完成进度。

        Returns:
            Awaitable[ResponseRoleAchievement]: 角色成就进度。
        """
        return await self.request(
            endpoint="/data/role/achievement", server=server, role=role, name=name
        )

    @require_token
    @require_ticket
    async def match_recent(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
        mode: Annotated[int | None, "比赛模式，查找该模式的相关记录"] = None,
    ) -> Annotated[Awaitable[ResponseMatchRecent], "角色近期战绩记录"]:
        """
        match_recent 名剑战绩

        角色近期战绩记录

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。
            mode (int, optional): 比赛模式，查找该模式的相关记录。

        Returns:
            Awaitable[ResponseMatchRecent]: 角色近期战绩记录。
        """
        return await self.request(
            endpoint="/data/match/recent", server=server, name=name, mode=mode
        )

    @require_token
    @require_ticket
    async def match_awesome(
        self,
        *,
        mode: Annotated[int, "比赛模式，查找该模式的相关记录，默认值 : 33"] = 33,
        limit: Annotated[int, "限制查询结果的数量，默认值 20"] = 20,
    ) -> Annotated[Awaitable[Sequence[ResponseMatchAwesome]], "角色近期战绩记录"]:
        """
        match_awesome 名剑排行

        角色近期战绩记录。

        Args:
            mode (int, optional): 比赛模式，查找该模式的相关记录，默认值 : 33. Defaults to 33.
            limit (int, optional): 限制查询结果的数量，默认值 20。

        Returns:
            Awaitable[Sequence[ResponseMatchAwesome]]: 角色近期战绩记录。
        """
        return await self.request(
            endpoint="/data/match/awesome", mode=mode, limit=limit
        )

    @require_token
    @require_ticket
    async def match_schools(
        self,
        *,
        mode: Annotated[int, "比赛模式，查找该模式的相关记录，默认值 : 33"] = 33,
    ) -> Annotated[Awaitable[Sequence[ResponseMatchSchools]], "角色近期战绩记录"]:
        """
        match_schools 名剑统计

        角色近期战绩记录

        Args:
            mode (int, optional): 比赛模式，查找该模式的相关记录，默认值 : 33。

        Returns:
            Awaitable[Sequence[ResponseMatchSchools]]: 角色近期战绩记录.
        """
        return await self.request(endpoint="/data/match/schools", mode=mode)

    @require_token
    async def member_recruit(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        keyword: Annotated[
            str | None, "关键字，模糊匹配记录，用``=关键字``完全匹配记录"
        ] = None,
        table: Annotated[
            int,
            "指定表记录，``1``=``本服+跨服``，``2``=``本服``，``3``=``跨服``，默认值：``1``",
        ] = 1,
    ) -> Annotated[Awaitable[ResponseMemberRecruit], "团队招募信息"]:
        """
        member_recruit 团队招募

        团队招募信息

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，模糊匹配记录，用``=关键字``完全匹配记录。
            table (int, optional): 指定表记录，``1``=``本服+跨服``，``2``=``本服``，``3``=``跨服``，默认值：``1``。

        Returns:
            Awaitable[ResponseMemberRecruit]: 团队招募信息。
        """
        return await self.request(
            endpoint="/data/member/recruit", server=server, keyword=keyword, table=table
        )

    @require_token
    async def member_teacher(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        keyword: Annotated[str | None, "关键字，查找该关键字的相关记录"] = None,
    ) -> Annotated[Awaitable[ResponseMemberTeacher], "师父列表"]:
        """
        member_teacher 师父列表

        客户端师徒系统

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，查找该关键字的相关记录。

        Returns:
            Awaitable[ResponseMemberTeacher]: 师父列表。
        """
        return await self.request(
            endpoint="/data/member/teacher", server=server, keyword=keyword
        )

    @require_token
    async def member_student(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        keyword: Annotated[str | None, "关键字，查找该关键字的相关记录"] = None,
    ) -> Annotated[Awaitable[ResponseMemberStudent], "徒弟列表"]:
        """
        member_student 徒弟列表

        客户端师徒系统

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，查找该关键字的相关记录。

        Returns:
            Awaitable[ResponseMemberStudent]: 徒弟列表。
        """
        return await self.request(
            endpoint="/data/member/student", server=server, keyword=keyword
        )

    @require_token
    async def server_sand(
        self, *, server: Annotated[str, "区服，查找该区服的相关记录"]
    ) -> Annotated[Awaitable[ResponseServerSand], "阵营沙盘信息"]:
        """
        server_sand 沙盘信息

        查看阵营沙盘信息。

        Args:
            server (str): 区服，查找该区服的相关记录。

        Returns:
            Awaitable[ResponseServerSand]: 阵营沙盘信息。
        """
        return await self.request(endpoint="/data/server/sand", server=server)

    @require_token
    async def server_event(
        self,
        *,
        name: Annotated[str | None, "阵营名称，查找该阵营的相关记录"] = None,
        limit: Annotated[int, "限制查询结果的数量，默认值 100", 100],
    ) -> Annotated[Awaitable[Sequence[ResponseServerEvent]], "全服阵营大事件"]:
        """
        server_event 阵营事件

        全服阵营大事件

        Args:
            name (str, optional): 阵营名称，查找该阵营的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 100。

        Returns:
            Awaitable[Sequence[ResponseServerEvent]]: 全服阵营大事件。
        """
        return await self.request(endpoint="/data/server/event", name=name, limit=limit)

    @require_token
    async def trade_demon(
        self,
        *,
        server: Annotated[str | None, "指定区服，查找该区服的相关记录，可选"] = None,
        limit: Annotated[int, "限制查询结果的数量，默认值 10，可选"] = 10,
    ) -> Annotated[Awaitable[Sequence[ResponseTradeDemon]], "金价比例信息"]:
        """
        trade_demon 金币比例

        金价比例信息

        Args:
            server (str, optional): 指定区服，查找该区服的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[ResponseTradeDemon]: 金价比例信息
        """
        return await self.request(
            endpoint="/data/trade/demon", server=server, limit=limit
        )

    @require_token
    async def trade_record(
        self,
        *,
        name: Annotated[str, "外观名称，查找该外观的记录"],
        server: Annotated[str | None, "区服，查找该区服的相关记录"] = None,
    ) -> Annotated[Awaitable[ResponseTradeRecord], "黑市物品价格统计"]:
        """
        trade_record 物品价格

        黑市物品价格统计

        Args:
            name (str): 外观名称，查找该外观的记录。
            server (str, optional): 区服，查找该区服的相关记录。

        Returns:
            ResponseTradeRecord: 黑市物品价格统计。
        """
        return await self.request(
            endpoint="/data/trade/record", server=server, name=name
        )

    @require_token
    async def tieba_item_records(
        self,
        *,
        server: Annotated[
            str, "区服，查找该区服的相关记录，默认值：``-`` 为全区服"
        ] = "-",
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 ``10``"] = 10,
    ) -> Annotated[Awaitable[Sequence[ResponseTiebaItemRecords]], "来自贴吧的外观记录"]:
        """
        tieba_item_records 贴吧记录

        来自贴吧的外观记录。

        Args:
            server (str, optional): 区服，查找该区服的相关记录，默认值：``-`` 为全区服。
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 ``10``。

        Returns:
            Awaitable[Sequence[ResponseTiebaItemRecords]]: 来自贴吧的外观记录。
        """
        return await self.request(
            endpoint="/data/tieba/item/records", server=server, name=name, limit=limit
        )

    @require_token
    async def valuables_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 20"] = 20,
    ) -> Annotated[
        Awaitable[Sequence[ResponseValuablesStatistical]], "统计副本掉落的贵重物品"
    ]:
        """
        valuables_statistical 掉落统计

        统计副本掉落的贵重物品。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 20。

        Returns:
            Awaitable[Sequence[ResponseValuablesStatistical]]: 统计副本掉落的贵重物品。
        """
        return await self.request(
            endpoint="/data/valuables/statistical",
            server=server,
            name=name,
            limit=limit,
        )

    @require_token
    async def valuables_server_statistical(
        self,
        *,
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[
        Awaitable[Sequence[ResponseValuablesServerStatistical]],
        "统计当前赛季副本掉落的特殊物品",
    ]:
        """
        valuables_server_statistical 全服掉落

        统计当前赛季副本掉落的特殊物品。

        Args:
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Awaitable[Sequence[ResponseValuablesServerStatistical]]: 统计当前赛季副本掉落的特殊物品。
        """
        return await self.request(
            endpoint="/data/valuables/server/statistical", name=name, limit=limit
        )

    @require_token
    async def server_antivice(
        self, *, server: Annotated[str | None, "服务器"] = None
    ) -> Annotated[
        Awaitable[Sequence[ResponseServerAntivice]], "诛恶事件历史记录(不允许轮询)"
    ]:
        """
        server_antivice 诛恶事件

        诛恶事件历史记录(不允许轮询)

        Args:
            server (str, optional): 服务器。

        Returns:
            Awaitable[Sequence[ResponseServerAntivice]]: 诛恶事件历史记录(不允许轮询)。
        """
        return await self.request(endpoint="/data/server/antivice")

    @require_token
    async def rank_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        table: Annotated[str, "榜单类型"],
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[
        Awaitable[Sequence[ResponseRankStatistical]], "客户端战功榜与风云录"
    ]:
        """
        rank_statistical 风云榜单

        客户端战功榜与风云录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            table (str): 榜单类型。
            name (str): 榜单名称。

        Returns:
            Awaitable[Sequence[ResponseRankStatistical]]: 客户端战功榜与风云录。
        """
        return await self.request(
            endpoint="/data/rank/statistical", server=server, table=table, name=name
        )

    @require_token
    async def rank_server_statistical(
        self,
        *,
        table: Annotated[str, "榜单类型，个人/帮会/阵营/试炼"],
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[
        Awaitable[Sequence[ResponseRankServerStatistical]], "客户端战功榜与风云录"
    ]:
        """
        rank_server_statistical 全服榜单

        客户端战功榜与风云录。

        Args:
            table (str): 榜单类型，个人/帮会/阵营/试炼。
            name (str): 榜单名称。
            token (str): 站点标识，检查请求权限。

        Returns:
            Awaitable[Sequence[ResponseRankServerStatistical]]: 客户端战功榜与风云录。
        """
        return await self.request(
            endpoint="/data/rank/server/statistical", table=table, name=name
        )

    @require_token
    @require_ticket
    async def school_rank_statistical(
        self,
        *,
        school: Annotated[str, "门派简称，查找该心法的相关记录，默认值 : ALL"] = "ALL",
        server: Annotated[str, "指定区服，查找该区服的相关记录，默认值 : ALL"] = "ALL",
    ) -> Annotated[Awaitable[Sequence[ResponseSchoolRankStatistical]], "游戏资历榜单"]:
        """
        school_rank_statistical 资历榜单

        游戏资历榜单

        Args:
            school (str, optional): 门派简称，查找该心法的相关记录，默认值 : ALL。
            server (str, optional): 指定区服，查找该区服的相关记录，默认值 : ALL。

        Returns:
            Awaitable[Sequence[ResponseSchoolRankStatistical]]: 游戏资历榜单。
        """
        return await self.request(
            endpoint="/data/school/rank/statistical", school=school, server=server
        )

    ##########
    # VIP II #
    ##########

    @require_token
    async def active_monster(
        self,
    ) -> Annotated[
        Awaitable[ResponseActiveMonster], "本周百战异闻录刷新的首领以及特殊效果"
    ]:
        """
        active_monster 百战首领

        本周百战异闻录刷新的首领以及特殊效果。

        Returns:
            Awaitable[ResponseActiveMonster]: 本周百战异闻录刷新的首领以及特殊效果。
        """
        return await self.request(endpoint="/data/active/monster")

    @require_token
    async def horse_record(
        self, *, server: Annotated[str, "可选的服务器，查找该区服的相关记录"]
    ) -> Annotated[Awaitable[Sequence[ResponseHorseRecord]], "客户端的卢刷新记录"]:
        """
        horse_record 的卢统计

        客户端的卢刷新记录。

        Args:
            server (str): 可选的服务器，查找该区服的相关记录。

        Returns:
            Awaitable[Sequence[ResponseHorseRecord]]: 客户端的卢刷新记录。
        """
        return await self.request(endpoint="/data/horse/record", server=server)

    @require_token
    async def horse_ranch(
        self, *, server: Annotated[str, "区服，查找该区服的相关记录"]
    ) -> Annotated[Awaitable[ResponseHorseRanch], "客户端马场刷新记录"]:
        """
        horse_ranch 马场事件

        客户端马场刷新记录。

        Args:
            server (str): 区服，查找该区服的相关记录。

        Returns:
            Awaitable[ResponseHorseRanch]: 客户端马场刷新记录。
        """
        return await self.request(endpoint="/data/horse/ranch", server=server)

    @require_token
    async def firework_record(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
    ) -> Annotated[
        Awaitable[Sequence[ResponseFireworkRecord]],
        "烟花赠送与接收的历史记录，不保证遗漏",
    ]:
        """
        firework_record 烟花记录

        烟花赠送与接收的历史记录，不保证遗漏。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。

        Returns:
            Awaitable[Sequence[ResponseFireworkRecord]]: 烟花赠送与接收的历史记录，不保证遗漏。
        """
        return await self.request(
            endpoint="/data/firework/record", server=server, name=name
        )

    @require_token
    async def firework_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "烟花名称，查找该烟花的相关统计"],
        limit: Annotated[int, "单页数量，设置返回的数量，默认值 : 20"] = 20,
    ) -> Annotated[Awaitable[Sequence[ResponseFireworkStatistical]], "统计烟花记录"]:
        """
        firework_statistical 烟花统计

        统计烟花记录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 烟花名称，查找该烟花的相关统计。
            limit (int, optional): 单页数量，设置返回的数量，默认值 : 20。

        Returns:
            Awaitable[Sequence[ResponseFireworkStatistical]]: 统计烟花记录。
        """
        return await self.request(
            endpoint="/data/firework/statistical", server=server, name=name, limit=limit
        )

    @require_token
    async def firework_collect(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        num: Annotated[int, "统计时间，默认值：7 天"] = 7,
    ) -> Annotated[Awaitable[Sequence[ResponseFireworkCollect]], "汇总烟花记录"]:
        """
        firework_collect 烟花汇总

        汇总烟花记录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            num (int, optional): 统计时间，默认值：7 天。

        Returns:
            Awaitable[Sequence[ResponseFireworkCollect]]: 汇总烟花记录。
        """
        return await self.request(
            endpoint="/data/firework/collect", server=server, num=num
        )

    @require_token
    async def firework_rank_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        column: Annotated[str, "可选范围：[sender recipient name]"],
        this_time: Annotated[int, "统计开始的时间，与结束的时间不得超过3个月"],
        that_time: Annotated[int, "统计结束的时间，与开始的时间不得超过3个月"],
    ) -> Annotated[
        Awaitable[Sequence[ResponseFireworkRankStatistical]], "烟花赠送与接收的榜单"
    ]:
        """
        firework_rank_statistical 烟花排行

        烟花赠送与接收的榜单。

        Args:
            server (str): 区服，查找该区服的相关记录。
            column (str): 可选范围：[sender recipient name]。
            this_time (int): 统计开始的时间，与结束的时间不得超过3个月。
            that_time (int): 统计结束的时间，与开始的时间不得超过3个月。

        Returns:
            Awaitable[Sequence[ResponseFireworkRankStatistical]]: 烟花赠送与接收的榜单。
        """
        return await self.request(
            endpoint="/data/firework/rank/statistical",
            server=server,
            column=column,
            this_time=this_time,
            that_time=that_time,
        )

    #############
    # Websocket #
    #############

    @require_token
    async def socket(self) -> AsyncGenerator[Dict, None]:
        async with (
            aiohttp.ClientSession(
                headers={"token": token} if (token := self.token) else {}
            ) as session,
            session.ws_connect("wss://socket.nicemoe.cn") as ws,
        ):
            logging.info("websocket connected")

            async for msg in ws:
                if (data := json.loads(msg.data))["action"] == 10000:
                    logging.info(data["message"])
                    continue

                yield data
