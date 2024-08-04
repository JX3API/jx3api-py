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
    List,
    Literal,
    Sequence,
)
from urllib.parse import urljoin
from urllib.request import Request, urlopen

import aiohttp

from .exception import APIError
from .response import (
    ResponseActiveCalendar,
    ResponseActiveCelebrity,
    ResponseActiveListCalendar,
    ResponseExamAnswer,
    ResponseHomeFurniture,
    ResponseHomeTravel,
    ResponseNewsAllNews,
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
    format=(
        "[%(asctime)s][%(levelname)s]"
        "[%(module)s:%(funcName)s:%(lineno)d]: %(message)s"
    ),
)


class JX3API:
    def __init__(
        self,
        *,
        token: Annotated[str | None, "推栏 token"] = None,
        ticket: Annotated[str | None, "站点标识"] = None,
    ) -> None:
        self.token = token or os.getenv("JX3API_TOKEN")
        self.ticket = ticket or os.getenv("JX3API_TICKET")

        if not self.token:
            logging.warning(
                "The `token` parameter is not specified, only the free API can be used."
            )

    def request(self, *, endpoint: str, **kwargs) -> Any:
        logging.debug(f"requesting: {endpoint=}, {kwargs=}")

        kwargs["ticket"] = self.ticket

        req = Request(
            urljoin(base="https://www.jx3api.com", url=endpoint),
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
        server: Annotated[str | None, "区服名称"] = None,
        num: Annotated[int, "预测时间"] = 0,
    ) -> Annotated[ResponseActiveCalendar, "今天、明天、后天、日常任务"]:
        """
        active_calendar 活动日历

        今天、明天、后天、日常任务。
        只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键与值。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。
            num (int, optional): 预测时间，预测指定时间的日常，默认值: ``0`` 为当天，``1`` 为明天，以此类推。

        Returns:
            ResponseActiveCalendar: 今天、明天、后天、日常任务。
        """
        return self.request(endpoint="/data/active/calendar", server=server, num=num)

    def active_list_calendar(
        self, *, num: Annotated[int, "预测时间"] = 15
    ) -> Annotated[ResponseActiveListCalendar, "预测每天的日常任务"]:
        """
        active_list_calendar 活动月历

        预测每天的日常任务。
        只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键与值。

        Args:
            num (int, optional): 预测时间，预测指定时间范围内的活动，默认值 : ``15`` 为当天，``1`` 为明天。

        Returns:
            ResponseActiveListCalendar: 预测每天的日常任务。
        """
        return self.request(endpoint="/data/active/list/calendar", num=num)

    def active_celebrity(
        self, *, season: Annotated[int, "第几赛季"] = 2
    ) -> Annotated[Sequence[ResponseActiveCelebrity], "当前时间的楚天社/云从社进度"]:
        """
        active_celebrity 行侠事件

        当前时间的楚天社/云从社进度。

        Args:
            season (int, optional): 第几赛季，用于返回楚天社或云从社的判断条件，可选值：``1-3``。

        Returns:
            Sequence[ResponseActiveCelebrity]: 当前时间的楚天社/云从社进度。
        """
        return self.request(endpoint="/data/active/celebrity", season=season)

    def exam_answer(
        self,
        *,
        match: Annotated[str, "科举试题"],
        limit: Annotated[int, "设置返回的数量"] = 10,
    ) -> Sequence[ResponseExamAnswer]:
        """
        exam_answer 科举试题

        科举答案。

        Args:
            match (str): 科举试题，支持首字母，支持模糊查询。
            limit (int, optional): 设置返回的数量，默认值 ``10``。

        Returns:
            Sequence[ResponseExamAnswer]: 科举试题答案。
        """
        return self.request(endpoint="/data/exam/answer", match=match, limit=limit)

    def home_flower(
        self, *, server: str, name: str | None = None, map: str | None = None
    ) -> Dict:
        """
        home_flower 鲜花价格

        家园鲜花最高价格线路。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str, optional): 鲜花名称，查找该鲜花的记录。
            map (str, optional): 地图名称，查找该地图的记录。

        Returns:
            Dict: 鲜花价格。
        """
        return self.request(
            endpoint="/data/home/flower", server=server, name=name, map=map
        )

    def home_furniture(self, *, name: str) -> ResponseHomeFurniture:
        """
        home_furniture 家园装饰

        装饰详情。

        Args:
            name (str): 装饰名称，查找该装饰的详细记录。

        Returns:
            ResponseHomeFurniture: 装饰详情。
        """
        return self.request(endpoint="/data/home/furniture", name=name)

    def home_travel(self, *, name: str) -> Sequence[ResponseHomeTravel]:
        """
        home_travel 器物图谱

        器物谱地图产出装饰。

        Args:
            name (str, optional): 地图名称，查找该地图的家具。

        Returns:
            Sequence[ResponseHomeTravel]: 地图产出装饰。
        """
        return self.request(endpoint="/data/home/travel", name=name)

    def news_allnews(self, *, limit: int = 10) -> Sequence[ResponseNewsAllNews]:
        """
        news_allnews 新闻资讯

        官方最新公告及新闻。

        Args:
            limit (int, optional): 单页数量，设置返回的数量，默认值 ``10``。

        Returns:
            Sequence[ResponseNewsAllNews]: 官方最新公告及新闻
        """
        return self.request(endpoint="/data/news/allnews", limit=limit)

    def news_announce(self, *, limit: int = 10) -> List[Dict]:
        """
        news_announce 维护公告

        官方最新公告及新闻。

        Args:
            limit (int, optional): 单页数量，设置返回的数量，默认值 ``10``。

        Returns:
            List[Dict]: 官方最新公告及新闻。
        """
        return self.request(endpoint="/data/news/announce", limit=limit)

    def school_toxic(self, *, name: str) -> List[Dict]:
        """
        school_stoxic 小药清单

        推荐的小药清单。

        Args:
            name (str): 心法名称，查找该心法的记录。

        Returns:
            List[Dict]: 推荐的小药清单。
        """
        return self.request(endpoint="/data/school/toxic", name=name)

    def server_master(self, *, name: str) -> Dict:
        """
        server_master 搜索区服

        简称搜索主次服务器。

        Args:
            name (str): 区服名称，查找该区服的记录。

        Returns:
            Dict: 主次服务器信息。
        """
        return self.request(endpoint="/data/server/master", name=name)

    def server_check(self, *, server: str | None = None) -> Dict:
        """
        server_check 开服检查

        服务器当前状态 ``[ 已开服/维护中 ]``。
        未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)。
        刷新频率 : ``30`` 秒。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。

        Returns:
            Dict: 服务器当前状态 ```[ 维护/正常/繁忙/爆满 ]```。
        """
        return self.request(endpoint="/data/server/check", server=server)

    def server_status(self, *, server: str) -> Dict:
        """
        server_status 查看状态

        服务器当前状态 ```[ 维护/正常/繁忙/爆满 ]```。

        Args:
            server (str): 区服名称，查找该区服的记录。

        Returns:
            Dict: 服务器当前状态 ```[ 维护/正常/繁忙/爆满 ]```。
        """
        return self.request(endpoint="/data/server/status", server=server)

    #############
    # VIP I API #
    #############

    @require_token
    @require_ticket
    def save_detailed(self, *, server: str, roleId: str) -> Dict:
        """
        save_detailed 角色更新, 数据服务

        自动更新角色信息。

        Args:
            server (str): 区服名称，查找该区服的记录。
            roleId (str): 角色数字标识，查找该标识的记录。

        Returns:
            Dict: 角色信息。
        """
        return self.request(
            endpoint="/data/save/detailed", server=server, roleid=roleId
        )

    @require_token
    @require_ticket
    def role_detailed(self, *, server: str, name: str) -> Dict:
        """
        role_detailed 角色信息

        角色详细信息。

        Args:
            server (str): 区服名称，查找目标区服的记录。
            name (str): 角色名称，查找目标角色的记录。

        Returns:
            Dict: 角色详细信息。
        """
        return self.request(endpoint="/data/role/detailed", server=server, name=name)

    @require_token
    def school_matrix(self, *, name: str) -> Dict:
        """
        school_matrix 阵法效果

        职业阵眼效果。

        Args:
            name (str): 心法名称，查找该心法的记录。

        Returns:
            Dict: 职业阵眼效果。
        """
        return self.request(endpoint="/data/school/matrix", name=name)

    @require_token
    def school_force(self, *, name: str) -> List[Dict]:
        """
        school_force 奇穴效果

        奇穴详细效果。

        Args:
            name (str): 心法名称，查找该心法的记录。

        Returns:
            List[Dict]: 奇穴详细效果。
        """
        return self.request(endpoint="/data/school/force", name=name)

    @require_token
    def school_skills(self, *, name: str) -> List[Dict]:
        """
        school_skills 技能效果

        技能详细效果。

        Args:
            name (str): 心法名称，查找该心法的记录。

        Returns:
            List[Dict]: 技能详细信息。
        """
        return self.request(endpoint="/data/school/skills", name=name)

    @require_token
    def tieba_random(
        self, *, subclass: str, server: str | None = None, limit: int = 1
    ) -> List[Dict]:
        """
        tieba_random 八卦帖子

        禁止轮询，随机搜索贴吧: 818 / 616 。

        Args:
            subclass (str): 帖子分类，可选范围：``818`` ``616`` ``鬼网三`` ``鬼网3`` ``树洞`` ``记录`` ``教程`` ``街拍`` ``故事`` ``避雷`` ``吐槽`` ``提问``。
            server (str, optional): 区服名称，查找该区服的记录。
            limit (int, optional): 单页数量，单页返回的数量。

        Returns:
            List[Dict]: 该服务器随机选择的结果。
        """
        return self.request(
            endpoint="/data/tieba/random", subclass=subclass, server=server, limit=limit
        )

    @require_token
    @require_ticket
    def role_attribute(self, *, server: str, name: str) -> Dict:
        """
        role_attribute 装备属性

        角色装备属性详情。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            Dict: 装备属性详细信息。
        """
        return self.request(endpoint="/data/role/attribute", server=server, name=name)

    @require_token
    @require_ticket
    def role_teamcdlist(self, *, server: str, name: str) -> Dict:
        """
        role_teamcdlist 副本记录

        角色副本记录。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            Dict: 副本记录。
        """
        return self.request(endpoint="/data/role/teamCdList", server=server, name=name)

    @require_token
    def luck_adventure(self, *, server: str, name: str) -> List[Dict]:
        """
        luck_adventure 奇遇记录

        角色奇遇触发记录(不保证遗漏)。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            List[Dict]: 奇遇记录。
        """
        return self.request(endpoint="/data/luck/adventure", server=server, name=name)

    @require_token
    def luck_statistical(
        self, *, server: str, name: str, limit: int = 20
    ) -> List[Dict]:
        """
        luck_statistical 奇遇统计

        奇遇近期触发统计。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 奇遇名称，查找该奇遇的记录。
            limit (int, optional): 单页数量，单页返回的数量，默认值 : `20`。

        Returns:
            List[Dict]: 奇遇近期触发统计。
        """
        return self.request(
            endpoint="/data/luck/statistical", server=server, name=name, limit=limit
        )

    @require_token
    def luck_server_statistical(self, *, name: str, limit: int = 20) -> List[Dict]:
        """
        luck_server_statistical 全服统计

        统计全服近期奇遇记录，不区分区服。

        Args:
            name (str): 奇遇名称，查找该奇遇的全服统计。
            limit (int, optional): 单页数量，设置返回的数量，默认值: `20`。

        Returns:
            List[Dict]: 全服近期奇遇记录。
        """
        return self.request(
            endpoint="/data/luck/server/statistical", name=name, limit=limit
        )

    @require_token
    def luck_collect(self, *, server: str, num: int = 7) -> List[Dict]:
        """
        luck_collect 奇遇汇总

        统计奇遇近期触发角色记录。

        Args:
            server (str): 区服名称，查找该区服的记录。
            num (int, optional): 汇总时间，汇总指定天数内的记录，默认值: `7`。

        Returns:
            List[Dict]: 奇遇触发记录。
        """
        return self.request(endpoint="/data/luck/collect", server=server, num=num)

    @require_token
    @require_ticket
    def role_achievement(self, *, server: str, role: str, name: str) -> List[Dict]:
        """
        role_achievement 成就百科

        角色成就进度。

        Args:
            server (str): 区服名称，查找该区服的记录。
            role (str): 角色名称，查找该角色的记录。
            name (str): 成就/系列名称，查询该成就/系列的完成进度。

        Returns:
            List[Dict]: 角色成就进度。
        """
        return self.request(
            endpoint="/data/role/achievement", server=server, role=role, name=name
        )

    @require_token
    @require_ticket
    def match_recent(self, *, server: str, name: str, mode: int = 0) -> Dict:
        """
        match_recent 名剑战绩

        角色近期战绩记录。
        未输入比赛模式时，将返回推栏全部角色近期的比赛记录(推栏个人页面，会出现返回结果非指定角色数据)。
        根据 ``mode`` 参数请求返回不同的数据结构，最终数据以返回为准。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。
            mode (int, optional): 比赛模式，查找该模式的记录。

        Returns:
            Dict: 角色近期战绩记录。
        """
        return self.request(
            endpoint="/data/match/recent", server=server, name=name, mode=mode
        )

    @require_token
    @require_ticket
    def match_awesome(self, *, mode: int = 33, limit: int = 20) -> Dict:
        """
        match_awesome 名剑排行

        角色近期战绩记录。

        Args:
            mode (int, optional): 比赛模式，查找该模式的记录，默认值: `33`。
            limit (int, optional): 单页数量，设置返回的数量，默认值: `20`。

        Returns:
            Dict: 名剑排行。
        """
        return self.request(endpoint="/data/match/awesome", mode=mode, limit=limit)

    @require_token
    @require_ticket
    def match_schools(self, *, mode: int = 33) -> List[Dict]:
        """
        match_schools 名剑统计

        角色近期战绩记录。

        Args:
            mode (int, optional): 比赛模式，查找该模式的记录，默认值: `33`。

        Returns:
            List[Dict]: 角色近期战绩记录。
        """
        return self.request(endpoint="/data/match/schools", mode=mode)

    @require_token
    def member_recruit(
        self, *, server: str, keyword: str | None = None, table: int = 1
    ) -> Dict:
        """
        member_recruit 团队招募

        团队招募信息。

        Args:
            server (str): 区服名称，查找该区服的记录。
            keyword (str, optional): 关键字，模糊匹配记录，用`=关键字`完全匹配记录。
            table (int, optional): 指定表记录，`1`=`本服+跨服`，`2`=`本服`，`3`=`跨服`，默认值：`1`。

        Returns:
            Dict: 团队招募信息。
        """
        return self.request(
            endpoint="/data/member/recruit", server=server, keyword=keyword, table=table
        )

    @require_token
    def member_teacher(self, *, server: str, keyword: str | None = None) -> List[Dict]:
        """
        member_teacher 师父列表

        客户端师徒系统。

        Args:
            server (str): 区服名称，查找该区服的记录。
            keyword (str, optional): 关键字，查找该关键字的记录。

        Returns:
            List[Dict]: 师父列表。
        """
        return self.request(
            endpoint="/data/member/teacher", server=server, keyword=keyword
        )

    @require_token
    def member_student(self, *, server: str, keyword: str | None = None) -> List[Dict]:
        """
        member_student 徒弟列表

        客户端师徒系统。

        Args:
            server (str): 区服名称，查找该区服的记录。
            keyword (str, optional): 关键字，查找该关键字的记录。

        Returns:
            List[Dict]: 徒弟列表。
        """
        return self.request(
            endpoint="/data/member/student", server=server, keyword=keyword
        )

    @require_token
    def server_sand(self, *, server: str) -> Dict:
        """
        server_sand 沙盘信息

        查看阵营沙盘信息。

        Args:
            server (str): 区服名称，查找该区服的记录。

        Returns:
            Dict: 沙盘信息。
        """
        return self.request(endpoint="/data/server/sand", server=server)

    @require_token
    def server_event(self, *, limit: int = 100) -> List[Dict]:
        """
        server_event 阵营事件

        全服阵营大事件。

        Args:
            limit (int, optional): 单页数量，设置返回数量，默认值: 100。

        Returns:
            List[Dict]: 阵营事件详细列表。
        """
        return self.request(endpoint="/data/server/event", limit=limit)

    @require_token
    def trade_demon(self, *, server: str | None = None, limit: int = 10) -> List[Dict]:
        """
        trade_demon 金币比例

        金价比例信息。
        未输入区服名称或输入错误区服名称时，将返回全部区服的金币比例信息。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。
            limit (int, optional): 单页数量，设置返回的数量，默认值: ``10``。

        Returns:
            List[Dict]: 金币比例信息。
        """
        return self.request(endpoint="/data/trade/demon", server=server, limit=limit)

    @require_token
    def trade_record(self, name: str) -> Dict:
        """
        trade_record 物品价格

        黑市物品价格统计。

        Args:
            name (str): 外观名称，查找该外观的记录。

        Returns:
            Dict: 物品价格。
        """
        return self.request(endpoint="/data/trade/record", name=name)

    @require_token
    def tieba_item_records(
        self, *, name: str, server: str | None = "", limit: int = 1
    ) -> List[Dict]:
        """
        tieba_item_records 贴吧记录

        来自贴吧的外观记录。

        Args:
            name (str): 外观名称，查找该外观的记录。
            server (str, optional): 区服名称，查找该区服的记录，默认值：``-`` 为全区服。
            limit (int, optional): 单页数量，设置返回的数量，默认值：1。

        Returns:
            List[Dict]: 贴吧记录。
        """
        return self.request(
            endpoint="/data/tieba/item/records", server=server, name=name, limit=limit
        )

    @require_token
    def valuables_statistical(self, *, name: str, limit: int = 20) -> List[Dict]:
        """
        valuables_statistical 掉落统计

        统计副本掉落的贵重物品。

        Args:
            name (str): 物品名称，查找该物品的记录。
            limit (int, optional): 单页数量，设置返回的数量，默认值：`20`。

        Returns:
            List[Dict]: 贵重物品掉落记录。
        """
        return self.request(
            endpoint="/data/valuables/statistical", name=name, limit=limit
        )

    @require_token
    def valuables_server_statistical(self, *, name: str, limit: int = 30) -> List[Dict]:
        """
        valuables_server_statistical 全服掉落

        统计当前赛季副本掉落的特殊物品。

        Args:
            name (str): 物品名称，查找该物品的记录。
            limit (int, optional): 单页数量，设置返回的数量，默认值 : ``30``。

        Returns:
            List[Dict]: 全服掉落物品记录。
        """
        return self.request(
            endpoint="/data/valuables/server/statistical", name=name, limit=limit
        )

    @require_token
    def valuables_collect(self, *, server: str, num: int = 7) -> List[Dict]:
        """
        valuables_collect 掉落汇总

        副本掉落的特殊物品。

        Args:
            server (str): 区服名称，查找该区服的记录。
            num (int, optional): 统计范围，默认值 ``7`` 天。

        Returns:
            List[Dict]: 掉落汇总信息。
        """
        return self.request(endpoint="/data/valuables/collect", server=server, num=num)

    @require_token
    def server_antivice(self) -> List[Dict]:
        """
        server_antivice 诛恶事件

        诛恶事件历史记录。
        不允许轮询。

        Returns:
            List[Dict]: 诛恶事件历史记录。
        """
        return self.request(endpoint="/data/server/antivice")

    @require_token
    def rank_statistical(self, *, table: str, name: str, server: str) -> List[Dict]:
        """
        rank_statistical 风云榜单

        客户端战功榜与风云录。

        Args:
            table (str): 榜单类型。
            name (str): 榜单名称。
            server (str): 区服名称。

        Returns:
            List[Dict]: 风云榜单。
        """
        return self.request(
            endpoint="/data/rank/statistical", table=table, name=name, server=server
        )

    @require_token
    def rank_server_statistical(self, *, table: str, name: str) -> List[Dict]:
        """
        server_rank 全服榜单

        客户端战功榜与风云录

        Args:
            table (str): 榜单类型。
            name (str): 榜单名称。

        Returns:
            List[Dict]: 全服榜单。
        """
        return self.request(
            endpoint="/data/rank/server/statistical", table=table, name=name
        )

    @require_token
    @require_ticket
    def school_rank_statistical(
        self, *, school: str | None = "ALL", server: str | None = "ALL"
    ) -> List[Dict]:
        """
        rank_statistical 资历榜单

        游戏资历榜单。

        Args:
            school (str, optional): 门派简称，查找该心法的记录，默认值: ``ALL``。
            server (str, optional): 区服名称，查找该区服的记录，默认值: ``ALL``。

        Returns:
            List[Dict]: 游戏资历榜单。
        """
        return self.request(
            endpoint="/data/school/rank/statistical", school=school, server=server
        )

    @require_token
    def duowan_statistical(self, *, server: str | None = None) -> List[Dict]:
        """
        duowan_statistical 歪歪频道

        服务器的统战歪歪。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。

        Returns:
            List[Dict]: 歪歪频道信息。
        """
        return self.request(endpoint="/data/duowan/statistical", server=server)

    ##############
    # VIP II API #
    ##############

    @require_token
    def active_monster(self, *, token: str) -> Dict:
        """
        active_monster 百战首领

        本周百战异闻录刷新的首领以及特殊效果。

        Args:
            token (str): 站点标识，检查请求权限。

        Returns:
            Dict: 本周百战异闻录刷新的首领以及特殊效果。
        """
        return self.request(endpoint="/data/active/monster", token=token)

    @require_token
    def horse_ecords(self, *, server: str | None = None) -> List[Dict]:
        """
        horse_records 的卢统计

        客户端的卢刷新记录。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。

        Returns:
            List[Dict]: 的卢统计。
        """
        return self.request(endpoint="/data/horse/records", server=server)

    @require_token
    def horse_event(self, *, server: str) -> Dict:
        """
        horse_event 马场事件

        客户端马场刷新记录。

        Args:
            server (str): 区服名称，查找该区服的记录。

        Returns:
            Dict: 马场刷新记录。
        """
        return self.request(endpoint="/data/horse/event", server=server)

    @require_token
    def watch_record(self, *, server: str, name: str) -> List[Dict]:
        """
        watch_record 烟花记录

        烟花赠送与接收的历史记录，不保证遗漏。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            List[Dict]: 烟花记录。
        """
        return self.request(endpoint="/data/watch/record", server=server, name=name)

    @require_token
    def watch_statistical(
        self, *, server: str, name: str, limit: int = 20
    ) -> List[Dict]:
        """
        watch_statistical 烟花统计

        统计烟花记录。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 烟花名称，查找该烟花的记录。
            limit (int, optional): 单页数量，设置返回的数量。

        Returns:
            List[Dict]: 烟花统计记录。
        """
        return self.request(
            endpoint="/data/watch/statistical", server=server, name=name, limit=limit
        )

    @require_token
    def watch_collect(self, *, server: str, num: int = 7) -> List[Dict]:
        """
        watch_collect 烟花汇总

        汇总烟花记录。

        Args:
            server (str): 区服名称，查找该区服的记录。
            num (int, optional): 统计时间，默认值：7 天。

        Returns:
            List[Dict]: 烟花汇总记录。
        """
        return self.request(endpoint="/data/watch/collect", server=server, num=num)

    @require_token
    def watch_rank_statistical(
        self,
        *,
        server: str,
        column: Literal["sender", "recipient", "name"],
        this_time: int,
        that_time: int,
    ) -> List[Dict]:
        """
        rank_statistical 烟花排行

        烟花赠送与接收的榜单。

        Args:
            server (str): 区服名称，查找该区服的记录。
            column (str): 可选范围：[``sender`` ``recipient`` ``name``]。
            this_time (int): 统计开始的时间，与结束的时间不得超过3个月。
            that_time (int): 统计结束的时间，与开始的时间不得超过3个月。

        Returns:
            List[Dict]: 烟花排行信息。
        """
        return self.request(
            endpoint="/data/watch/rank/statistical",
            server=server,
            column=column,
            this_time=this_time,
            that_time=that_time,
        )

    ###########
    # VRF API #
    ###########

    @require_token
    def chat_mixed(self, *, name: str, text: str) -> Dict:
        """
        chat_mixed 智障聊天

        Args:
            name (str): 机器人的名称。
            text (str): 聊天的完整内容。

        Returns:
            Dict: 聊天的详细内容。
        """
        return self.request(endpoint="/data/chat/mixed", name=name, text=text)

    @require_token
    def music_tencent(self, *, name: str) -> List[Dict]:
        """
        music_tencent 腾讯音乐

        搜索腾讯音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找歌曲的编号。

        Returns:
            List[Dict]: 腾讯音乐编号信息。
        """
        return self.request(endpoint="/data/music/tencent", name=name)

    @require_token
    def music_netease(self, *, name: str) -> List[Dict]:
        """
        music_netease 网易音乐

        搜索网易云音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找该歌曲的编号。

        Returns:
            List[Dict]: 网易云音乐歌曲编号。
        """
        return self.request(endpoint="/data/music/netease", name=name)

    @require_token
    def music_kugou(self, *, name: str) -> Dict:
        """
        music_kugou 酷狗音乐

        搜索酷狗音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找该歌曲的编号。

        Returns:
            Dict: 酷狗音乐歌曲信息。
        """
        return self.request(endpoint="/data/music/kugou", name=name)

    @require_token
    def fraud_detail(self, *, uin: int) -> Dict:
        """
        fraud_detail 骗子记录

        搜索贴吧的行骗记录。

        Args:
            uin (int): 用户QQ号，查找是否存在行骗记录。

        Returns:
            Dict: 骗子记录。
        """
        return self.request(endpoint="/data/fraud/detail", uin=uin)

    def idiom_solitaire(self, *, name: str) -> Dict:
        """
        idiom_solitaire 成语接龙

        校对成语并返回相关成语

        Args:
            name (str): 查找对应词语。

        Returns:
            Dict: 成语及其信息
        """
        return self.request(endpoint="/data/idiom/solitaire", name=name)

    def saohua_random(self) -> Dict:
        """
        saohua_random 撩人骚话

        万花门派骚话。

        Returns:
            Dict: 骚话。
        """
        return self.request(endpoint="/data/saohua/random")

    def saohua_content(self) -> Dict:
        """
        saohua_content 舔狗日记

        召唤一条舔狗日记。

        Returns:
            Dict: 舔狗日记。
        """
        return self.request(endpoint="/data/saohua/content")

    def sound_converter(
        self,
        *,
        appkey: str,
        access: str,
        secret: str,
        text: str,
        voice: str = "Aitong",
        format: str = "mp3",
        sample_rate: int = 16000,
        volume: int = 50,
        speech_rate: int = 0,
        pitch_rate: int = 0,
    ) -> Dict:
        """
        converter 语音合成

        阿里云语音合成（TTS）。

        Args:
            appkey (str): 阿里云身份识别，`[点击申请](https://nls-portal.console.aliyun.com/overview)`。
            access (str): 阿里云身份识别，`[点击申请](https://usercenter.console.aliyun.com)`。
            secret (str): 阿里云身份识别，`[点击申请](https://usercenter.console.aliyun.com)`。
            text (str): 合成的内容。
            voice (str, optional): 发音人，默认值 `[Aitong]`，`[点击查看](https://help.aliyun.com/knowledge_detail/84435.html?spm=a2c4g.11186631.2.1.67045663WlpL4n)`。
            format (str, optional): 编码格式，范围 `[PCM][WAV][MP3]`，默认值 `[MP3]`。
            sample_rate (int, optional): 采样率，默认值 `[16000]`。
            volume (int, optional): 音量，范围 `[0～100]`，默认值 `[50]`。
            speech_rate (int, optional): 语速，范围 `[-500～500]`，默认值 `[0]`。
            pitch_rate (int, optional): 音调，范围 `[-500～500]`，默认值 `[0]`。

        Returns:
            Dict: 语音合成信息。
        """

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
    def __init__(self, *, token: str | None = None, ticket: str | None = None) -> None:
        if not token:
            logging.warning(
                "The `token` parameter is not specified, only the free API can be used."
            )

        self.token = token
        self.ticket = ticket

    async def request(self, *, endpoint: str, **kwargs) -> Any:
        logging.debug(f"requesting: {endpoint=}, {kwargs=}")

        kwargs["ticket"] = self.ticket

        async with aiohttp.request(
            "GET",
            urljoin(base="https://www.jx3api.com", url=endpoint),
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
        self, *, server: str | None = None, num: int = 0
    ) -> Annotated[Awaitable[ResponseActiveCalendar], "今天、明天、后天、日常任务"]:
        """
        active_calendar 活动日历

        今天、明天、后天、日常任务。
        只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键与值。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。
            num (int, optional): 预测时间，预测指定时间的日常，默认值: ``0`` 为当天，``1`` 为明天，以此类推。

        Returns:
            Awaitable[Dict]: 今天、明天、后天、日常任务。
        """
        return await self.request(
            endpoint="/data/active/calendar", server=server, num=num
        )

    async def active_list_calendar(
        self, *, num: int = 15
    ) -> Annotated[Awaitable[ResponseActiveListCalendar], "预测每天的日常任务"]:
        """
        active_list_calendar 活动月历

        预测每天的日常任务。
        只有 星期三、星期五、星期六、星期日 才有美人画图，星期三、星期五 才有世界首领，若非活动时间不返回相关键与值。

        Args:
            num (int, optional): 预测时间，预测指定时间范围内的活动，默认值 : ``15`` 为当天，``1`` 为明天。

        Returns:
            Awaitable[Dict]: 预测每天的日常任务。
        """
        return await self.request(endpoint="/data/active/list/calendar", num=num)

    async def active_celebrity(
        self, *, season: int = 2
    ) -> Annotated[
        Awaitable[Sequence[ResponseActiveCelebrity]], "当前时间的楚天社/云从社进度"
    ]:
        """
        active_celebrity 行侠事件

        当前时间的楚天社/云从社进度。

        Args:
            season (int, optional): 第几赛季，用于返回楚天社或云从社的判断条件，可选值：``1-3``。

        Returns:
            Awaitable[List[Dict]]: 当前时间的楚天社/云从社进度。
        """
        return await self.request(endpoint="/data/active/celebrity", season=season)

    async def exam_answer(
        self, *, match: str, limit: int = 10
    ) -> Awaitable[List[Dict]]:
        """
        exam_answer 科举试题

        科举答案。

        Args:
            match (str): 科举试题，支持首字母，支持模糊查询。
            limit (int, optional): 设置返回的数量，默认值 ``10``。

        Returns:
            Awaitable[List[Dict]]: 科举试题答案。
        """
        return await self.request(
            endpoint="/data/exam/answer", match=match, limit=limit
        )

    async def home_flower(
        self, *, server: str, name: str | None = None, map: str | None = None
    ) -> Awaitable[Dict]:
        """
        home_flower 鲜花价格

        家园鲜花最高价格线路。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str, optional): 鲜花名称，查找该鲜花的记录。
            map (str, optional): 地图名称，查找该地图的记录。

        Returns:
            Awaitable[Dict]: 鲜花价格。
        """
        return await self.request(
            endpoint="/data/home/flower", server=server, name=name, map=map
        )

    async def home_furniture(self, *, name: str) -> Awaitable[Dict]:
        """
        home_furniture 家园装饰

        装饰详情。

        Args:
            name (str): 装饰名称，查找该装饰的详细记录。

        Returns:
            Awaitable[Dict]: 装饰详情。
        """
        return await self.request(endpoint="/data/home/furniture", name=name)

    async def home_travel(self, *, name: str) -> Awaitable[List[Dict]]:
        """
        home_travel 器物图谱

        器物谱地图产出装饰。

        Args:
            name (str, optional): 地图名称，查找该地图的家具。

        Returns:
            Awaitable[List[Dict]]: 地图产出装饰。
        """
        return await self.request(endpoint="/data/home/travel", name=name)

    async def news_allnews(self, *, limit: int = 10) -> Awaitable[List[Dict]]:
        """
        news_allnews 新闻资讯

        官方最新公告及新闻。

        Args:
            limit (int, optional): 单页数量，设置返回的数量，默认值 ``10``。

        Returns:
            Awaitable[List[Dict]]: 官方最新公告及新闻
        """
        return await self.request(endpoint="/data/news/allnews", limit=limit)

    async def news_announce(self, *, limit: int = 10) -> Awaitable[List[Dict]]:
        """
        news_announce 维护公告

        官方最新公告及新闻。

        Args:
            limit (int, optional): 单页数量，设置返回的数量，默认值 ``10``。

        Returns:
            Awaitable[List[Dict]]: 官方最新公告及新闻。
        """
        return await self.request(endpoint="/data/news/announce", limit=limit)

    async def school_toxic(self, *, name: str) -> Awaitable[List[Dict]]:
        """
        school_stoxic 小药清单

        推荐的小药清单。

        Args:
            name (str): 心法名称，查找该心法的记录。

        Returns:
            Awaitable[List[Dict]]: 推荐的小药清单。
        """
        return await self.request(endpoint="/data/school/toxic", name=name)

    async def server_master(self, *, name: str) -> Awaitable[Dict]:
        """
        server_master 搜索区服

        简称搜索主次服务器。

        Args:
            name (str): 区服名称，查找该区服的记录。

        Returns:
            Awaitable[Dict]: 主次服务器信息。
        """
        return await self.request(endpoint="/data/server/master", name=name)

    async def server_check(self, *, server: str | None = None) -> Awaitable[Dict]:
        """
        server_check 开服检查

        服务器当前状态 ``[ 已开服/维护中 ]``。
        未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)。
        刷新频率 : ``30`` 秒。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。

        Returns:
            Awaitable[Dict]: 服务器当前状态 ```[ 维护/正常/繁忙/爆满 ]```。
        """
        return await self.request(endpoint="/data/server/check", server=server)

    async def server_status(self, *, server: str) -> Awaitable[Dict]:
        """
        server_status 查看状态

        服务器当前状态 ```[ 维护/正常/繁忙/爆满 ]```。

        Args:
            server (str): 区服名称，查找该区服的记录。

        Returns:
            Awaitable[Dict]: 服务器当前状态 ```[ 维护/正常/繁忙/爆满 ]```。
        """
        return await self.request(endpoint="/data/server/status", server=server)

    #############
    # VIP I API #
    #############

    @require_token
    @require_ticket
    async def save_detailed(self, *, server: str, roleId: str) -> Awaitable[Dict]:
        """
        save_detailed 角色更新, 数据服务

        自动更新角色信息。

        Args:
            server (str): 区服名称，查找该区服的记录。
            roleId (str): 角色数字标识，查找该标识的记录。

        Returns:
            Awaitable[Dict]: 角色信息。
        """
        return await self.request(
            endpoint="/data/save/detailed", server=server, roleid=roleId
        )

    @require_token
    @require_ticket
    async def role_detailed(self, *, server: str, name: str) -> Awaitable[Dict]:
        """
        role_detailed 角色信息

        角色详细信息。

        Args:
            server (str): 区服名称，查找目标区服的记录。
            name (str): 角色名称，查找目标角色的记录。

        Returns:
            Awaitable[Dict]: 角色详细信息。
        """
        return await self.request(
            endpoint="/data/role/detailed", server=server, name=name
        )

    @require_token
    async def school_matrix(self, *, name: str) -> Awaitable[Dict]:
        """
        school_matrix 阵法效果

        职业阵眼效果。

        Args:
            name (str): 心法名称，查找该心法的记录。

        Returns:
            Awaitable[Dict]: 职业阵眼效果。
        """
        return await self.request(endpoint="/data/school/matrix", name=name)

    @require_token
    async def school_force(self, *, name: str) -> Awaitable[List[Dict]]:
        """
        school_force 奇穴效果

        奇穴详细效果。

        Args:
            name (str): 心法名称，查找该心法的记录。

        Returns:
            Awaitable[List[Dict]]: 奇穴详细效果。
        """
        return await self.request(endpoint="/data/school/force", name=name)

    @require_token
    async def school_skills(self, *, name: str) -> Awaitable[List[Dict]]:
        """
        school_skills 技能效果

        技能详细效果。

        Args:
            name (str): 心法名称，查找该心法的记录。

        Returns:
            Awaitable[List[Dict]]: 技能详细信息。
        """
        return await self.request(endpoint="/data/school/skills", name=name)

    @require_token
    async def tieba_random(
        self, *, subclass: str, server: str | None = None, limit: int = 1
    ) -> Awaitable[List[Dict]]:
        """
        tieba_random 八卦帖子

        禁止轮询，随机搜索贴吧: 818 / 616 。

        Args:
            subclass (str): 帖子分类，可选范围：``818`` ``616`` ``鬼网三`` ``鬼网3`` ``树洞`` ``记录`` ``教程`` ``街拍`` ``故事`` ``避雷`` ``吐槽`` ``提问``。
            server (str, optional): 区服名称，查找该区服的记录。
            limit (int, optional): 单页数量，单页返回的数量。

        Returns:
            Awaitable[List[Dict]]: 该服务器随机选择的结果。
        """
        return await self.request(
            endpoint="/data/tieba/random", subclass=subclass, server=server, limit=limit
        )

    @require_token
    @require_ticket
    async def role_attribute(self, *, server: str, name: str) -> Awaitable[Dict]:
        """
        role_attribute 装备属性

        角色装备属性详情。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            Awaitable[Dict]: 装备属性详细信息。
        """
        return await self.request(
            endpoint="/data/role/attribute", server=server, name=name
        )

    @require_token
    @require_ticket
    async def role_teamcdlist(self, *, server: str, name: str) -> Awaitable[Dict]:
        """
        role_teamcdlist 副本记录

        角色副本记录。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            Awaitable[Dict]: 副本记录。
        """
        return await self.request(
            endpoint="/data/role/teamCdList", server=server, name=name
        )

    @require_token
    async def luck_adventure(self, *, server: str, name: str) -> Awaitable[List[Dict]]:
        """
        luck_adventure 奇遇记录

        角色奇遇触发记录(不保证遗漏)。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            Awaitable[List[Dict]]: 奇遇记录。
        """
        return await self.request(
            endpoint="/data/luck/adventure", server=server, name=name
        )

    @require_token
    async def luck_statistical(
        self, *, server: str, name: str, limit: int = 20
    ) -> Awaitable[List[Dict]]:
        """
        luck_statistical 奇遇统计

        奇遇近期触发统计。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 奇遇名称，查找该奇遇的记录。
            limit (int, optional): 单页数量，单页返回的数量，默认值 : `20`。

        Returns:
            Awaitable[List[Dict]]: 奇遇近期触发统计。
        """
        return await self.request(
            endpoint="/data/luck/statistical", server=server, name=name, limit=limit
        )

    @require_token
    async def luck_server_statistical(
        self, *, name: str, limit: int = 20
    ) -> Awaitable[List[Dict]]:
        """
        luck_server_statistical 全服统计

        统计全服近期奇遇记录，不区分区服。

        Args:
            name (str): 奇遇名称，查找该奇遇的全服统计。
            limit (int, optional): 单页数量，设置返回的数量，默认值: `20`。

        Returns:
            Awaitable[List[Dict]]: 全服近期奇遇记录。
        """
        return await self.request(
            endpoint="/data/luck/server/statistical", name=name, limit=limit
        )

    @require_token
    async def luck_collect(self, *, server: str, num: int = 7) -> Awaitable[List[Dict]]:
        """
        luck_collect 奇遇汇总

        统计奇遇近期触发角色记录。

        Args:
            server (str): 区服名称，查找该区服的记录。
            num (int, optional): 汇总时间，汇总指定天数内的记录，默认值: `7`。

        Returns:
            Awaitable[List[Dict]]: 奇遇触发记录。
        """
        return await self.request(endpoint="/data/luck/collect", server=server, num=num)

    @require_token
    @require_ticket
    async def role_achievement(
        self, *, server: str, role: str, name: str
    ) -> Awaitable[List[Dict]]:
        """
        role_achievement 成就百科

        角色成就进度。

        Args:
            server (str): 区服名称，查找该区服的记录。
            role (str): 角色名称，查找该角色的记录。
            name (str): 成就/系列名称，查询该成就/系列的完成进度。

        Returns:
            Awaitable[List[Dict]]: 角色成就进度。
        """
        return await self.request(
            endpoint="/data/role/achievement", server=server, role=role, name=name
        )

    @require_token
    @require_ticket
    async def match_recent(
        self, *, server: str, name: str, mode: int = 0
    ) -> Awaitable[Dict]:
        """
        match_recent 名剑战绩

        角色近期战绩记录。
        未输入比赛模式时，将返回推栏全部角色近期的比赛记录(推栏个人页面，会出现返回结果非指定角色数据)。
        根据 ``mode`` 参数请求返回不同的数据结构，最终数据以返回为准。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。
            mode (int, optional): 比赛模式，查找该模式的记录。

        Returns:
            Awaitable[Dict]: 角色近期战绩记录。
        """
        return await self.request(
            endpoint="/data/match/recent", server=server, name=name, mode=mode
        )

    @require_token
    @require_ticket
    async def match_awesome(
        self, *, mode: int = 33, limit: int = 20
    ) -> Awaitable[Dict]:
        """
        match_awesome 名剑排行

        角色近期战绩记录。

        Args:
            mode (int, optional): 比赛模式，查找该模式的记录，默认值: `33`。
            limit (int, optional): 单页数量，设置返回的数量，默认值: `20`。

        Returns:
            Awaitable[Dict]: 名剑排行。
        """
        return await self.request(
            endpoint="/data/match/awesome", mode=mode, limit=limit
        )

    @require_token
    @require_ticket
    async def match_schools(self, *, mode: int = 33) -> Awaitable[List[Dict]]:
        """
        match_schools 名剑统计

        角色近期战绩记录。

        Args:
            mode (int, optional): 比赛模式，查找该模式的记录，默认值: `33`。

        Returns:
            Awaitable[List[Dict]]: 角色近期战绩记录。
        """
        return await self.request(endpoint="/data/match/schools", mode=mode)

    @require_token
    async def member_recruit(
        self, *, server: str, keyword: str | None = None, table: int = 1
    ) -> Awaitable[Dict]:
        """
        member_recruit 团队招募

        团队招募信息。

        Args:
            server (str): 区服名称，查找该区服的记录。
            keyword (str, optional): 关键字，模糊匹配记录，用`=关键字`完全匹配记录。
            table (int, optional): 指定表记录，`1`=`本服+跨服`，`2`=`本服`，`3`=`跨服`，默认值：`1`。

        Returns:
            Awaitable[Dict]: 团队招募信息。
        """
        return await self.request(
            endpoint="/data/member/recruit", server=server, keyword=keyword, table=table
        )

    @require_token
    async def member_teacher(
        self, *, server: str, keyword: str | None = None
    ) -> Awaitable[List[Dict]]:
        """
        member_teacher 师父列表

        客户端师徒系统。

        Args:
            server (str): 区服名称，查找该区服的记录。
            keyword (str, optional): 关键字，查找该关键字的记录。

        Returns:
            Awaitable[List[Dict]]: 师父列表。
        """
        return await self.request(
            endpoint="/data/member/teacher", server=server, keyword=keyword
        )

    @require_token
    async def member_student(
        self, *, server: str, keyword: str | None = None
    ) -> Awaitable[List[Dict]]:
        """
        member_student 徒弟列表

        客户端师徒系统。

        Args:
            server (str): 区服名称，查找该区服的记录。
            keyword (str, optional): 关键字，查找该关键字的记录。

        Returns:
            Awaitable[List[Dict]]: 徒弟列表。
        """
        return await self.request(
            endpoint="/data/member/student", server=server, keyword=keyword
        )

    @require_token
    async def server_sand(self, *, server: str) -> Awaitable[Dict]:
        """
        server_sand 沙盘信息

        查看阵营沙盘信息。

        Args:
            server (str): 区服名称，查找该区服的记录。

        Returns:
            Awaitable[Dict]: 沙盘信息。
        """
        return await self.request(endpoint="/data/server/sand", server=server)

    @require_token
    async def server_event(self, *, limit: int = 100) -> Awaitable[List[Dict]]:
        """
        server_event 阵营事件

        全服阵营大事件。

        Args:
            limit (int, optional): 单页数量，设置返回数量，默认值: 100。

        Returns:
            Awaitable[List[Dict]]: 阵营事件详细列表。
        """
        return await self.request(endpoint="/data/server/event", limit=limit)

    @require_token
    async def trade_demon(
        self, *, server: str | None = None, limit: int = 10
    ) -> Awaitable[List[Dict]]:
        """
        trade_demon 金币比例

        金价比例信息。
        未输入区服名称或输入错误区服名称时，将返回全部区服的金币比例信息。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。
            limit (int, optional): 单页数量，设置返回的数量，默认值: ``10``。

        Returns:
            Awaitable[List[Dict]]: 金币比例信息。
        """
        return await self.request(
            endpoint="/data/trade/demon", server=server, limit=limit
        )

    @require_token
    async def trade_record(self, name: str) -> Awaitable[Dict]:
        """
        trade_record 物品价格

        黑市物品价格统计。

        Args:
            name (str): 外观名称，查找该外观的记录。

        Returns:
            Awaitable[Dict]: 物品价格。
        """
        return await self.request(endpoint="/data/trade/record", name=name)

    @require_token
    async def tieba_item_records(
        self, *, name: str, server: str | None = "", limit: int = 1
    ) -> Awaitable[List[Dict]]:
        """
        tieba_item_records 贴吧记录

        来自贴吧的外观记录。

        Args:
            name (str): 外观名称，查找该外观的记录。
            server (str, optional): 区服名称，查找该区服的记录，默认值：``-`` 为全区服。
            limit (int, optional): 单页数量，设置返回的数量，默认值：1。

        Returns:
            Awaitable[List[Dict]]: 贴吧记录。
        """
        return await self.request(
            endpoint="/data/tieba/item/records", server=server, name=name, limit=limit
        )

    @require_token
    async def valuables_statistical(
        self, *, name: str, limit: int = 20
    ) -> Awaitable[List[Dict]]:
        """
        valuables_statistical 掉落统计

        统计副本掉落的贵重物品。

        Args:
            name (str): 物品名称，查找该物品的记录。
            limit (int, optional): 单页数量，设置返回的数量，默认值：`20`。

        Returns:
            Awaitable[List[Dict]]: 贵重物品掉落记录。
        """
        return await self.request(
            endpoint="/data/valuables/statistical", name=name, limit=limit
        )

    @require_token
    async def valuables_server_statistical(
        self, *, name: str, limit: int = 30
    ) -> Awaitable[List[Dict]]:
        """
        valuables_server_statistical 全服掉落

        统计当前赛季副本掉落的特殊物品。

        Args:
            name (str): 物品名称，查找该物品的记录。
            limit (int, optional): 单页数量，设置返回的数量，默认值 : ``30``。

        Returns:
            Awaitable[List[Dict]]: 全服掉落物品记录。
        """
        return await self.request(
            endpoint="/data/valuables/server/statistical", name=name, limit=limit
        )

    @require_token
    async def valuables_collect(
        self, *, server: str, num: int = 7
    ) -> Awaitable[List[Dict]]:
        """
        valuables_collect 掉落汇总

        副本掉落的特殊物品。

        Args:
            server (str): 区服名称，查找该区服的记录。
            num (int, optional): 统计范围，默认值 ``7`` 天。

        Returns:
            Awaitable[List[Dict]]: 掉落汇总信息。
        """
        return await self.request(
            endpoint="/data/valuables/collect", server=server, num=num
        )

    @require_token
    async def server_antivice(self) -> Awaitable[List[Dict]]:
        """
        server_antivice 诛恶事件

        诛恶事件历史记录。
        不允许轮询。

        Returns:
            Awaitable[List[Dict]]: 诛恶事件历史记录。
        """
        return await self.request(endpoint="/data/server/antivice")

    @require_token
    async def rank_statistical(
        self, *, table: str, name: str, server: str
    ) -> Awaitable[List[Dict]]:
        """
        rank_statistical 风云榜单

        客户端战功榜与风云录。

        Args:
            table (str): 榜单类型。
            name (str): 榜单名称。
            server (str): 区服名称。

        Returns:
            Awaitable[List[Dict]]: 风云榜单。
        """
        return await self.request(
            endpoint="/data/rank/statistical", table=table, name=name, server=server
        )

    @require_token
    async def rank_server_statistical(
        self, *, table: str, name: str
    ) -> Awaitable[List[Dict]]:
        """
        server_rank 全服榜单

        客户端战功榜与风云录

        Args:
            table (str): 榜单类型。
            name (str): 榜单名称。

        Returns:
            Awaitable[List[Dict]]: 全服榜单。
        """
        return await self.request(
            endpoint="/data/rank/server/statistical", table=table, name=name
        )

    @require_token
    @require_ticket
    async def school_rank_statistical(
        self, *, school: str | None = "ALL", server: str | None = "ALL"
    ) -> Awaitable[List[Dict]]:
        """
        rank_statistical 资历榜单

        游戏资历榜单。

        Args:
            school (str, optional): 门派简称，查找该心法的记录，默认值: ``ALL``。
            server (str, optional): 区服名称，查找该区服的记录，默认值: ``ALL``。

        Returns:
            Awaitable[List[Dict]]: 游戏资历榜单。
        """
        return await self.request(
            endpoint="/data/school/rank/statistical", school=school, server=server
        )

    @require_token
    async def duowan_statistical(
        self, *, server: str | None = None
    ) -> Awaitable[List[Dict]]:
        """
        duowan_statistical 歪歪频道

        服务器的统战歪歪。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。

        Returns:
            Awaitable[List[Dict]]: 歪歪频道信息。
        """
        return await self.request(endpoint="/data/duowan/statistical", server=server)

    ##############
    # VIP II API #
    ##############

    @require_token
    async def active_monster(self, *, token: str) -> Awaitable[Dict]:
        """
        active_monster 百战首领

        本周百战异闻录刷新的首领以及特殊效果。

        Args:
            token (str): 站点标识，检查请求权限。

        Returns:
            Awaitable[Dict]: 本周百战异闻录刷新的首领以及特殊效果。
        """
        return await self.request(endpoint="/data/active/monster", token=token)

    @require_token
    async def horse_ecords(self, *, server: str | None = None) -> Awaitable[List[Dict]]:
        """
        horse_records 的卢统计

        客户端的卢刷新记录。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。

        Returns:
            Awaitable[List[Dict]]: 的卢统计。
        """
        return await self.request(endpoint="/data/horse/records", server=server)

    @require_token
    async def horse_event(self, *, server: str) -> Awaitable[Dict]:
        """
        horse_event 马场事件

        客户端马场刷新记录。

        Args:
            server (str): 区服名称，查找该区服的记录。

        Returns:
            Awaitable[Dict]: 马场刷新记录。
        """
        return await self.request(endpoint="/data/horse/event", server=server)

    @require_token
    async def watch_record(self, *, server: str, name: str) -> Awaitable[List[Dict]]:
        """
        watch_record 烟花记录

        烟花赠送与接收的历史记录，不保证遗漏。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            Awaitable[List[Dict]]: 烟花记录。
        """
        return await self.request(
            endpoint="/data/watch/record", server=server, name=name
        )

    @require_token
    async def watch_statistical(
        self, *, server: str, name: str, limit: int = 20
    ) -> Awaitable[List[Dict]]:
        """
        watch_statistical 烟花统计

        统计烟花记录。

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 烟花名称，查找该烟花的记录。
            limit (int, optional): 单页数量，设置返回的数量。

        Returns:
            Awaitable[List[Dict]]: 烟花统计记录。
        """
        return await self.request(
            endpoint="/data/watch/statistical", server=server, name=name, limit=limit
        )

    @require_token
    async def watch_collect(
        self, *, server: str, num: int = 7
    ) -> Awaitable[List[Dict]]:
        """
        watch_collect 烟花汇总

        汇总烟花记录。

        Args:
            server (str): 区服名称，查找该区服的记录。
            num (int, optional): 统计时间，默认值：7 天。

        Returns:
            Awaitable[List[Dict]]: 烟花汇总记录。
        """
        return await self.request(
            endpoint="/data/watch/collect", server=server, num=num
        )

    @require_token
    async def watch_rank_statistical(
        self,
        *,
        server: str,
        column: Literal["sender", "recipient", "name"],
        this_time: int,
        that_time: int,
    ) -> Awaitable[List[Dict]]:
        """
        rank_statistical 烟花排行

        烟花赠送与接收的榜单。

        Args:
            server (str): 区服名称，查找该区服的记录。
            column (str): 可选范围：[``sender`` ``recipient`` ``name``]。
            this_time (int): 统计开始的时间，与结束的时间不得超过3个月。
            that_time (int): 统计结束的时间，与开始的时间不得超过3个月。

        Returns:
            Awaitable[List[Dict]]: 烟花排行信息。
        """
        return await self.request(
            endpoint="/data/watch/rank/statistical",
            server=server,
            column=column,
            this_time=this_time,
            that_time=that_time,
        )

    ###########
    # VRF API #
    ###########

    @require_token
    async def chat_mixed(self, *, name: str, text: str) -> Awaitable[Dict]:
        """
        chat_mixed 智障聊天

        Args:
            name (str): 机器人的名称。
            text (str): 聊天的完整内容。

        Returns:
            Awaitable[Dict]: 聊天的详细内容。
        """
        return await self.request(endpoint="/data/chat/mixed", name=name, text=text)

    @require_token
    async def music_tencent(self, *, name: str) -> Awaitable[List[Dict]]:
        """
        music_tencent 腾讯音乐

        搜索腾讯音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找歌曲的编号。

        Returns:
            Awaitable[List[Dict]]: 腾讯音乐编号信息。
        """
        return await self.request(endpoint="/data/music/tencent", name=name)

    @require_token
    async def music_netease(self, *, name: str) -> Awaitable[List[Dict]]:
        """
        music_netease 网易音乐

        搜索网易云音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找该歌曲的编号。

        Returns:
            Awaitable[List[Dict]]: 网易云音乐歌曲编号。
        """
        return await self.request(endpoint="/data/music/netease", name=name)

    @require_token
    async def music_kugou(self, *, name: str) -> Awaitable[Dict]:
        """
        music_kugou 酷狗音乐

        搜索酷狗音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找该歌曲的编号。

        Returns:
            Awaitable[Dict]: 酷狗音乐歌曲信息。
        """
        return await self.request(endpoint="/data/music/kugou", name=name)

    @require_token
    async def fraud_detail(self, *, uin: int) -> Awaitable[Dict]:
        """
        fraud_detail 骗子记录

        搜索贴吧的行骗记录。

        Args:
            uin (int): 用户QQ号，查找是否存在行骗记录。

        Returns:
            Awaitable[Dict]: 骗子记录。
        """
        return await self.request(endpoint="/data/fraud/detail", uin=uin)

    async def idiom_solitaire(self, *, name: str) -> Awaitable[Dict]:
        """
        idiom_solitaire 成语接龙

        校对成语并返回相关成语

        Args:
            name (str): 查找对应词语。

        Returns:
            Awaitable[Dict]: 成语及其信息
        """
        return await self.request(endpoint="/data/idiom/solitaire", name=name)

    async def saohua_random(self) -> Awaitable[Dict]:
        """
        saohua_random 撩人骚话

        万花门派骚话。

        Returns:
            Awaitable[Dict]: 骚话。
        """
        return await self.request(endpoint="/data/saohua/random")

    async def saohua_content(self) -> Awaitable[Dict]:
        """
        saohua_content 舔狗日记

        召唤一条舔狗日记。

        Returns:
            Awaitable[Dict]: 舔狗日记。
        """
        return await self.request(endpoint="/data/saohua/content")

    async def sound_converter(
        self,
        *,
        appkey: str,
        access: str,
        secret: str,
        text: str,
        voice: str = "Aitong",
        format: str = "mp3",
        sample_rate: int = 16000,
        volume: int = 50,
        speech_rate: int = 0,
        pitch_rate: int = 0,
    ) -> Awaitable[Dict]:
        """
        converter 语音合成

        阿里云语音合成（TTS）。

        Args:
            appkey (str): 阿里云身份识别，`[点击申请](https://nls-portal.console.aliyun.com/overview)`。
            access (str): 阿里云身份识别，`[点击申请](https://usercenter.console.aliyun.com)`。
            secret (str): 阿里云身份识别，`[点击申请](https://usercenter.console.aliyun.com)`。
            text (str): 合成的内容。
            voice (str, optional): 发音人，默认值 `[Aitong]`，`[点击查看](https://help.aliyun.com/knowledge_detail/84435.html?spm=a2c4g.11186631.2.1.67045663WlpL4n)`。
            format (str, optional): 编码格式，范围 `[PCM][WAV][MP3]`，默认值 `[MP3]`。
            sample_rate (int, optional): 采样率，默认值 `[16000]`。
            volume (int, optional): 音量，范围 `[0～100]`，默认值 `[50]`。
            speech_rate (int, optional): 语速，范围 `[-500～500]`，默认值 `[0]`。
            pitch_rate (int, optional): 音调，范围 `[-500～500]`，默认值 `[0]`。

        Returns:
            Awaitable[Dict]: 语音合成信息。
        """

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
