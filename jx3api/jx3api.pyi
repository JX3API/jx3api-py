from collections.abc import Awaitable, Sequence
from typing import Annotated, NotRequired, TypedDict

class Response[T](TypedDict):
    code: int
    msg: str
    data: T
    time: int

class WebsocketResponse[T](TypedDict):
    action: int
    data: T

class ActiveWeekly(TypedDict):
    conn: Annotated[Sequence[str], "五人周常"]
    raid: Annotated[Sequence[str], "团队周常"]

class ActiveCalendar(TypedDict):
    date: Annotated[str, "日期"]
    week: Annotated[str, "星期"]
    war: Annotated[str, "大战"]
    battle: Annotated[str, "战场"]
    orecar: Annotated[str, "矿车活动"]
    rescue: Annotated[str, "驰援事件"]
    card: Annotated[Sequence[str], "名片掉落"]
    school: Annotated[str, "门派事件"]
    lucky: Annotated[Sequence[str], "宠物奇遇"]
    weekly: NotRequired[Annotated[ActiveWeekly, "周常活动"]]
    draw: NotRequired[Annotated[Sequence[str], "美人图"]]
    leader: NotRequired[Annotated[Sequence[str], "世界首领"]]

class ActiveCalendarToday(TypedDict):
    date: Annotated[str, "日期"]
    week: Annotated[str, "星期"]
    year: Annotated[str, "年"]
    month: Annotated[str, "月"]
    day: Annotated[str, "日"]

class ActiveCalendarItem(TypedDict):
    date: Annotated[str, "日期"]
    week: Annotated[str, "星期"]
    war: Annotated[str, "大战"]
    battle: Annotated[str, "战场"]
    orecar: Annotated[str, "矿车活动"]
    rescue: Annotated[str, "驰援事件"]
    card: Annotated[Sequence[str], "名片掉落"]
    school: Annotated[str, "门派事件"]
    lucky: Annotated[Sequence[str], "宠物奇遇"]
    draw: NotRequired[Annotated[Sequence[str], "美人图"]]
    leader: NotRequired[Annotated[Sequence[str], "世界首领"]]

class ActiveListCalendar(TypedDict):
    today: Annotated[ActiveCalendarToday, "当前日期"]
    total: Annotated[Sequence[ActiveCalendarItem], "日期区间活动"]

class ActiveCelebs(TypedDict):
    map: Annotated[str, "地图名称"]
    stage: Annotated[str, "事件阶段"]
    site: Annotated[str, "事件地点"]
    desc: Annotated[str, "事件描述"]
    icon: Annotated[str, "事件图标"]
    time: Annotated[str, "事件时间"]

class BattleRecord(TypedDict):
    declaringName: Annotated[str, "宣战帮会"]
    acceptingName: Annotated[str, "应战帮会"]
    startTime: Annotated[int, "开始时间"]
    durationSeconds: Annotated[int, "持续秒数"]
    endTime: Annotated[int | None, "结束时间"]
    winnerName: NotRequired[Annotated[str, "获胜帮会"]]
    winnerScore: NotRequired[Annotated[str, "获胜积分"]]

class DuowanChannel(TypedDict):
    sid: int
    users: int
    limit: int
    logo: int
    asid: int
    logoUrl: str
    campName: Annotated[str, "阵营名称"]
    snick: Annotated[str, "频道名称"]
    esid: NotRequired[str]

class DuowanStatistics(TypedDict):
    server: Annotated[str, "服务器名称"]
    data: Annotated[Sequence[DuowanChannel], "阵营频道"]

class ExamAnswer(TypedDict):
    question: Annotated[str, "试题"]
    answer: Annotated[str, "答案"]
    correctness: Annotated[int | None, "正确性"]
    index: Annotated[int, "结果序号"]

SchoolFood = TypedDict(
    "SchoolFood",
    {
        "school": Annotated[str, "门派"],
        "kungfu": Annotated[str, "心法"],
        "color": Annotated[str, "品质"],
        "class": Annotated[str, "食品或药品分类"],
        "name": Annotated[str, "名称"],
        "boost": Annotated[str, "增益类型"],
    },
)

class HomeFlowerItem(TypedDict):
    name: Annotated[str, "鲜花名称"]
    color: Annotated[str | None, "鲜花颜色"]
    price: Annotated[float, "价格"]
    line: Annotated[Sequence[str], "线路"]

class HomeFurniture(TypedDict):
    id: int
    name: str
    type: int
    color: int
    source: str
    architecture: int
    limit: int
    quality: int
    view: int
    practical: int
    hard: int
    geomantic: int
    interesting: int
    produce: str
    image: str
    tip: str

class HomeTravel(HomeFurniture): ...

class NewsRecord(TypedDict):
    catid: Annotated[str, "栏目编号"]
    date: Annotated[str, "发布日期"]
    title: Annotated[str, "标题"]
    type: Annotated[str, "新闻类型"]
    url: Annotated[str, "链接"]

class SaohuaContent(TypedDict):
    text: Annotated[str, "舔狗日志内容"]

class SaohuaRandom(TypedDict):
    text: Annotated[str, "随机骚话内容"]

class SaohuaContext(TypedDict):
    content: Annotated[str, "分类语录内容"]

class ServerCheck(TypedDict):
    zone: Annotated[str, "大区"]
    server: Annotated[str, "服务器"]
    status: Annotated[str, "状态"]

class SkillRework(TypedDict):
    id: Annotated[int, "公告编号"]
    title: Annotated[str, "公告标题"]
    url: Annotated[str, "公告链接"]
    time: Annotated[str, "发布时间"]

class SoundConverter(TypedDict):
    text: Annotated[str, "合成内容"]
    token: Annotated[str, "语音服务令牌"]
    url: Annotated[str, "音频地址"]

class ArenaPerformanceItem(TypedDict):
    mmr: int
    grade: int
    ranking: str
    winCount: int
    totalCount: int
    mvpCount: int
    pvpType: str
    winRate: int

ArenaRecentPerformance = TypedDict(
    "ArenaRecentPerformance",
    {
        "2v2": ArenaPerformanceItem,
        "3v3": ArenaPerformanceItem,
        "5v5": Sequence[dict],
    },
    total=False,
)

class ArenaRecentHistory(TypedDict):
    zone: str
    server: str
    avgGrade: int
    totalMmr: int
    mmr: int
    kungfu: str
    pvpType: int
    won: bool
    mvp: bool
    startTime: int
    endTime: int

class ArenaRecent(TypedDict):
    zoneName: str
    serverName: str
    roleName: str
    roleId: str
    globalId: str
    forceName: str
    forceId: int
    bodyName: str
    bodyId: int
    tongName: str
    tongId: int
    campName: str
    campId: int | str
    performance: ArenaRecentPerformance
    history: Sequence[ArenaRecentHistory]

class ArenaAwesome(TypedDict):
    zoneName: str
    serverName: str
    roleName: str
    forceName: str
    avatarUrl: str
    rankNum: str
    score: str
    upNum: str
    winRate: str

class ArenaSchools(TypedDict):
    name: Annotated[str, "门派名称"]
    this: Annotated[int, "本周统计"]
    last: Annotated[int, "上周统计"]

class EventLastRecord(TypedDict):
    name: Annotated[str, "角色名称"]
    time: Annotated[int, "触发时间"]

class EventCollect(TypedDict):
    zone: str
    server: str
    event: Annotated[str, "奇遇名称"]
    count: Annotated[int, "触发次数"]
    last: Annotated[EventLastRecord, "最近记录"]

class EventMissing(TypedDict):
    name: Annotated[str, "奇遇名称"]
    type: Annotated[str, "奇遇类型"]
    level: Annotated[int, "奇遇等级"]

class EventRecord(TypedDict):
    zone: str
    server: str
    name: Annotated[str, "角色名称"]
    event: Annotated[str, "奇遇名称"]
    status: int
    source: int
    time: int
    level: NotRequired[int]

class EventStrategy(TypedDict):
    box: int
    type: Annotated[str, "奇遇类型"]
    name: Annotated[str, "奇遇名称"]
    level: Annotated[int, "奇遇等级"]

class FraudRecord(TypedDict):
    tid: int
    author: str
    commented: bool
    content: str
    created: int
    pid: int
    status: int
    tieba: str
    title: str
    uid: int

class MechDecrypt(TypedDict):
    nowTime: str
    nowNode: str
    nowResult: str
    nextNode: str
    nextResult: str
    intervalTime: str

class MentorRecord(TypedDict):
    forceId: int
    mapId: int
    miniAvatorId: int
    roleId: int
    roleType: int
    tongId: int
    campId: int
    roleLevel: int
    tongMemberCount: int
    commentText: str
    roleName: str
    tongMasterName: str
    tongName: str

class RaidBossProgress(TypedDict):
    name: Annotated[str, "首领名称"]
    index: int
    progressId: int
    finished: bool

class RaidRecord(TypedDict):
    mapName: Annotated[str, "副本名称"]
    mapId: int
    bossCount: int
    bossFinished: int
    bossProgress: Sequence[RaidBossProgress]

class RanchRecords(TypedDict):
    zone: str
    server: str
    data: dict[str, Sequence[str]]
    note: str

class RankStatisticsItem(TypedDict):
    max_count: int
    now_count: int
    tong_name: str
    castle_name: str
    master_name: str
    total_score: int

class RankStatistics(TypedDict):
    id: int
    zone: str
    server: str
    name: str
    data: Sequence[RankStatisticsItem]
    time: int

class RankTrialsItem(TypedDict):
    max_level: int
    role_name: str
    equip_score: int
    total_score: int

class RankTrials(TypedDict):
    id: int
    zone: str
    server: str
    name: str
    data: Sequence[RankTrialsItem]
    time: int

class RecruitVariant(TypedDict):
    isSwitchServer: bool
    publisherId: int
    pushId: int
    roleId: int

class RecruitRecord(TypedDict):
    activityId: str
    activityName: str
    typeName: str
    subTypeName: str
    miniAvatarId: int
    createTime: int
    currentMemberCount: int
    maxMemberCount: int
    forceId: int
    lastModifyTime: int
    roleName: str
    roleType: int
    roleLevel: int
    kungfuId: int
    campId: int
    flagBits: int
    commentText: str
    labelIdTable: Sequence[int]
    labelIdComment: str
    variantInfo: RecruitVariant

class RewardRecord(TypedDict):
    zone: str
    server: str
    roleName: str
    mapName: str
    itemName: str
    itemAmount: int
    time: int

class RoleDetailed(TypedDict):
    zoneName: str
    serverName: str
    roleName: str
    roleId: str
    globalId: str
    forceName: str
    forceId: int
    bodyName: str
    bodyId: int
    tongName: str
    tongId: int
    campName: str
    campId: int

class SandRecord(TypedDict):
    tongId: int
    tongName: str
    castleId: int
    castleName: str
    masterId: int
    masterName: str
    campId: int
    campName: str
    ridePiece: int
    defendCount: int

class ServerSand(TypedDict):
    zone: str
    server: str
    reset: int
    update: int
    data: Sequence[SandRecord]

class SchoolMatrixDesc(TypedDict):
    desc: str
    level: int
    name: str

class SchoolMatrix(TypedDict):
    name: str
    skillName: str
    descs: Sequence[SchoolMatrixDesc]

SchoolTalentItem = TypedDict(
    "SchoolTalentItem",
    {
        "name": str,
        "class": int,
        "desc": str,
        "icon": str,
        "kind": str,
        "subKind": str,
    },
)

class SchoolTalent(TypedDict):
    level: int
    data: Sequence[SchoolTalentItem]

class SchoolSkillItem(TypedDict):
    name: str
    simpleDesc: str
    desc: str
    specialDesc: str
    interval: str
    consumption: str
    distance: str
    icon: str
    kind: str
    subKind: str
    releaseType: str
    weapon: str

SchoolSkills = TypedDict(
    "SchoolSkills",
    {"class": str, "data": Sequence[SchoolSkillItem]},
)

class SchoolSeniority(TypedDict):
    name: str
    role: str
    school: str
    server: str
    zone: str
    value: int
    avatar: str

class TiebaItemRecord(TypedDict):
    zone: str
    server: str
    name: str
    url: int
    context: str
    reply: int
    token: str
    floor: int
    time: int

TiebaRandom = TypedDict(
    "TiebaRandom",
    {
        "id": int,
        "class": str,
        "zone": str,
        "server": str,
        "name": str,
        "title": str,
        "url": int,
        "date": str,
    },
)

TradeDemon = TypedDict(
    "TradeDemon",
    {
        "zone": str,
        "server": str,
        "tieba": str,
        "wanbaolou": str,
        "dd373": str,
        "uu898": str,
        "5173": str,
        "7881": str,
        "date": str,
    },
)

class TradeItem(TypedDict):
    category: str
    name: str
    alias: str
    retail: int
    desc: str
    date: str
    view: str

class TradeSaleRecord(TypedDict):
    date: str
    sale: int
    server: str
    value: int
    zone: str

class TradeListingRecord(TypedDict):
    id: str
    index: str
    zone: str
    server: str
    value: int
    sale: int
    remainingTime: int
    token: str
    date: str
    source: int
    status: int

class TradeRecordGroup(TypedDict):
    name: str
    list: Sequence[TradeSaleRecord | TradeListingRecord]

class TradeRecords(TradeItem):
    list: Sequence[TradeRecordGroup]

class AuctionRecord(TypedDict):
    zone: str
    server: str
    roleName: str
    campName: str
    itemName: str
    itemAmount: str
    time: int

class CardRandom(TypedDict):
    zoneName: str
    serverName: str
    roleName: str
    roleId: str
    globalRoleId: str
    showHash: str
    showAvatar: str
    fileName: str

class CardCached(TypedDict):
    zoneName: str
    serverName: str
    roleName: str
    roleId: str
    globalRoleId: str
    showLike: int
    showHash: str
    showIndex: int
    showAvatar: str
    fileName: str
    cacheTime: int

class CardRecord(CardCached):
    showActive: bool

class CardHistory(TypedDict):
    zoneName: str
    serverName: str
    globalRoleId: str
    roleName: str
    fileName: str
    showHash: str
    showActive: bool
    showIndex: int
    showAvatar: str
    lastEditTime: int

class CastleRecord(TypedDict):
    zone: str
    server: str
    leader: str
    campName: str
    castle: str
    status: int
    statusText: str
    startTime: int
    endTime: int

class CastleStatus(TypedDict):
    server: str
    data: Sequence[CastleRecord]

class ChituRecord(TypedDict):
    id: int
    server: str
    map_name: str
    horse: str
    send: int
    date: str

class ChituWeekRecord(TypedDict):
    server: str
    map_name: str
    horse: str
    date: str

class FenxianRecord(TypedDict):
    campName: str
    fenxianName: str
    seizeTime: int
    friendName: str
    roleName: str

class FireworkRecord(TypedDict):
    time: int
    server: str
    sender: str
    receiver: str
    firework: str
    mapName: str
    matched: int
    status: int
    zone: str

class MonsterSkill(TypedDict):
    bDeprecated: bool
    dwInSkillID: int
    dwOutSkillID: int
    nColor: int
    nCost: int
    nLevel: int
    nSex: int
    szBoss: str
    szBossName: str
    szSkillName: str
    szType: str

class MonsterRecord(TypedDict):
    zone: str
    server: str
    roleName: str
    roleId: str
    globalId: str
    skillStamina: int
    skillEnergy: int
    skillCount: int
    skillList: Sequence[MonsterSkill]
    updateTime: int

class MonsterEffect(TypedDict):
    name: str
    list: Sequence[str]
    desc: str

class MonsterWeeklyItem(TypedDict):
    index: int
    name: str
    skill: Sequence[str]
    data: MonsterEffect

class MonsterWeekly(TypedDict):
    week: str
    start: int
    end: int
    boss: str
    list: Sequence[MonsterWeeklyItem]

RoleAchievementItem = TypedDict(
    "RoleAchievementItem",
    {
        "id": int,
        "icon": str,
        "likes": int,
        "name": str,
        "class": str,
        "subClass": str,
        "desc": str,
        "detail": str,
        "maps": Sequence[dict],
        "isFinished": bool,
        "isFav": bool,
        "type": str,
        "currentValue": int,
        "triggerValue": int,
        "subset": Sequence[dict],
        "rewardItem": str,
        "rewardPoint": int,
        "rewardPrefix": str,
        "rewardSuffix": str,
    },
    total=False,
)

class RoleAchievement(TypedDict, total=False):
    zoneName: str
    serverName: str
    roleName: str
    roleId: str | int
    globalRoleId: str | int
    forceName: str
    forceId: int
    bodyName: str
    bodyId: int
    tongName: str
    tongId: int
    campName: str
    campId: int
    personName: str
    personId: str
    personAvatar: str
    data: Sequence[RoleAchievementItem]

class SkillCalculate(TypedDict):
    duration: float
    hastePercent: float
    hastePercentLimit: float
    nowFrame: int
    uNowFrame: int
    surplusNowFrame: int
    level: int

class SteedRecord(TypedDict):
    zone: str
    server: str
    mapName: str
    refreshTime: int
    captureCampName: str
    captureRoleName: str
    captureTime: int
    auctionAmount: str
    auctionCampName: str
    auctionRoleName: str
    auctionTime: int

class TradePrice(TypedDict):
    lowestPrice: int
    avgPrice: int
    highestPrice: int
    sampleSize: int
    updatedAt: int

class TradeTip(TypedDict):
    text: str
    font: int
    color: str

class TradeManufactureTotal(TypedDict):
    subtotal: int
    lowestTotal: int
    avgTotal: int
    highestTotal: int

class TradeMaterial(TypedDict):
    type: str
    name: str
    quality: int
    genre: int | None
    iconId: int
    quantity: int
    price: TradePrice | int

class TradeManufacture(TypedDict):
    name: str
    level: int
    exp: int
    costVigor: int
    quality: int
    iconId: int
    createItemMin: int
    createItemMax: int
    createItemIndex: int
    tipInfo: Sequence[TradeTip]
    price: TradePrice
    total: TradeManufactureTotal
    items: Sequence[TradeMaterial]

class WickedRecord(TypedDict):
    zone: str
    server: str
    mapName: str
    time: int

class JX3API:
    def __init__(
        self,
        *,
        token: Annotated[str | None, "站点访问令牌"] = None,
        ticket: Annotated[str | None, "推栏标识鉴权"] = None,
        base_url: Annotated[str, "API 根地址"] = "https://www.jx3api.com",
        **kwargs,
    ) -> None: ...

    ##########
    # FREE  #
    ##########

    def active_calendar(
        self,
        *,
        num: Annotated[int, "天数偏移（单日）或区间半径（list）"] = 0,
        mode: Annotated[str, "'day' 单日 / 'list' 前后区间"] = "day",
    ) -> Annotated[ActiveCalendar | ActiveListCalendar, "活动日历"]:
        """
        活动日历

        单日或前后区间的日常活动推演

        Args:
            num (int): 天数偏移（单日）或区间半径（list）
            mode (str): 'day' 单日 / 'list' 前后区间

        Returns:
            ActiveCalendar | ActiveListCalendar: 活动日历
        """

    def active_celebs(
        self,
        *,
        name: Annotated[str, "事件名称"],
    ) -> Annotated[Sequence[ActiveCelebs], "地图活动"]:
        """
        地图活动

        楚天社 / 云从社 / 披风会接下来 10 条排期

        Args:
            name (str): 事件名称

        Returns:
            Sequence[ActiveCelebs]: 地图活动
        """

    def battle_records(
        self,
        *,
        server: Annotated[str, "查询信息"],
    ) -> Annotated[Sequence[BattleRecord], "帮战记录"]:
        """
        帮战记录

        查某服最近 30 场帮战，区分已结束 / 进行中并算出时长与结束时间

        Args:
            server (str): 查询信息

        Returns:
            Sequence[BattleRecord]: 帮战记录
        """

    def duowan_statistics(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Sequence[DuowanStatistics], "统战歪歪"]:
        """
        统战歪歪

        查各服 YY 语音频道的在线主播；指定服查该服两营，不指定则每服每营取一个代表

        Args:
            server (str | None): 服务器名称

        Returns:
            Sequence[DuowanStatistics]: 统战歪歪
        """

    def exam_search(
        self,
        *,
        subject: Annotated[str, "科举试题"],
        limit: Annotated[int, "返回数量"] = 10,
    ) -> Annotated[Sequence[ExamAnswer], "科举答案"]:
        """
        科举答案

        按题目或拼音模糊匹配，返回候选答案（原 question/pinyin LIKE 双查）

        Args:
            subject (str): 科举试题
            limit (int): 返回数量

        Returns:
            Sequence[ExamAnswer]: 科举答案
        """

    def food_list(
        self,
        *,
        name: Annotated[str | None, "心法名称"] = None,
    ) -> Annotated[Sequence[SchoolFood], "小吃小药"]:
        """
        小吃小药

        指定心法则返回该心法的小吃小药，否则返回全部

        Args:
            name (str | None): 心法名称

        Returns:
            Sequence[SchoolFood]: 小吃小药
        """

    def home_flower(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "鲜花名称"] = "",
        map: Annotated[str, "地图名称"] = "",
    ) -> Annotated[dict[str, Sequence[HomeFlowerItem]], "家园鲜花"]:
        """
        家园鲜花

        白名单校验后查推栏鲜花行情，按地图归组（鲜花名剥离括号色，括号内作 color）

        Args:
            server (str): 服务器名称
            name (str): 鲜花名称
            map (str): 地图名称

        Returns:
            dict[str, Sequence[HomeFlowerItem]]: 家园鲜花
        """

    def home_furniture(
        self,
        *,
        name: Annotated[str, "装饰名称"],
    ) -> Annotated[Sequence[HomeFurniture], "家园装饰"]:
        """
        家园装饰

        按装饰名查 travel 合集，补全图片链接

        Args:
            name (str): 装饰名称

        Returns:
            Sequence[HomeFurniture]: 家园装饰
        """

    def home_travel(
        self,
        *,
        name: Annotated[str, "器物名称"],
    ) -> Annotated[Sequence[HomeTravel], "器物图谱"]:
        """
        器物图谱

        按器物名查 travel 合集（produce 列），补全图片链接

        Args:
            name (str): 器物名称

        Returns:
            Sequence[HomeTravel]: 器物图谱
        """

    def news_announce(
        self,
        *,
        limit: Annotated[int, "显示数量"] = 10,
    ) -> Annotated[Sequence[NewsRecord], "维护公告"]:
        """
        维护公告

        标题含“版本更新”的公告，最新在前

        Args:
            limit (int): 显示数量

        Returns:
            Sequence[NewsRecord]: 维护公告
        """

    def news_records(
        self,
        *,
        limit: Annotated[int, "显示数量"] = 10,
    ) -> Annotated[Sequence[NewsRecord], "新闻资讯"]:
        """
        新闻资讯

        最新资讯列表；原 id DESC → _id DESC（导入按原 id 升序插入，等价于最新在前）

        Args:
            limit (int): 显示数量

        Returns:
            Sequence[NewsRecord]: 新闻资讯
        """

    def saohua_content(self) -> Annotated[SaohuaContent, "舔狗日志"]:
        """
        舔狗日志

        从舔狗日志库随机取一条

        Returns:
            SaohuaContent: 舔狗日志
        """

    def saohua_random(self) -> Annotated[SaohuaRandom, "随机骚话"]:
        """
        随机骚话

        从骚话库随机取一条

        Returns:
            SaohuaRandom: 随机骚话
        """

    def server_status_check(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[ServerCheck | Sequence[ServerCheck], "大区状态"]:
        """
        大区状态

        拉 xoyo 服务器列表（60 秒缓存）解析各服在线状态；指定服返回单条，否则返回收录的全部

        Args:
            server (str | None): 服务器名称

        Returns:
            ServerCheck | Sequence[ServerCheck]: 大区状态
        """

    def skill_rework(self) -> Annotated[Sequence[SkillRework], "技改记录"]:
        """
        技改记录

        拉 xoyo 公告列表（10 分钟缓存），筛出标题含「武学调整」的技改公告

        Returns:
            Sequence[SkillRework]: 技改记录
        """

    def sound_converter(
        self,
        *,
        appkey: Annotated[str, "阿里云 appkey"],
        access: Annotated[str, "AccessKeyId"],
        secret: Annotated[str, "AccessKeySecret"],
        voice: Annotated[str, "发音人"] = "Aitong",
        format: Annotated[str, "音频编码"] = "mp3",
        sample_rate: Annotated[int, "音频采样率"] = 16000,
        volume: Annotated[str, "音量"] = "50",
        speech_rate: Annotated[str, "语速"] = "0",
        pitch_rate: Annotated[str, "语调"] = "0",
        text: Annotated[str, "语音内容"],
    ) -> Annotated[SoundConverter, "语音合成"]:
        """
        语音合成

        用用户的阿里云密钥签名换取 Token，拼出 NLS TTS 流地址返回

        Args:
            appkey (str): 阿里云 appkey
            access (str): AccessKeyId
            secret (str): AccessKeySecret
            voice (str): 发音人
            format (str): 音频编码
            sample_rate (int): 音频采样率
            volume (str): 音量
            speech_rate (str): 语速
            pitch_rate (str): 语调
            text (str): 语音内容

        Returns:
            SoundConverter: 语音合成
        """

    ##########
    # VIP  1 #
    ##########

    def arena_awesome(
        self,
        *,
        mode: Annotated[int, "服务器名称"] = 33,
        limit: Annotated[int, "显示数量"] = 20,
    ) -> Annotated[Sequence[ArenaAwesome], "名剑排行"]:
        """
        名剑排行

        某比赛模式竞技场排行榜前 limit 名

        Args:
            mode (int): 服务器名称
            limit (int): 显示数量

        Returns:
            Sequence[ArenaAwesome]: 名剑排行
        """

    def arena_recent(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
        mode: Annotated[str, "比赛模式"] = 0,
    ) -> Annotated[ArenaRecent, "名剑战绩"]:
        """
        名剑战绩

        角色竞技场名片、各模式战绩表现、历史对战，指定模式时附趋势

        Args:
            server (str): 服务器名称
            name (str): 角色名称
            mode (str): 比赛模式

        Returns:
            ArenaRecent: 名剑战绩
        """

    def arena_schools(
        self,
        *,
        mode: Annotated[int, "比赛模式"] = 33,
    ) -> Annotated[Sequence[ArenaSchools], "名剑统计"]:
        """
        名剑统计

        某比赛模式下各门派的竞技场周统计

        Args:
            mode (int): 比赛模式

        Returns:
            Sequence[ArenaSchools]: 名剑统计
        """

    def event_collect(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        num: Annotated[int, "统计天数"] = 7,
    ) -> Annotated[Sequence[EventCollect], "奇遇汇总"]:
        """
        奇遇汇总

        白名单每个奇遇：最近 num 天在该服的触发次数 + 历史最新一条（角色名/时间）

        Args:
            server (str): 服务器名称
            num (int): 统计天数

        Returns:
            Sequence[EventCollect]: 奇遇汇总
        """

    def event_missing(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[Sequence[EventMissing], "未触发的"]:
        """
        未触发的

        返回该角色尚未触发的奇遇（不在全局 binding / 服务器 event 记录里的 event.master 项）

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            Sequence[EventMissing]: 未触发的
        """

    def event_recent(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        limit: Annotated[int, "显示数量"] = 20,
    ) -> Annotated[Sequence[EventRecord], "近期奇遇"]:
        """
        近期奇遇

        某服最近触发的奇遇事件，时间倒序

        Args:
            server (str): 服务器名称
            limit (int): 显示数量

        Returns:
            Sequence[EventRecord]: 近期奇遇
        """

    def event_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
        full: Annotated[int, "是否返回完整列表（含未触发）"] = 0,
    ) -> Annotated[Sequence[EventRecord], "奇遇记录"]:
        """
        奇遇记录

        整合角色全局事件(binding) + 服务器事件(event) + 魔盒成就，可补全未触发

        Args:
            server (str): 服务器名称
            name (str): 角色名称
            full (int): 是否返回完整列表（含未触发）

        Returns:
            Sequence[EventRecord]: 奇遇记录
        """

    def event_statistics(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        name: Annotated[str, "奇遇名称"],
        limit: Annotated[int, "显示数量"] = 20,
    ) -> Annotated[Sequence[EventRecord], "奇遇统计"]:
        """
        奇遇统计

        某奇遇最近的触发记录，时间倒序；指定服查单服，不指定查全服

        Args:
            server (str | None): 服务器名称
            name (str): 奇遇名称
            limit (int): 显示数量

        Returns:
            Sequence[EventRecord]: 奇遇统计
        """

    def event_strategy(
        self,
        *,
        name: Annotated[str, "奇遇名称"],
    ) -> Annotated[EventStrategy, "奇遇攻略"]:
        """
        奇遇攻略

        返回该奇遇的白名单配置（event.master + touch.master 合并）

        Args:
            name (str): 奇遇名称

        Returns:
            EventStrategy: 奇遇攻略
        """

    def fraud_detail(
        self,
        *,
        server: Annotated[str, "服务器名称"] = "",
        uid: Annotated[int, "角色 UID"],
    ) -> Annotated[Sequence[FraudRecord], "骗子查询"]:
        """
        骗子查询

        按 route 合集配置转发到远程风控服务，取该 UID 的详细记录

        Args:
            server (str): 服务器名称
            uid (int): 角色 UID

        Returns:
            Sequence[FraudRecord]: 骗子查询
        """

    def mech_decrypt(self) -> Annotated[MechDecrypt, "秘境方位"]:
        """
        秘境方位

        按 15 分钟档推算当前方位、下次变化时刻与倒计时

        Returns:
            MechDecrypt: 秘境方位
        """

    def mentor_search(
        self,
        *,
        label: Annotated[int, "师徒类型"] = 1,
        server: Annotated[str, "服务器大区"],
        keyword: Annotated[str | None, "关键字"] = None,
        limit: Annotated[int, "显示数量"] = 50,
    ) -> Annotated[Sequence[MentorRecord], "师徒列表"]:
        """
        师徒列表

        转发到远程取师徒名单，按关键字过滤评论，超量随机抽样

        Args:
            label (int): 师徒类型
            server (str): 服务器大区
            keyword (str | None): 关键字
            limit (int): 显示数量

        Returns:
            Sequence[MentorRecord]: 师徒列表
        """

    def raid_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[Sequence[RaidRecord], "副本记录"]:
        """
        副本记录

        转发到远程取该角色的团队副本 CD 列表

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            Sequence[RaidRecord]: 副本记录
        """

    def ranch_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        expired: Annotated[int, "是否包含已过期"] = 0,
    ) -> Annotated[RanchRecords, "马场事件"]:
        """
        马场事件

        jx3box 马场播报预告 + 本周期赤兔（mount）/ 的卢（steed）出世情况，附提示

        Args:
            server (str): 服务器名称
            expired (int): 是否包含已过期

        Returns:
            RanchRecords: 马场事件
        """

    def rank_statistics(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[RankStatistics, "排行统计"]:
        """
        排行统计

        指定服查该服该榜单，否则查全服该榜单

        Args:
            server (str | None): 服务器名称
            name (str): 榜单名称

        Returns:
            RankStatistics: 排行统计
        """

    def rank_trials(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[RankTrials, "试炼之地"]:
        """
        试炼之地

        同榜单查询，山居剑意归并到藏剑；行是位置字段 1~4，重建成具名字段

        Args:
            server (str | None): 服务器名称
            name (str): 榜单名称

        Returns:
            RankTrials: 试炼之地
        """

    def recruit_search(
        self,
        *,
        server: Annotated[str, "服务器大区"],
        label: Annotated[int, "服务类型"] = 1,
        keyword: Annotated[str | None, "关键字"] = None,
        limit: Annotated[int, "显示数量"] = 50,
    ) -> Annotated[Sequence[RecruitRecord], "团队招募"]:
        """
        团队招募

        转发远程取招募名单，按关键字（活动/团长/内容）过滤，超量截断

        Args:
            server (str): 服务器大区
            label (int): 服务类型
            keyword (str | None): 关键字
            limit (int): 显示数量

        Returns:
            Sequence[RecruitRecord]: 团队招募
        """

    def reward_statistics(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        name: Annotated[str, "物品名称"],
        limit: Annotated[int, "显示数量"] = 20,
    ) -> Annotated[Sequence[RewardRecord], "掉落统计"]:
        """
        掉落统计

        按物品名模糊匹配掉落记录，时间倒序；指定服查单服，不指定查全服

        Args:
            server (str | None): 服务器名称
            name (str): 物品名称
            limit (int): 显示数量

        Returns:
            Sequence[RewardRecord]: 掉落统计
        """

    def role_detail(
        self,
        *,
        server: Annotated[str, "服务器大区"],
        name: Annotated[str, "角色名称"],
        history: Annotated[int, "是否返回改名 / 帮会历史"] = 0,
    ) -> Annotated[RoleDetailed, "角色详情"]:
        """
        角色详情

        角色名片（roles 合集）；每次都采集 ermaozi 历史去重入库以持续收录 history=1：同步先采集再返回最新历史；history=0：采集甩到响应之后异步跑，客户端零等待

        Args:
            server (str): 服务器大区
            name (str): 角色名称
            history (int): 是否返回改名 / 帮会历史

        Returns:
            RoleDetailed: 角色详情
        """

    def sand_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
    ) -> Annotated[ServerSand, "沙盘据点"]:
        """
        沙盘据点

        各据点归属帮会 / 阵营 + 本周被献祭（防守）次数

        Args:
            server (str): 服务器名称

        Returns:
            ServerSand: 沙盘据点
        """

    def school_matrix(
        self,
        *,
        name: Annotated[str, "职业名称"],
    ) -> Annotated[SchoolMatrix, "阵眼效果"]:
        """
        阵眼效果

        按心法取推栏阵眼（阵法）效果与描述

        Args:
            name (str): 职业名称

        Returns:
            SchoolMatrix: 阵眼效果
        """

    def school_seniority(
        self,
        *,
        server: Annotated[str, "服务器名称"] = "ALL",
        school: Annotated[str, "门派名称"] = "ALL",
    ) -> Annotated[Sequence[SchoolSeniority], "资历榜单"]:
        """
        资历榜单

        指定服 / 门派（默认全服全门派）的资历前 100 名，补门派名

        Args:
            server (str): 服务器名称
            school (str): 门派名称

        Returns:
            Sequence[SchoolSeniority]: 资历榜单
        """

    def school_skills(
        self,
        *,
        name: Annotated[str, "门派名称"],
        update: Annotated[int, "是否更新"] = 0,
    ) -> Annotated[Sequence[SchoolSkills], "技能信息"]:
        """
        技能信息

        按心法取推栏各分类（remark）下的招式技能

        Args:
            name (str): 门派名称
            update (int): 是否更新

        Returns:
            Sequence[SchoolSkills]: 技能信息
        """

    def school_talent(
        self,
        *,
        name: Annotated[str, "门派名称"],
        update: Annotated[int, "是否更新"] = 0,
    ) -> Annotated[Sequence[SchoolTalent], "奇穴信息"]:
        """
        奇穴信息

        按心法取推栏各等级的招式（class=1）/ 奇穴（class=0）技能，按等级升序

        Args:
            name (str): 门派名称
            update (int): 是否更新

        Returns:
            Sequence[SchoolTalent]: 奇穴信息
        """

    def tieba_item_records(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        name: Annotated[str, "物品名称"],
        limit: Annotated[int, "返回数量"] = 10,
    ) -> Annotated[Sequence[TiebaItemRecord], "外观记录"]:
        """
        外观记录

        在贴吧楼层（search.floor）里按物品名搜相关帖子（正则 + 分词兜底）

        Args:
            server (str | None): 服务器名称
            name (str): 物品名称
            limit (int): 返回数量

        Returns:
            Sequence[TiebaItemRecord]: 外观记录
        """

    def tieba_random(
        self,
        *,
        tags: Annotated[str, "帖子类型"],
        server: Annotated[str | None, "服务器名称"] = None,
        limit: Annotated[int, "返回数量"] = 10,
    ) -> Annotated[Sequence[TiebaRandom], "百度贴吧"]:
        """
        百度贴吧

        按帖子类型随机取近 31 天的帖子（seasun.tieba），可选指定服

        Args:
            tags (str): 帖子类型
            server (str | None): 服务器名称
            limit (int): 返回数量

        Returns:
            Sequence[TiebaRandom]: 百度贴吧
        """

    def trade_demon(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        limit: Annotated[int, "显示数量"] = 10,
    ) -> Annotated[Sequence[TradeDemon], "金价行情"]:
        """
        金价行情

        各渠道金币比价（search.price）；指定服返回该服最近 limit 条，否则每服最新一条

        Args:
            server (str | None): 服务器名称
            limit (int): 显示数量

        Returns:
            Sequence[TradeDemon]: 金价行情
        """

    def trade_item_records(
        self,
        *,
        name: Annotated[str, "物品名称"],
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[TradeRecords, "外观价格"]:
        """
        外观价格

        精确定位外观（search.main）后取各区/指定服历史成交 + 万宝楼两期挂单

        Args:
            name (str): 物品名称
            server (str | None): 服务器名称

        Returns:
            TradeRecords: 外观价格
        """

    def trade_item_search(
        self,
        *,
        name: Annotated[str, "物品名称"],
    ) -> Annotated[Sequence[TradeItem], "外观搜索"]:
        """
        外观搜索

        按名称查外观（search.main）；先精确 name/alias/feiniu，无则模糊 name/alias/allalias/feiniu

        Args:
            name (str): 物品名称

        Returns:
            Sequence[TradeItem]: 外观搜索
        """

    def trade_records(
        self,
        *,
        name: Annotated[str, "物品名称"],
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[TradeRecords, "物品价格"]:
        """
        物品价格

        定位外观（search.main）后取各区 / 指定服历史成交价（search.sales，各最近 10 条）

        Args:
            name (str): 物品名称
            server (str | None): 服务器名称

        Returns:
            TradeRecords: 物品价格
        """

    ##########
    # VIP  2 #
    ##########

    def auction_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str | None, "物品名称"] = None,
        limit: Annotated[int, "限制数量"] = 50,
    ) -> Annotated[Sequence[AuctionRecord], "阵营拍卖"]:
        """
        阵营拍卖

        按大区查角色竞拍记录，可按物品名模糊筛选，时间倒序

        Args:
            server (str): 服务器名称
            name (str | None): 物品名称
            limit (int): 限制数量

        Returns:
            Sequence[AuctionRecord]: 阵营拍卖
        """

    def card_cached(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[CardCached, "名片缓存"]:
        """
        名片缓存

        转发远程取已缓存名片

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            CardCached: 名片缓存
        """

    def card_preset(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[dict, "名片预设"]:
        """
        名片预设

        取角色推栏名片预设图与获赞数，URL 解密后返回

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            dict: 名片预设
        """

    def card_random(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        force: Annotated[str | None, "门派名称"] = None,
        body: Annotated[str | None, "体型名称"] = None,
    ) -> Annotated[CardRandom, "随机名片"]:
        """
        随机名片

        转发远程按门派 / 体型随机取一张名片

        Args:
            server (str | None): 服务器名称
            force (str | None): 门派名称
            body (str | None): 体型名称

        Returns:
            CardRandom: 随机名片
        """

    def card_record(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[CardRecord, "名片记录"]:
        """
        名片记录

        转发远程取角色名片

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            CardRecord: 名片记录
        """

    def card_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
        like: Annotated[bool, "是否只看点赞"] = False,
    ) -> Annotated[Sequence[CardHistory], "名片历史"]:
        """
        名片历史

        转发远程取角色名片历史列表

        Args:
            server (str): 服务器名称
            name (str): 角色名称
            like (bool): 是否只看点赞

        Returns:
            Sequence[CardHistory]: 名片历史
        """

    def castle_status(self) -> Annotated[Sequence[CastleStatus], "关隘首领"]:
        """
        关隘首领

        各服关隘首领的当前状态（可拾取 / 保护期 / 可抢占 / 每日 7-12 点统一保护），按服务器分组

        Returns:
            Sequence[CastleStatus]: 关隘首领
        """

    def chitu_records(self) -> Annotated[Sequence[ChituRecord], "今日赤兔"]:
        """
        今日赤兔

        查 ranch 合集当天的赤兔记录

        Returns:
            Sequence[ChituRecord]: 今日赤兔
        """

    def chitu_week_records(
        self,
    ) -> Annotated[Sequence[ChituWeekRecord] | dict, "本周赤兔"]:
        """
        本周赤兔

        爬 jx3box 播报，解析各服本周(周二 7 点重置后)赤兔到达地图

        Returns:
            Sequence[ChituWeekRecord] | dict: 本周赤兔
        """

    def fenxian_records(
        self,
        *,
        name: Annotated[str | None, "阵营名称"] = None,
        limit: Annotated[int, "显示数量"] = 100,
    ) -> Annotated[Sequence[FenxianRecord], "阵营奉献"]:
        """
        阵营奉献

        据点争夺记录，按占领时间倒序；给了阵营名则只看该阵营（原 id DESC → seize_time DESC）

        Args:
            name (str | None): 阵营名称
            limit (int): 显示数量

        Returns:
            Sequence[FenxianRecord]: 阵营奉献
        """

    def firework_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[Sequence[FireworkRecord], "烟花记录"]:
        """
        烟花记录

        角色作为送花人或收花人的烟花记录，时间倒序

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            Sequence[FireworkRecord]: 烟花记录
        """

    def monster_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[MonsterRecord, "角色百战"]:
        """
        角色百战

        角色的百战技能配装（体力 / 精力 / 场次 / 技能列表）；未打过则取全服默认技能

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            MonsterRecord: 角色百战
        """

    def monster_weekly(self) -> Annotated[MonsterWeekly, "百战首领"]:
        """
        百战首领

        本周首领列表及 buff 效果，附荡剑恩仇轮换首领

        Returns:
            MonsterWeekly: 百战首领
        """

    def ranch_chat(
        self,
        *,
        server: Annotated[str, "服务器名称"],
    ) -> Annotated[dict[str, Sequence[str]], "马场预告"]:
        """
        马场预告

        爬 jx3box 马场 NPC 播报，解析各地图「下一匹 X 出世还有 N 分钟」的预计时刻

        Args:
            server (str): 服务器名称

        Returns:
            dict[str, Sequence[str]]: 马场预告
        """

    def rank_arena(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        mode: Annotated[int, "竞技模式 0=2v2/1=3v3/2=5v5"] = 0,
    ) -> Annotated[Sequence[dict], "跨服名剑"]:
        """
        跨服名剑

        按竞技模式（0=2v2 / 1=3v3 / 2=5v5）查军团赛季战绩榜；指定服查单服，否则全服

        Args:
            server (str | None): 服务器名称
            mode (int): 竞技模式 0=2v2/1=3v3/2=5v5

        Returns:
            Sequence[dict]: 跨服名剑
        """

    def rank_championship(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        camp: Annotated[int, "阵营 1=浩气/2=恶人"] = 1,
    ) -> Annotated[Sequence[dict], "武林争霸"]:
        """
        武林争霸

        按阵营（1=浩气 / 2=恶人）查帮会争霸赛季榜（与名剑榜共用 season 合集，每赛季清零）

        Args:
            server (str | None): 服务器名称
            camp (int): 阵营 1=浩气/2=恶人

        Returns:
            Sequence[dict]: 武林争霸
        """

    def rank_constable(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Sequence[dict], "捕快荣誉"]:
        """
        捕快荣誉

        与江湖浪客榜同字段格式（bounty 合集）

        Args:
            server (str | None): 服务器名称

        Returns:
            Sequence[dict]: 捕快荣誉
        """

    def rank_outlaw(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Sequence[dict], "江湖浪客"]:
        """
        江湖浪客

        实时榜（bounty 合集），显式列字段，nRank 排名序号不返回

        Args:
            server (str | None): 服务器名称

        Returns:
            Sequence[dict]: 江湖浪客
        """

    def rank_wanted(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        mode: Annotated[int, "1=公开/2=私密"] = 1,
    ) -> Annotated[Sequence[dict], "决斗挑战"]:
        """
        决斗挑战

        按类型（1=公开 / 2=私密）查决斗悬赏榜（bounty 合集，mode 存的是字符串）

        Args:
            server (str | None): 服务器名称
            mode (int): 1=公开/2=私密

        Returns:
            Sequence[dict]: 决斗挑战
        """

    def role_achievement(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        role: Annotated[str, "角色名称"],
        name: Annotated[str, "成就名称"],
    ) -> Annotated[RoleAchievement, "成就查询"]:
        """
        成就查询

        角色名片 + 成就库按 名称/分类/子类/详情 模糊匹配，标记该角色是否已完成（魔盒成就）

        Args:
            server (str): 服务器名称
            role (str): 角色名称
            name (str): 成就名称

        Returns:
            RoleAchievement: 成就查询
        """

    def saohua_context(
        self,
        *,
        name: Annotated[str, "语录分类（疯狂星期四 / 彩虹屁 / 毒鸡汤 / 朋友圈）"],
    ) -> Annotated[SaohuaContext, "分类语录"]:
        """
        分类语录

        按分类名随机取一条（疯狂星期四 / 彩虹屁 / 毒鸡汤 / 朋友圈）

        Args:
            name (str): 语录分类（疯狂星期四 / 彩虹屁 / 毒鸡汤 / 朋友圈）

        Returns:
            SaohuaContext: 分类语录
        """

    def school_search(
        self,
        *,
        name: Annotated[str, "门派名称"],
        mode: Annotated[str | None, "玩法模式"] = None,
    ) -> Annotated[dict, "配装搜索"]:
        """
        配装搜索

        按心法 + 玩法模式取推栏推荐配装；赛季与配装各缓存 7 天（少打推栏）

        Args:
            name (str): 门派名称
            mode (str | None): 玩法模式

        Returns:
            dict: 配装搜索
        """

    def skill_calculate(
        self,
        *,
        cooldown: Annotated[float, "技能 cd"] = 1.5,
    ) -> Annotated[Sequence[SkillCalculate], "急速计算"]:
        """
        急速计算

        按技能 cd 推算各急速档位对应的读条帧数与实际时长（帧数相同的档位去重，只保留最低急速） extra / uExtra 预留额外急速（当前为 0），保留 buff 版字段（uNowFrame / hastePercentLimit）供前端全字段渲染

        Args:
            cooldown (float): 技能 cd

        Returns:
            Sequence[SkillCalculate]: 急速计算
        """

    def steed_records(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Sequence[SteedRecord], "的卢拍卖"]:
        """
        的卢拍卖

        指定服返回最新 10 条；不指定则每服最新 1 条（按收录服列全，无记录给空）

        Args:
            server (str | None): 服务器名称

        Returns:
            Sequence[SteedRecord]: 的卢拍卖
        """

    def trade_manufacture(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "成品名称"],
        source: Annotated[int, "价格来源 0=交易行/1=jx3box"] = 0,
    ) -> Annotated[TradeManufacture, "成本计算"]:
        """
        成本计算

        按成品配方（seasun.recipe/cooking）算材料成本：商店材料取固定售价，交易行材料 + 成品取实时价（jx3box）

        Args:
            server (str): 服务器名称
            name (str): 成品名称
            source (int): 价格来源 0=交易行/1=jx3box

        Returns:
            TradeManufacture: 成本计算
        """

    def trade_wanbaolou(
        self,
        *,
        id: Annotated[str, "角色编号"],
    ) -> Annotated[dict, "编号搜索"]:
        """
        编号搜索

        按角色编号查万宝楼账号详情（aijx3 两跳：查 zhanghaoId 再取详情，密文 base64+zlib 解开）

        Args:
            id (str): 角色编号

        Returns:
            dict: 编号搜索
        """

    def tuilan_achievement(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
        class_: Annotated[int, "资历分类"] = 1,
        subclass: Annotated[str | None, "资历子类"] = None,
    ) -> Annotated[dict, "资历分布"]:
        """
        资历分布

        角色名片 + 按 子类/详情/地图/副本 汇总的资历完成度 静态骨架（各桶 total + 排序 + totalScore）按 class 缓存，每次请求只查用户已完成子集叠加 speed

        Args:
            server (str): 服务器名称
            name (str): 角色名称
            class_ (int): 资历分类
            subclass (str | None): 资历子类

        Returns:
            dict: 资历分布
        """

    def wicked_records(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        limit: Annotated[int, "显示数量"] = 20,
    ) -> Annotated[Sequence[WickedRecord], "诛恶事件"]:
        """
        诛恶事件

        恶人（诛恶）刷新记录，时间倒序；指定服查单服，不指定查全服

        Args:
            server (str | None): 服务器名称
            limit (int): 显示数量

        Returns:
            Sequence[WickedRecord]: 诛恶事件
        """

class AsyncJX3API:
    def __init__(
        self,
        *,
        token: Annotated[str | None, "站点访问令牌"] = None,
        ticket: Annotated[str | None, "推栏标识鉴权"] = None,
        base_url: Annotated[str, "API 根地址"] = "https://www.jx3api.com",
        **kwargs,
    ) -> None: ...

    ##########
    # FREE  #
    ##########

    async def active_calendar(
        self,
        *,
        num: Annotated[int, "天数偏移（单日）或区间半径（list）"] = 0,
        mode: Annotated[str, "'day' 单日 / 'list' 前后区间"] = "day",
    ) -> Annotated[Awaitable[ActiveCalendar | ActiveListCalendar], "活动日历"]:
        """
        活动日历

        单日或前后区间的日常活动推演

        Args:
            num (int): 天数偏移（单日）或区间半径（list）
            mode (str): 'day' 单日 / 'list' 前后区间

        Returns:
            Awaitable[ActiveCalendar | ActiveListCalendar]: 活动日历
        """

    async def active_celebs(
        self,
        *,
        name: Annotated[str, "事件名称"],
    ) -> Annotated[Awaitable[Sequence[ActiveCelebs]], "地图活动"]:
        """
        地图活动

        楚天社 / 云从社 / 披风会接下来 10 条排期

        Args:
            name (str): 事件名称

        Returns:
            Awaitable[Sequence[ActiveCelebs]]: 地图活动
        """

    async def battle_records(
        self,
        *,
        server: Annotated[str, "查询信息"],
    ) -> Annotated[Awaitable[Sequence[BattleRecord]], "帮战记录"]:
        """
        帮战记录

        查某服最近 30 场帮战，区分已结束 / 进行中并算出时长与结束时间

        Args:
            server (str): 查询信息

        Returns:
            Awaitable[Sequence[BattleRecord]]: 帮战记录
        """

    async def duowan_statistics(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Awaitable[Sequence[DuowanStatistics]], "统战歪歪"]:
        """
        统战歪歪

        查各服 YY 语音频道的在线主播；指定服查该服两营，不指定则每服每营取一个代表

        Args:
            server (str | None): 服务器名称

        Returns:
            Awaitable[Sequence[DuowanStatistics]]: 统战歪歪
        """

    async def exam_search(
        self,
        *,
        subject: Annotated[str, "科举试题"],
        limit: Annotated[int, "返回数量"] = 10,
    ) -> Annotated[Awaitable[Sequence[ExamAnswer]], "科举答案"]:
        """
        科举答案

        按题目或拼音模糊匹配，返回候选答案（原 question/pinyin LIKE 双查）

        Args:
            subject (str): 科举试题
            limit (int): 返回数量

        Returns:
            Awaitable[Sequence[ExamAnswer]]: 科举答案
        """

    async def food_list(
        self,
        *,
        name: Annotated[str | None, "心法名称"] = None,
    ) -> Annotated[Awaitable[Sequence[SchoolFood]], "小吃小药"]:
        """
        小吃小药

        指定心法则返回该心法的小吃小药，否则返回全部

        Args:
            name (str | None): 心法名称

        Returns:
            Awaitable[Sequence[SchoolFood]]: 小吃小药
        """

    async def home_flower(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "鲜花名称"] = "",
        map: Annotated[str, "地图名称"] = "",
    ) -> Annotated[Awaitable[dict[str, Sequence[HomeFlowerItem]]], "家园鲜花"]:
        """
        家园鲜花

        白名单校验后查推栏鲜花行情，按地图归组（鲜花名剥离括号色，括号内作 color）

        Args:
            server (str): 服务器名称
            name (str): 鲜花名称
            map (str): 地图名称

        Returns:
            Awaitable[dict[str, Sequence[HomeFlowerItem]]]: 家园鲜花
        """

    async def home_furniture(
        self,
        *,
        name: Annotated[str, "装饰名称"],
    ) -> Annotated[Awaitable[Sequence[HomeFurniture]], "家园装饰"]:
        """
        家园装饰

        按装饰名查 travel 合集，补全图片链接

        Args:
            name (str): 装饰名称

        Returns:
            Awaitable[Sequence[HomeFurniture]]: 家园装饰
        """

    async def home_travel(
        self,
        *,
        name: Annotated[str, "器物名称"],
    ) -> Annotated[Awaitable[Sequence[HomeTravel]], "器物图谱"]:
        """
        器物图谱

        按器物名查 travel 合集（produce 列），补全图片链接

        Args:
            name (str): 器物名称

        Returns:
            Awaitable[Sequence[HomeTravel]]: 器物图谱
        """

    async def news_announce(
        self,
        *,
        limit: Annotated[int, "显示数量"] = 10,
    ) -> Annotated[Awaitable[Sequence[NewsRecord]], "维护公告"]:
        """
        维护公告

        标题含“版本更新”的公告，最新在前

        Args:
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[NewsRecord]]: 维护公告
        """

    async def news_records(
        self,
        *,
        limit: Annotated[int, "显示数量"] = 10,
    ) -> Annotated[Awaitable[Sequence[NewsRecord]], "新闻资讯"]:
        """
        新闻资讯

        最新资讯列表；原 id DESC → _id DESC（导入按原 id 升序插入，等价于最新在前）

        Args:
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[NewsRecord]]: 新闻资讯
        """

    async def saohua_content(self) -> Annotated[Awaitable[SaohuaContent], "舔狗日志"]:
        """
        舔狗日志

        从舔狗日志库随机取一条

        Returns:
            Awaitable[SaohuaContent]: 舔狗日志
        """

    async def saohua_random(self) -> Annotated[Awaitable[SaohuaRandom], "随机骚话"]:
        """
        随机骚话

        从骚话库随机取一条

        Returns:
            Awaitable[SaohuaRandom]: 随机骚话
        """

    async def server_status_check(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Awaitable[ServerCheck | Sequence[ServerCheck]], "大区状态"]:
        """
        大区状态

        拉 xoyo 服务器列表（60 秒缓存）解析各服在线状态；指定服返回单条，否则返回收录的全部

        Args:
            server (str | None): 服务器名称

        Returns:
            Awaitable[ServerCheck | Sequence[ServerCheck]]: 大区状态
        """

    async def skill_rework(
        self,
    ) -> Annotated[Awaitable[Sequence[SkillRework]], "技改记录"]:
        """
        技改记录

        拉 xoyo 公告列表（10 分钟缓存），筛出标题含「武学调整」的技改公告

        Returns:
            Awaitable[Sequence[SkillRework]]: 技改记录
        """

    async def sound_converter(
        self,
        *,
        appkey: Annotated[str, "阿里云 appkey"],
        access: Annotated[str, "AccessKeyId"],
        secret: Annotated[str, "AccessKeySecret"],
        voice: Annotated[str, "发音人"] = "Aitong",
        format: Annotated[str, "音频编码"] = "mp3",
        sample_rate: Annotated[int, "音频采样率"] = 16000,
        volume: Annotated[str, "音量"] = "50",
        speech_rate: Annotated[str, "语速"] = "0",
        pitch_rate: Annotated[str, "语调"] = "0",
        text: Annotated[str, "语音内容"],
    ) -> Annotated[Awaitable[SoundConverter], "语音合成"]:
        """
        语音合成

        用用户的阿里云密钥签名换取 Token，拼出 NLS TTS 流地址返回

        Args:
            appkey (str): 阿里云 appkey
            access (str): AccessKeyId
            secret (str): AccessKeySecret
            voice (str): 发音人
            format (str): 音频编码
            sample_rate (int): 音频采样率
            volume (str): 音量
            speech_rate (str): 语速
            pitch_rate (str): 语调
            text (str): 语音内容

        Returns:
            Awaitable[SoundConverter]: 语音合成
        """

    ##########
    # VIP  1 #
    ##########

    async def arena_awesome(
        self,
        *,
        mode: Annotated[int, "服务器名称"] = 33,
        limit: Annotated[int, "显示数量"] = 20,
    ) -> Annotated[Awaitable[Sequence[ArenaAwesome]], "名剑排行"]:
        """
        名剑排行

        某比赛模式竞技场排行榜前 limit 名

        Args:
            mode (int): 服务器名称
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[ArenaAwesome]]: 名剑排行
        """

    async def arena_recent(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
        mode: Annotated[str, "比赛模式"] = 0,
    ) -> Annotated[Awaitable[ArenaRecent], "名剑战绩"]:
        """
        名剑战绩

        角色竞技场名片、各模式战绩表现、历史对战，指定模式时附趋势

        Args:
            server (str): 服务器名称
            name (str): 角色名称
            mode (str): 比赛模式

        Returns:
            Awaitable[ArenaRecent]: 名剑战绩
        """

    async def arena_schools(
        self,
        *,
        mode: Annotated[int, "比赛模式"] = 33,
    ) -> Annotated[Awaitable[Sequence[ArenaSchools]], "名剑统计"]:
        """
        名剑统计

        某比赛模式下各门派的竞技场周统计

        Args:
            mode (int): 比赛模式

        Returns:
            Awaitable[Sequence[ArenaSchools]]: 名剑统计
        """

    async def event_collect(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        num: Annotated[int, "统计天数"] = 7,
    ) -> Annotated[Awaitable[Sequence[EventCollect]], "奇遇汇总"]:
        """
        奇遇汇总

        白名单每个奇遇：最近 num 天在该服的触发次数 + 历史最新一条（角色名/时间）

        Args:
            server (str): 服务器名称
            num (int): 统计天数

        Returns:
            Awaitable[Sequence[EventCollect]]: 奇遇汇总
        """

    async def event_missing(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[Awaitable[Sequence[EventMissing]], "未触发的"]:
        """
        未触发的

        返回该角色尚未触发的奇遇（不在全局 binding / 服务器 event 记录里的 event.master 项）

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            Awaitable[Sequence[EventMissing]]: 未触发的
        """

    async def event_recent(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        limit: Annotated[int, "显示数量"] = 20,
    ) -> Annotated[Awaitable[Sequence[EventRecord]], "近期奇遇"]:
        """
        近期奇遇

        某服最近触发的奇遇事件，时间倒序

        Args:
            server (str): 服务器名称
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[EventRecord]]: 近期奇遇
        """

    async def event_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
        full: Annotated[int, "是否返回完整列表（含未触发）"] = 0,
    ) -> Annotated[Awaitable[Sequence[EventRecord]], "奇遇记录"]:
        """
        奇遇记录

        整合角色全局事件(binding) + 服务器事件(event) + 魔盒成就，可补全未触发

        Args:
            server (str): 服务器名称
            name (str): 角色名称
            full (int): 是否返回完整列表（含未触发）

        Returns:
            Awaitable[Sequence[EventRecord]]: 奇遇记录
        """

    async def event_statistics(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        name: Annotated[str, "奇遇名称"],
        limit: Annotated[int, "显示数量"] = 20,
    ) -> Annotated[Awaitable[Sequence[EventRecord]], "奇遇统计"]:
        """
        奇遇统计

        某奇遇最近的触发记录，时间倒序；指定服查单服，不指定查全服

        Args:
            server (str | None): 服务器名称
            name (str): 奇遇名称
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[EventRecord]]: 奇遇统计
        """

    async def event_strategy(
        self,
        *,
        name: Annotated[str, "奇遇名称"],
    ) -> Annotated[Awaitable[EventStrategy], "奇遇攻略"]:
        """
        奇遇攻略

        返回该奇遇的白名单配置（event.master + touch.master 合并）

        Args:
            name (str): 奇遇名称

        Returns:
            Awaitable[EventStrategy]: 奇遇攻略
        """

    async def fraud_detail(
        self,
        *,
        server: Annotated[str, "服务器名称"] = "",
        uid: Annotated[int, "角色 UID"],
    ) -> Annotated[Awaitable[Sequence[FraudRecord]], "骗子查询"]:
        """
        骗子查询

        按 route 合集配置转发到远程风控服务，取该 UID 的详细记录

        Args:
            server (str): 服务器名称
            uid (int): 角色 UID

        Returns:
            Awaitable[Sequence[FraudRecord]]: 骗子查询
        """

    async def mech_decrypt(self) -> Annotated[Awaitable[MechDecrypt], "秘境方位"]:
        """
        秘境方位

        按 15 分钟档推算当前方位、下次变化时刻与倒计时

        Returns:
            Awaitable[MechDecrypt]: 秘境方位
        """

    async def mentor_search(
        self,
        *,
        label: Annotated[int, "师徒类型"] = 1,
        server: Annotated[str, "服务器大区"],
        keyword: Annotated[str | None, "关键字"] = None,
        limit: Annotated[int, "显示数量"] = 50,
    ) -> Annotated[Awaitable[Sequence[MentorRecord]], "师徒列表"]:
        """
        师徒列表

        转发到远程取师徒名单，按关键字过滤评论，超量随机抽样

        Args:
            label (int): 师徒类型
            server (str): 服务器大区
            keyword (str | None): 关键字
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[MentorRecord]]: 师徒列表
        """

    async def raid_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[Awaitable[Sequence[RaidRecord]], "副本记录"]:
        """
        副本记录

        转发到远程取该角色的团队副本 CD 列表

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            Awaitable[Sequence[RaidRecord]]: 副本记录
        """

    async def ranch_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        expired: Annotated[int, "是否包含已过期"] = 0,
    ) -> Annotated[Awaitable[RanchRecords], "马场事件"]:
        """
        马场事件

        jx3box 马场播报预告 + 本周期赤兔（mount）/ 的卢（steed）出世情况，附提示

        Args:
            server (str): 服务器名称
            expired (int): 是否包含已过期

        Returns:
            Awaitable[RanchRecords]: 马场事件
        """

    async def rank_statistics(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[Awaitable[RankStatistics], "排行统计"]:
        """
        排行统计

        指定服查该服该榜单，否则查全服该榜单

        Args:
            server (str | None): 服务器名称
            name (str): 榜单名称

        Returns:
            Awaitable[RankStatistics]: 排行统计
        """

    async def rank_trials(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[Awaitable[RankTrials], "试炼之地"]:
        """
        试炼之地

        同榜单查询，山居剑意归并到藏剑；行是位置字段 1~4，重建成具名字段

        Args:
            server (str | None): 服务器名称
            name (str): 榜单名称

        Returns:
            Awaitable[RankTrials]: 试炼之地
        """

    async def recruit_search(
        self,
        *,
        server: Annotated[str, "服务器大区"],
        label: Annotated[int, "服务类型"] = 1,
        keyword: Annotated[str | None, "关键字"] = None,
        limit: Annotated[int, "显示数量"] = 50,
    ) -> Annotated[Awaitable[Sequence[RecruitRecord]], "团队招募"]:
        """
        团队招募

        转发远程取招募名单，按关键字（活动/团长/内容）过滤，超量截断

        Args:
            server (str): 服务器大区
            label (int): 服务类型
            keyword (str | None): 关键字
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[RecruitRecord]]: 团队招募
        """

    async def reward_statistics(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        name: Annotated[str, "物品名称"],
        limit: Annotated[int, "显示数量"] = 20,
    ) -> Annotated[Awaitable[Sequence[RewardRecord]], "掉落统计"]:
        """
        掉落统计

        按物品名模糊匹配掉落记录，时间倒序；指定服查单服，不指定查全服

        Args:
            server (str | None): 服务器名称
            name (str): 物品名称
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[RewardRecord]]: 掉落统计
        """

    async def role_detail(
        self,
        *,
        server: Annotated[str, "服务器大区"],
        name: Annotated[str, "角色名称"],
        history: Annotated[int, "是否返回改名 / 帮会历史"] = 0,
    ) -> Annotated[Awaitable[RoleDetailed], "角色详情"]:
        """
        角色详情

        角色名片（roles 合集）；每次都采集 ermaozi 历史去重入库以持续收录 history=1：同步先采集再返回最新历史；history=0：采集甩到响应之后异步跑，客户端零等待

        Args:
            server (str): 服务器大区
            name (str): 角色名称
            history (int): 是否返回改名 / 帮会历史

        Returns:
            Awaitable[RoleDetailed]: 角色详情
        """

    async def sand_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
    ) -> Annotated[Awaitable[ServerSand], "沙盘据点"]:
        """
        沙盘据点

        各据点归属帮会 / 阵营 + 本周被献祭（防守）次数

        Args:
            server (str): 服务器名称

        Returns:
            Awaitable[ServerSand]: 沙盘据点
        """

    async def school_matrix(
        self,
        *,
        name: Annotated[str, "职业名称"],
    ) -> Annotated[Awaitable[SchoolMatrix], "阵眼效果"]:
        """
        阵眼效果

        按心法取推栏阵眼（阵法）效果与描述

        Args:
            name (str): 职业名称

        Returns:
            Awaitable[SchoolMatrix]: 阵眼效果
        """

    async def school_seniority(
        self,
        *,
        server: Annotated[str, "服务器名称"] = "ALL",
        school: Annotated[str, "门派名称"] = "ALL",
    ) -> Annotated[Awaitable[Sequence[SchoolSeniority]], "资历榜单"]:
        """
        资历榜单

        指定服 / 门派（默认全服全门派）的资历前 100 名，补门派名

        Args:
            server (str): 服务器名称
            school (str): 门派名称

        Returns:
            Awaitable[Sequence[SchoolSeniority]]: 资历榜单
        """

    async def school_skills(
        self,
        *,
        name: Annotated[str, "门派名称"],
        update: Annotated[int, "是否更新"] = 0,
    ) -> Annotated[Awaitable[Sequence[SchoolSkills]], "技能信息"]:
        """
        技能信息

        按心法取推栏各分类（remark）下的招式技能

        Args:
            name (str): 门派名称
            update (int): 是否更新

        Returns:
            Awaitable[Sequence[SchoolSkills]]: 技能信息
        """

    async def school_talent(
        self,
        *,
        name: Annotated[str, "门派名称"],
        update: Annotated[int, "是否更新"] = 0,
    ) -> Annotated[Awaitable[Sequence[SchoolTalent]], "奇穴信息"]:
        """
        奇穴信息

        按心法取推栏各等级的招式（class=1）/ 奇穴（class=0）技能，按等级升序

        Args:
            name (str): 门派名称
            update (int): 是否更新

        Returns:
            Awaitable[Sequence[SchoolTalent]]: 奇穴信息
        """

    async def tieba_item_records(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        name: Annotated[str, "物品名称"],
        limit: Annotated[int, "返回数量"] = 10,
    ) -> Annotated[Awaitable[Sequence[TiebaItemRecord]], "外观记录"]:
        """
        外观记录

        在贴吧楼层（search.floor）里按物品名搜相关帖子（正则 + 分词兜底）

        Args:
            server (str | None): 服务器名称
            name (str): 物品名称
            limit (int): 返回数量

        Returns:
            Awaitable[Sequence[TiebaItemRecord]]: 外观记录
        """

    async def tieba_random(
        self,
        *,
        tags: Annotated[str, "帖子类型"],
        server: Annotated[str | None, "服务器名称"] = None,
        limit: Annotated[int, "返回数量"] = 10,
    ) -> Annotated[Awaitable[Sequence[TiebaRandom]], "百度贴吧"]:
        """
        百度贴吧

        按帖子类型随机取近 31 天的帖子（seasun.tieba），可选指定服

        Args:
            tags (str): 帖子类型
            server (str | None): 服务器名称
            limit (int): 返回数量

        Returns:
            Awaitable[Sequence[TiebaRandom]]: 百度贴吧
        """

    async def trade_demon(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        limit: Annotated[int, "显示数量"] = 10,
    ) -> Annotated[Awaitable[Sequence[TradeDemon]], "金价行情"]:
        """
        金价行情

        各渠道金币比价（search.price）；指定服返回该服最近 limit 条，否则每服最新一条

        Args:
            server (str | None): 服务器名称
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[TradeDemon]]: 金价行情
        """

    async def trade_item_records(
        self,
        *,
        name: Annotated[str, "物品名称"],
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Awaitable[TradeRecords], "外观价格"]:
        """
        外观价格

        精确定位外观（search.main）后取各区/指定服历史成交 + 万宝楼两期挂单

        Args:
            name (str): 物品名称
            server (str | None): 服务器名称

        Returns:
            Awaitable[TradeRecords]: 外观价格
        """

    async def trade_item_search(
        self,
        *,
        name: Annotated[str, "物品名称"],
    ) -> Annotated[Awaitable[Sequence[TradeItem]], "外观搜索"]:
        """
        外观搜索

        按名称查外观（search.main）；先精确 name/alias/feiniu，无则模糊 name/alias/allalias/feiniu

        Args:
            name (str): 物品名称

        Returns:
            Awaitable[Sequence[TradeItem]]: 外观搜索
        """

    async def trade_records(
        self,
        *,
        name: Annotated[str, "物品名称"],
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Awaitable[TradeRecords], "物品价格"]:
        """
        物品价格

        定位外观（search.main）后取各区 / 指定服历史成交价（search.sales，各最近 10 条）

        Args:
            name (str): 物品名称
            server (str | None): 服务器名称

        Returns:
            Awaitable[TradeRecords]: 物品价格
        """

    ##########
    # VIP  2 #
    ##########

    async def auction_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str | None, "物品名称"] = None,
        limit: Annotated[int, "限制数量"] = 50,
    ) -> Annotated[Awaitable[Sequence[AuctionRecord]], "阵营拍卖"]:
        """
        阵营拍卖

        按大区查角色竞拍记录，可按物品名模糊筛选，时间倒序

        Args:
            server (str): 服务器名称
            name (str | None): 物品名称
            limit (int): 限制数量

        Returns:
            Awaitable[Sequence[AuctionRecord]]: 阵营拍卖
        """

    async def card_cached(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[Awaitable[CardCached], "名片缓存"]:
        """
        名片缓存

        转发远程取已缓存名片

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            Awaitable[CardCached]: 名片缓存
        """

    async def card_preset(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[Awaitable[dict], "名片预设"]:
        """
        名片预设

        取角色推栏名片预设图与获赞数，URL 解密后返回

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            Awaitable[dict]: 名片预设
        """

    async def card_random(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        force: Annotated[str | None, "门派名称"] = None,
        body: Annotated[str | None, "体型名称"] = None,
    ) -> Annotated[Awaitable[CardRandom], "随机名片"]:
        """
        随机名片

        转发远程按门派 / 体型随机取一张名片

        Args:
            server (str | None): 服务器名称
            force (str | None): 门派名称
            body (str | None): 体型名称

        Returns:
            Awaitable[CardRandom]: 随机名片
        """

    async def card_record(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[Awaitable[CardRecord], "名片记录"]:
        """
        名片记录

        转发远程取角色名片

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            Awaitable[CardRecord]: 名片记录
        """

    async def card_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
        like: Annotated[bool, "是否只看点赞"] = False,
    ) -> Annotated[Awaitable[Sequence[CardHistory]], "名片历史"]:
        """
        名片历史

        转发远程取角色名片历史列表

        Args:
            server (str): 服务器名称
            name (str): 角色名称
            like (bool): 是否只看点赞

        Returns:
            Awaitable[Sequence[CardHistory]]: 名片历史
        """

    async def castle_status(
        self,
    ) -> Annotated[Awaitable[Sequence[CastleStatus]], "关隘首领"]:
        """
        关隘首领

        各服关隘首领的当前状态（可拾取 / 保护期 / 可抢占 / 每日 7-12 点统一保护），按服务器分组

        Returns:
            Awaitable[Sequence[CastleStatus]]: 关隘首领
        """

    async def chitu_records(
        self,
    ) -> Annotated[Awaitable[Sequence[ChituRecord]], "今日赤兔"]:
        """
        今日赤兔

        查 ranch 合集当天的赤兔记录

        Returns:
            Awaitable[Sequence[ChituRecord]]: 今日赤兔
        """

    async def chitu_week_records(
        self,
    ) -> Annotated[Awaitable[Sequence[ChituWeekRecord] | dict], "本周赤兔"]:
        """
        本周赤兔

        爬 jx3box 播报，解析各服本周(周二 7 点重置后)赤兔到达地图

        Returns:
            Awaitable[Sequence[ChituWeekRecord] | dict]: 本周赤兔
        """

    async def fenxian_records(
        self,
        *,
        name: Annotated[str | None, "阵营名称"] = None,
        limit: Annotated[int, "显示数量"] = 100,
    ) -> Annotated[Awaitable[Sequence[FenxianRecord]], "阵营奉献"]:
        """
        阵营奉献

        据点争夺记录，按占领时间倒序；给了阵营名则只看该阵营（原 id DESC → seize_time DESC）

        Args:
            name (str | None): 阵营名称
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[FenxianRecord]]: 阵营奉献
        """

    async def firework_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[Awaitable[Sequence[FireworkRecord]], "烟花记录"]:
        """
        烟花记录

        角色作为送花人或收花人的烟花记录，时间倒序

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            Awaitable[Sequence[FireworkRecord]]: 烟花记录
        """

    async def monster_records(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
    ) -> Annotated[Awaitable[MonsterRecord], "角色百战"]:
        """
        角色百战

        角色的百战技能配装（体力 / 精力 / 场次 / 技能列表）；未打过则取全服默认技能

        Args:
            server (str): 服务器名称
            name (str): 角色名称

        Returns:
            Awaitable[MonsterRecord]: 角色百战
        """

    async def monster_weekly(self) -> Annotated[Awaitable[MonsterWeekly], "百战首领"]:
        """
        百战首领

        本周首领列表及 buff 效果，附荡剑恩仇轮换首领

        Returns:
            Awaitable[MonsterWeekly]: 百战首领
        """

    async def ranch_chat(
        self,
        *,
        server: Annotated[str, "服务器名称"],
    ) -> Annotated[Awaitable[dict[str, Sequence[str]]], "马场预告"]:
        """
        马场预告

        爬 jx3box 马场 NPC 播报，解析各地图「下一匹 X 出世还有 N 分钟」的预计时刻

        Args:
            server (str): 服务器名称

        Returns:
            Awaitable[dict[str, Sequence[str]]]: 马场预告
        """

    async def rank_arena(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        mode: Annotated[int, "竞技模式 0=2v2/1=3v3/2=5v5"] = 0,
    ) -> Annotated[Awaitable[Sequence[dict]], "跨服名剑"]:
        """
        跨服名剑

        按竞技模式（0=2v2 / 1=3v3 / 2=5v5）查军团赛季战绩榜；指定服查单服，否则全服

        Args:
            server (str | None): 服务器名称
            mode (int): 竞技模式 0=2v2/1=3v3/2=5v5

        Returns:
            Awaitable[Sequence[dict]]: 跨服名剑
        """

    async def rank_championship(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        camp: Annotated[int, "阵营 1=浩气/2=恶人"] = 1,
    ) -> Annotated[Awaitable[Sequence[dict]], "武林争霸"]:
        """
        武林争霸

        按阵营（1=浩气 / 2=恶人）查帮会争霸赛季榜（与名剑榜共用 season 合集，每赛季清零）

        Args:
            server (str | None): 服务器名称
            camp (int): 阵营 1=浩气/2=恶人

        Returns:
            Awaitable[Sequence[dict]]: 武林争霸
        """

    async def rank_constable(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Awaitable[Sequence[dict]], "捕快荣誉"]:
        """
        捕快荣誉

        与江湖浪客榜同字段格式（bounty 合集）

        Args:
            server (str | None): 服务器名称

        Returns:
            Awaitable[Sequence[dict]]: 捕快荣誉
        """

    async def rank_outlaw(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Awaitable[Sequence[dict]], "江湖浪客"]:
        """
        江湖浪客

        实时榜（bounty 合集），显式列字段，nRank 排名序号不返回

        Args:
            server (str | None): 服务器名称

        Returns:
            Awaitable[Sequence[dict]]: 江湖浪客
        """

    async def rank_wanted(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        mode: Annotated[int, "1=公开/2=私密"] = 1,
    ) -> Annotated[Awaitable[Sequence[dict]], "决斗挑战"]:
        """
        决斗挑战

        按类型（1=公开 / 2=私密）查决斗悬赏榜（bounty 合集，mode 存的是字符串）

        Args:
            server (str | None): 服务器名称
            mode (int): 1=公开/2=私密

        Returns:
            Awaitable[Sequence[dict]]: 决斗挑战
        """

    async def role_achievement(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        role: Annotated[str, "角色名称"],
        name: Annotated[str, "成就名称"],
    ) -> Annotated[Awaitable[RoleAchievement], "成就查询"]:
        """
        成就查询

        角色名片 + 成就库按 名称/分类/子类/详情 模糊匹配，标记该角色是否已完成（魔盒成就）

        Args:
            server (str): 服务器名称
            role (str): 角色名称
            name (str): 成就名称

        Returns:
            Awaitable[RoleAchievement]: 成就查询
        """

    async def saohua_context(
        self,
        *,
        name: Annotated[str, "语录分类（疯狂星期四 / 彩虹屁 / 毒鸡汤 / 朋友圈）"],
    ) -> Annotated[Awaitable[SaohuaContext], "分类语录"]:
        """
        分类语录

        按分类名随机取一条（疯狂星期四 / 彩虹屁 / 毒鸡汤 / 朋友圈）

        Args:
            name (str): 语录分类（疯狂星期四 / 彩虹屁 / 毒鸡汤 / 朋友圈）

        Returns:
            Awaitable[SaohuaContext]: 分类语录
        """

    async def school_search(
        self,
        *,
        name: Annotated[str, "门派名称"],
        mode: Annotated[str | None, "玩法模式"] = None,
    ) -> Annotated[Awaitable[dict], "配装搜索"]:
        """
        配装搜索

        按心法 + 玩法模式取推栏推荐配装；赛季与配装各缓存 7 天（少打推栏）

        Args:
            name (str): 门派名称
            mode (str | None): 玩法模式

        Returns:
            Awaitable[dict]: 配装搜索
        """

    async def skill_calculate(
        self,
        *,
        cooldown: Annotated[float, "技能 cd"] = 1.5,
    ) -> Annotated[Awaitable[Sequence[SkillCalculate]], "急速计算"]:
        """
        急速计算

        按技能 cd 推算各急速档位对应的读条帧数与实际时长（帧数相同的档位去重，只保留最低急速） extra / uExtra 预留额外急速（当前为 0），保留 buff 版字段（uNowFrame / hastePercentLimit）供前端全字段渲染

        Args:
            cooldown (float): 技能 cd

        Returns:
            Awaitable[Sequence[SkillCalculate]]: 急速计算
        """

    async def steed_records(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
    ) -> Annotated[Awaitable[Sequence[SteedRecord]], "的卢拍卖"]:
        """
        的卢拍卖

        指定服返回最新 10 条；不指定则每服最新 1 条（按收录服列全，无记录给空）

        Args:
            server (str | None): 服务器名称

        Returns:
            Awaitable[Sequence[SteedRecord]]: 的卢拍卖
        """

    async def trade_manufacture(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "成品名称"],
        source: Annotated[int, "价格来源 0=交易行/1=jx3box"] = 0,
    ) -> Annotated[Awaitable[TradeManufacture], "成本计算"]:
        """
        成本计算

        按成品配方（seasun.recipe/cooking）算材料成本：商店材料取固定售价，交易行材料 + 成品取实时价（jx3box）

        Args:
            server (str): 服务器名称
            name (str): 成品名称
            source (int): 价格来源 0=交易行/1=jx3box

        Returns:
            Awaitable[TradeManufacture]: 成本计算
        """

    async def trade_wanbaolou(
        self,
        *,
        id: Annotated[str, "角色编号"],
    ) -> Annotated[Awaitable[dict], "编号搜索"]:
        """
        编号搜索

        按角色编号查万宝楼账号详情（aijx3 两跳：查 zhanghaoId 再取详情，密文 base64+zlib 解开）

        Args:
            id (str): 角色编号

        Returns:
            Awaitable[dict]: 编号搜索
        """

    async def tuilan_achievement(
        self,
        *,
        server: Annotated[str, "服务器名称"],
        name: Annotated[str, "角色名称"],
        class_: Annotated[int, "资历分类"] = 1,
        subclass: Annotated[str | None, "资历子类"] = None,
    ) -> Annotated[Awaitable[dict], "资历分布"]:
        """
        资历分布

        角色名片 + 按 子类/详情/地图/副本 汇总的资历完成度 静态骨架（各桶 total + 排序 + totalScore）按 class 缓存，每次请求只查用户已完成子集叠加 speed

        Args:
            server (str): 服务器名称
            name (str): 角色名称
            class_ (int): 资历分类
            subclass (str | None): 资历子类

        Returns:
            Awaitable[dict]: 资历分布
        """

    async def wicked_records(
        self,
        *,
        server: Annotated[str | None, "服务器名称"] = None,
        limit: Annotated[int, "显示数量"] = 20,
    ) -> Annotated[Awaitable[Sequence[WickedRecord]], "诛恶事件"]:
        """
        诛恶事件

        恶人（诛恶）刷新记录，时间倒序；指定服查单服，不指定查全服

        Args:
            server (str | None): 服务器名称
            limit (int): 显示数量

        Returns:
            Awaitable[Sequence[WickedRecord]]: 诛恶事件
        """
