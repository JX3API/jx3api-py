from typing import (
    Annotated,
    AsyncGenerator,
    Awaitable,
    Dict,
    Generic,
    List,
    Literal,
    NotRequired,
    Sequence,
    TypedDict,
    TypeVar,
)

T = TypeVar("T")
class_ = Literal["class"]

class Response(TypedDict, Generic[T]):
    code: int
    data: T

class WebsocketResponse(TypedDict, Generic[T]):
    action: int
    data: T

class ActiveCalendar(TypedDict):
    date: Annotated[str, "日期"]
    week: Annotated[str, "星期"]
    war: Annotated[str, "大战"]
    battle: Annotated[str, "战场"]
    orecar: Annotated[str, "挖矿", Literal["烂柯山"]]
    school: Annotated[str, "门派事件"]
    rescue: Annotated[str, "驰援事件"]
    draw: NotRequired[Annotated[str, "美人图"]]
    leader: NotRequired[Annotated[Sequence[str], "世界首领"]]
    team: Annotated[
        Sequence[str],
        "多人活动",
        Annotated[str, "周常事件"],
        Annotated[str, "五人周常"],
        Annotated[str, "十人周长"],
    ]

class _Today(TypedDict):
    date: Annotated[str, "日期"]
    week: Annotated[str, "星期"]
    year: Annotated[str, "年"]
    month: Annotated[str, "月"]
    day: Annotated[str, "日"]

class _ActiveCalendarList(TypedDict):
    date: Annotated[str, "日期"]
    day: Annotated[str, "日"]
    week: Annotated[str, "星期"]
    war: Annotated[str, "大战"]
    battle: Annotated[str, "战场"]
    orecar: Annotated[str, "挖矿", Literal["烂柯山"]]
    school: Annotated[str, "门派事件"]
    rescue: Annotated[str, "驰援事件"]

class ActiveListCalendar(TypedDict):
    today: Annotated[_Today, "日期信息"]
    data: Annotated[Sequence[_ActiveCalendarList], "活动月历"]

class ActiveCelebs(TypedDict):
    map_name: Annotated[str, "地图名称"]
    event: Annotated[str, "事件名称"]
    site: Annotated[str, "地点"]
    desc: Annotated[str, "事件描述"]
    icon: Annotated[str, "事件图标"]
    time: Annotated[str, "事件时间"]

class ExamAnswer(TypedDict):
    id: Annotated[int, "试题 ID"]
    question: Annotated[str, "试题内容"]
    answer: Annotated[str, "试题答案"]
    correctness: Annotated[int, "正确性，1 为正确，0 为错误"]
    index: Annotated[int, "试题序号"]
    pinyin: Annotated[str, "试题拼音"]

class HomeFurniture(TypedDict):
    id: Annotated[int, "装饰 ID"]
    name: Annotated[str, "装饰名称"]
    type: Annotated[int, "装饰类型"]
    color: Annotated[int, "装饰颜色"]
    source: Annotated[str, "装饰来源"]
    architecture: Annotated[int, "建筑"]
    limit: Annotated[int, "装饰数量限制"]
    quality: Annotated[int, "装饰品质"]
    view: Annotated[int, "观赏值"]
    practical: Annotated[int, "实用值"]
    hard: Annotated[int, "坚固值"]
    geomantic: Annotated[int, "风水值"]
    interesting: Annotated[int, "趣味值"]
    produce: Annotated[str, "装饰产出地图"]
    image: Annotated[str, "装饰图片"]
    tip: Annotated[str, "装饰描述"]

class HomeTravel(TypedDict):
    id: Annotated[int, "装饰 ID"]
    name: Annotated[str, "装饰名称"]
    type: Annotated[int, "装饰类型"]
    color: Annotated[int, "装饰颜色"]
    source: Annotated[str, "装饰来源"]
    architecture: Annotated[int, "建筑"]
    limit: Annotated[int, "装饰数量限制"]
    quality: Annotated[int, "装饰品质"]
    view: Annotated[int, "观赏值"]
    practical: Annotated[int, "实用值"]
    hard: Annotated[int, "坚固值"]
    geomantic: Annotated[int, "风水值"]
    interesting: Annotated[int, "装饰趣味"]
    produce: Annotated[str, "装饰产出地图"]
    image: Annotated[str, "装饰图片"]
    tip: Annotated[str, "装饰产出地图提示"]

class NewsAllnews(TypedDict):
    id: Annotated[int, "新闻 ID"]
    token: Annotated[int, "新闻 Token"]
    class_: Annotated[str, "新闻分类"]
    title: Annotated[str, "新闻标题"]
    date: Annotated[str, "新闻日期"]
    url: Annotated[str, "新闻链接"]

class NewsAnnounce(TypedDict):
    id: Annotated[int, "公告 ID"]
    token: Annotated[int, "公告 Token"]
    class_: Annotated[str, "公告类别"]
    title: Annotated[str, "公告标题"]
    date: Annotated[str, "公告日期"]
    url: Annotated[str, "公告链接"]

class ServerMaster(TypedDict):
    id: Annotated[str, "区服 ID"]
    zone: Annotated[str, "区服所属大区"]
    name: Annotated[str, "区服名称"]
    column: Annotated[str, "c"]
    duowan: Annotated[Dict[str, List[int]], "多玩 ID"]
    abbreviation: Annotated[List[str], "区服简称"]
    subordinate: Annotated[List[str], "区服下属服务器"]

class ServerCheck(TypedDict):
    id: Annotated[int, "服务器 ID"]
    zone: Annotated[str, "服务器所在大区"]
    server: Annotated[str, "服务器名称"]
    status: Annotated[Literal[0, 1], "服务器状态，1 为开服，0 为维护中"]
    time: Annotated[int, "服务器状态更新时间戳"]

class ServerStatus(TypedDict):
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    status: Annotated[str, "服务器状态"]

class _HomeFlower(TypedDict):
    name: Annotated[str, "鲜花名称"]
    color: Annotated[str, "鲜花颜色"]
    price: Annotated[float, "鲜花价格"]
    line: Annotated[Sequence[str], "鲜花线路"]

class HomeFlower(TypedDict):
    map: Annotated[Sequence[_HomeFlower], "地图鲜花价格"]

class SaveDetailed(TypedDict):
    zoneName: Annotated[str, "区服名称"]
    serverName: Annotated[str, "服务器名称"]
    roleName: Annotated[str, "角色名称"]
    roleId: Annotated[str, "角色 ID"]
    globalRoleId: Annotated[str, "全局角色 ID"]
    forceName: Annotated[str, "门派名称"]
    forceId: Annotated[str, "门派 ID"]
    bodyName: Annotated[str, "体型名称"]
    bodyId: Annotated[str, "体型 ID"]
    tongName: Annotated[str, "帮会名称", "可选"]
    tongId: Annotated[str, "帮会 ID", "可选"]
    campName: Annotated[str, "阵营名称"]
    campId: Annotated[str, "阵营 ID"]
    personName: Annotated[str, "人物名称", "可选"]
    personId: Annotated[str, "人物ID", "可选"]
    personAvatar: Annotated[str, "人物头像"]

class RoleDetailed(TypedDict):
    zoneName: Annotated[str, "区服名称"]
    serverName: Annotated[str, "服务器名称"]
    roleName: Annotated[str, "角色名称"]
    roleId: Annotated[str, "角色 ID"]
    globalRoleId: Annotated[str, "全局角色 ID"]
    forceName: Annotated[str, "门派名称"]
    forceId: Annotated[str, "门派 ID"]
    bodyName: Annotated[str, "体型名称"]
    bodyId: Annotated[str, "体型 ID"]
    tongName: Annotated[str, "帮会名称"]
    tongId: Annotated[str, "帮会 ID"]
    campName: Annotated[str, "阵营名称"]
    campId: Annotated[str, "阵营 ID"]
    personName: Annotated[str, "人物名称"]
    personId: Annotated[str, "人物 ID"]
    personAvatar: Annotated[str, "人物头像"]

class SchoolMatrixDescs(TypedDict):
    desc: Annotated[str, "阵眼效果描述"]
    level: Annotated[int, "阵眼等级"]
    name: Annotated[str, "阵眼等级名称"]

class SchoolMatrix(TypedDict):
    name: Annotated[str, "心法名称"]
    skillName: Annotated[str, "阵眼名称"]
    descs: Annotated[Sequence[SchoolMatrixDescs], "阵眼效果列表"]

class _SchoolForce(TypedDict):
    name: Annotated[str, "奇穴名称"]
    class_: Annotated[int, "奇穴分类"]
    desc: Annotated[str, "奇穴效果描述"]
    icon: Annotated[str, "奇穴图标"]
    kind: Annotated[str, "奇穴类型"]
    subKind: Annotated[str, "奇穴子类型"]

class SchoolForce(TypedDict):
    level: Annotated[int, "奇穴等级"]
    data: Annotated[Sequence[_SchoolForce], "奇穴效果列表"]

class _SchoolSkills(TypedDict):
    name: Annotated[str, "技能名称"]
    simpleDesc: Annotated[str, "技能简要描述"]
    desc: Annotated[str, "技能详细描述"]
    specialDesc: Annotated[str, "技能特殊描述"]
    interval: Annotated[str, "技能间隔"]
    consumption: Annotated[str, "技能消耗"]
    distance: Annotated[str, "技能距离"]
    icon: Annotated[str, "技能图标"]
    kind: Annotated[str, "技能类型"]
    subKind: Annotated[str, "技能子类型"]
    releaseType: Annotated[str, "技能释放类型"]
    weapon: Annotated[str, "技能武器"]

class SchoolSkills(TypedDict):
    class_: Annotated[str, "心法名"]
    data: Annotated[List[_SchoolSkills], "技能"]

class TiebaRandom(TypedDict):
    id: Annotated[int, "帖子 ID"]
    class_: Annotated[str, "帖子分类"]
    zone: Annotated[str, "大区"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "游戏名称"]
    title: Annotated[str, "帖子标题"]
    url: Annotated[int, "帖子链接"]
    date: Annotated[str, "发布时间"]

class RoleTeamCdListBossProgress(TypedDict):
    finished: Annotated[bool, "是否完成"]
    icon: Annotated[str, "图标"]
    index: Annotated[str, "索引"]
    name: Annotated[str, "名称"]
    progressId: Annotated[str, "进度ID"]

class _RoleTeamCdList(TypedDict):
    mapIcon: Annotated[str, "地图图标"]
    mapId: Annotated[str, "地图 ID"]
    mapName: Annotated[str, "地图名称"]
    mapType: Annotated[str, "地图类型"]
    bossCount: Annotated[int, "BOSS 数量"]
    bossFinished: Annotated[int, "已完成 BOSS 数量"]
    bossProgress: Annotated[Sequence[RoleTeamCdListBossProgress], "BOSS 进度"]

class RoleTeamCdList(TypedDict):
    zoneName: Annotated[str, "区服名称"]
    serverName: Annotated[str, "服务器名称"]
    roleName: Annotated[str, "角色名称"]
    roleId: Annotated[str, "角色 ID"]
    globalRoleId: Annotated[str, "全局角色 ID"]
    forceName: Annotated[str, "门派名称"]
    forceId: Annotated[str, "门派 ID"]
    bodyName: Annotated[str, "体型名称"]
    bodyId: Annotated[str, "体型 ID"]
    tongName: Annotated[str, "帮会名称"]
    tongId: Annotated[str, "帮会 ID"]
    campName: Annotated[str, "阵营名称"]
    campId: Annotated[str, "阵营 ID"]
    personName: Annotated[str, "人物名称"]
    personId: Annotated[str, "人物 ID"]
    personAvatar: Annotated[str, "人物头像"]
    data: Annotated[Sequence[_RoleTeamCdList], "副本记录"]

class LuckAdventure(TypedDict):
    zone: Annotated[str, "大区"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "角色名称"]
    event: Annotated[str, "奇遇名称"]
    level: Annotated[int, "奇遇等级"]
    status: Annotated[int, "奇遇状态"]
    time: Annotated[int, "触发时间"]

class LuckStatistical(TypedDict):
    id: Annotated[int, "奇遇 ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "奇遇名称"]
    event: Annotated[str, "奇遇事件"]
    status: Annotated[int, "奇遇状态"]
    time: Annotated[int, "触发时间"]

class LuckServerStatistical(TypedDict):
    id: Annotated[int, "记录 ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "玩家名称"]
    event: Annotated[str, "奇遇名称"]
    status: Annotated[int, "状态"]
    time: Annotated[int, "时间戳"]

class _LuckCollect(TypedDict):
    name: Annotated[str, "触发角色名称"]
    time: Annotated[int, "触发时间"]

class LuckCollect(TypedDict):
    server: Annotated[str, "区服"]
    event: Annotated[str, "奇遇名称"]
    count: Annotated[int, "触发次数"]
    data: Annotated[_LuckCollect, "触发角色信息"]

class _RoleAchievement(TypedDict):
    id: Annotated[int, "成就ID"]
    icon: Annotated[str, "成就图标"]
    likes: Annotated[int, "点赞数"]
    name: Annotated[str, "成就名称"]
    class_: Annotated[str, "成就分类"]
    subClass: Annotated[str, "成就子分类"]
    desc: Annotated[str, "成就描述"]
    detail: Annotated[str, "成就详情"]
    maps: Annotated[list, "成就地图"]
    isFinished: Annotated[bool, "是否完成"]
    isFav: Annotated[bool, "是否收藏"]
    type: Annotated[str, "成就类型"]
    currentValue: Annotated[int, "当前进度"]
    triggerValue: Annotated[int, "触发进度"]
    subset: Annotated[list, "成就子集"]
    rewardItem: Annotated[str, "成就奖励物品"]
    rewardPoint: Annotated[int, "成就奖励积分"]
    rewardPrefix: Annotated[str, "成就奖励前缀"]
    rewardSuffix: Annotated[str, "成就奖励后缀"]

class RoleAchievement(TypedDict):
    zoneName: Annotated[str, "区服名称"]
    serverName: Annotated[str, "服务器名称"]
    roleName: Annotated[str, "角色名称"]
    roleId: Annotated[int, "角色ID"]
    globalRoleId: Annotated[int, "全局角色ID"]
    forceName: Annotated[str, "门派名称"]
    forceId: Annotated[int, "门派ID"]
    bodyName: Annotated[str, "体型名称"]
    bodyId: Annotated[int, "体型ID"]
    tongName: Annotated[str, "帮会名称"]
    tongId: Annotated[int, "帮会ID"]
    campName: Annotated[str, "阵营名称"]
    campId: Annotated[int, "阵营ID"]
    personName: Annotated[str, "人物名称"]
    personId: Annotated[str, "人物ID"]
    personAvatar: Annotated[str, "人物头像"]
    data: Annotated[Sequence[_RoleAchievement], "成就数据"]

class ArenaRecentPerformance3v3(TypedDict):
    mmr: Annotated[int, "3v3 竞技场 MMR"]
    grade: Annotated[int, "3v3 竞技场 段位"]
    ranking: Annotated[str, "3v3 竞技场 排名"]
    winCount: Annotated[int, "3v3 竞技场 胜场"]
    totalCount: Annotated[int, "3v3 竞技场 总场"]
    mvpCount: Annotated[int, "3v3 竞技场 MVP 次数"]
    pvpType: Annotated[str, "3v3 竞技场 类型"]
    winRate: Annotated[int, "3v3 竞技场 胜率"]

class ArenaRecentHistory(TypedDict):
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    avgGrade: Annotated[int, "平均段位"]
    totalMmr: Annotated[int, "总 MMR"]
    mmr: Annotated[int, "MMR 变动"]
    kungfu: Annotated[str, "门派"]
    pvpType: Annotated[int, "比赛类型"]
    won: Annotated[bool, "是否胜利"]
    mvp: Annotated[bool, "是否 MVP"]
    startTime: Annotated[int, "开始时间"]
    endTime: Annotated[int, "结束时间"]

class ArenaRecentTrend(TypedDict):
    matchDate: Annotated[int, "比赛日期"]
    mmr: Annotated[int, "MMR"]
    winRate: Annotated[float, "胜率"]

class ArenaRecentPerformance(TypedDict, total=False):
    _3v3: ArenaRecentPerformance3v3

class ArenaRecent(TypedDict):
    zoneName: Annotated[str, "区服名称"]
    serverName: Annotated[str, "服务器名称"]
    roleName: Annotated[str, "角色名称"]
    roleId: Annotated[int, "角色 ID"]
    globalRoleId: Annotated[int, "全局角色 ID"]
    forceName: Annotated[str, "门派名称"]
    forceId: Annotated[int, "门派 ID"]
    bodyName: Annotated[str, "体型名称"]
    bodyId: Annotated[int, "体型 ID"]
    tongName: Annotated[str, "帮会名称"]
    tongId: Annotated[int, "帮会 ID"]
    campName: Annotated[str, "阵营名称"]
    campId: Annotated[int, "阵营 ID"]
    personName: Annotated[str, "人物名称"]
    personId: Annotated[str, "人物 ID"]
    personAvatar: Annotated[str, "人物头像"]
    performance: ArenaRecentPerformance
    history: Annotated[Sequence[ArenaRecentHistory], "近期比赛记录"]
    trend: Annotated[Sequence[ArenaRecentTrend], "近期比赛趋势"]

class ArenaAwesome(TypedDict):
    zoneName: Annotated[str, "区服名称"]
    serverName: Annotated[str, "服务器名称"]
    roleName: Annotated[str, "角色名称"]
    forceName: Annotated[str, "门派名称"]
    avatarUrl: Annotated[str, "头像地址"]
    rankNum: Annotated[str, "排名"]
    score: Annotated[str, "积分"]
    upNum: Annotated[str, "上升名次"]
    winRate: Annotated[str, "胜率"]

class ArenaSchools(TypedDict):
    name: Annotated[str, "门派名称"]
    this: Annotated[int, "本周胜场"]
    last: Annotated[int, "上周胜场"]

class _MemberRecruit(TypedDict):
    crossServer: Annotated[bool, "是否跨服"]
    activityId: Annotated[int, "活动ID"]
    activity: Annotated[str, "活动名称"]
    level: Annotated[int, "等级要求"]
    leader: Annotated[str, "队长"]
    pushId: Annotated[int, "推送ID"]
    roomID: Annotated[str, "房间ID"]
    roleId: Annotated[int, "角色ID"]
    createTime: Annotated[int, "创建时间"]
    number: Annotated[int, "当前人数"]
    maxNumber: Annotated[int, "最大人数"]
    label: Annotated[list, "标签"]
    content: Annotated[str, "招募内容"]

class MemberRecruit(TypedDict):
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    time: Annotated[int, "时间戳"]
    data: Annotated[Sequence[_MemberRecruit], "招募信息"]

class _MemberTeacher(TypedDict):
    roleId: Annotated[int, "角色 ID"]
    roleName: Annotated[str, "角色名称"]
    roleLevel: Annotated[int, "角色等级"]
    campName: Annotated[str, "门派名称"]
    tongName: Annotated[str, "帮会名称"]
    tongMasterName: Annotated[str, "帮会会长名称"]
    bodyId: Annotated[int, "体型 ID"]
    bodyName: Annotated[str, "体型名称"]
    forceId: Annotated[int, "门派 ID"]
    forceName: Annotated[str, "势力名称"]
    comment: Annotated[str, "备注"]
    time: Annotated[int, "时间戳"]

class MemberTeacher(TypedDict):
    zone: Annotated[str, "大区"]
    server: Annotated[str, "服务器"]
    data: Annotated[Sequence[_MemberTeacher], "角色列表"]

class _MemberStudent(TypedDict):
    roleId: Annotated[int, "角色 ID"]
    roleName: Annotated[str, "角色名称"]
    roleLevel: Annotated[int, "角色等级"]
    campName: Annotated[str, "阵营名称"]
    tongName: Annotated[str, "帮会名称"]
    tongMasterName: Annotated[str, "帮会会长名称"]
    bodyId: Annotated[int, "体型 ID"]
    bodyName: Annotated[str, "体型名称"]
    forceId: Annotated[int, "门派 ID"]
    forceName: Annotated[str, "门派名称"]
    comment: Annotated[str, "备注"]
    time: Annotated[int, "时间戳"]

class MemberStudent(TypedDict):
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    data: Annotated[Sequence[_MemberStudent], "徒弟列表"]

class _ServerSand(TypedDict):
    tongId: Annotated[int, "帮会ID"]
    tongName: Annotated[str, "帮会名称"]
    castleId: Annotated[int, "据点ID"]
    castleName: Annotated[str, "据点名称"]
    masterId: Annotated[int, "帮主ID"]
    masterName: Annotated[str, "帮主名称"]
    campId: Annotated[int, "阵营ID"]
    campName: Annotated[str, "阵营名称"]

class ServerSand(TypedDict):
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    reset: Annotated[int, "重置时间"]
    update: Annotated[int, "更新时间"]
    data: Annotated[Sequence[_ServerSand], "沙盘信息"]

class ServerEvent(TypedDict):
    id: Annotated[int, "事件ID"]
    camp_name: Annotated[str, "阵营名称"]
    fenxian_zone_name: Annotated[str, "分线区服名称"]
    fenxian_server_name: Annotated[str, "分线服务器名称"]
    friend_zone_name: Annotated[str, "友方区服名称"]
    friend_server_name: Annotated[str, "友方服务器名称"]
    role_name: Annotated[str, "角色名称"]
    add_time: Annotated[int, "添加时间"]

class TableRecords(TypedDict):
    id: Annotated[int, "挂件ID"]
    class_: Annotated[str, "挂件类别"]
    name: Annotated[str, "挂件名称"]
    ui: Annotated[str, "挂件UI"]
    source: Annotated[str, "获取方式"]
    desc: Annotated[str, "挂件描述"]

class TradeDemon(TypedDict):
    id: Annotated[int, "ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    tieba: Annotated[str, "贴吧价格"]
    wanbaolou: Annotated[str, "万宝楼价格"]
    dd373: Annotated[str, "点卡价格"]
    uu898: Annotated[str, "UU价格"]
    _5173: Annotated[str, "5173价格"]
    _7881: Annotated[str, "7881价格"]
    time: Annotated[int, "时间戳"]
    date: Annotated[str, "日期"]

class _TradeRecord(TypedDict):
    id: Annotated[str, "记录ID"]
    index: Annotated[int, "物品索引"]
    zone: Annotated[str, "区服类型"]
    server: Annotated[str, "区服名称"]
    value: Annotated[int, "价格"]
    sales: Annotated[
        int,
        "交易类型，1 = 出售，2 = 收购，3 = 想出，4 = 想收，5 = 成交，6 = 正出，7 = 公示",
    ]
    token: Annotated[str, "站点标识"]
    source: Annotated[int, "数据来源"]
    date: Annotated[str, "日期"]
    status: Annotated[int, "状态"]
    datetime: Annotated[str, "时间"]

class TradeRecords(TypedDict):
    id: Annotated[int, "物品ID"]
    class_: Annotated[str, "物品类别"]
    subclass: Annotated[str, "物品子类别"]
    name: Annotated[str, "物品名称"]
    alias: Annotated[str, "物品别名"]
    subalias: Annotated[str, "物品别名"]
    raw: Annotated[str, "物品行情"]
    level: Annotated[int, "物品等级"]
    desc: Annotated[str, "物品描述"]
    view: Annotated[str, "物品图片"]
    date: Annotated[str, "物品上架日期"]
    data: Annotated[Sequence[Sequence[_TradeRecord]], "物品价格数据"]

class TiebaItemRecords(TypedDict):
    id: Annotated[int, "记录 ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "贴吧名称"]
    url: Annotated[int, "贴吧链接"]
    context: Annotated[str, "帖子内容"]
    reply: Annotated[int, "回复数量"]
    token: Annotated[str, "帖子标识"]
    floor: Annotated[int, "楼层"]
    time: Annotated[int, "发布时间"]

class ValuablesStatistical(TypedDict):
    id: Annotated[int, "记录 ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "物品名称"]
    role_name: Annotated[str, "角色名称"]
    map_name: Annotated[str, "副本名称"]
    time: Annotated[int, "掉落时间"]

class ValuablesServerStatistical(TypedDict):
    id: Annotated[int, "记录ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "物品名称"]
    role_name: Annotated[str, "角色名称"]
    map_name: Annotated[str, "副本名称"]
    time: Annotated[int, "掉落时间"]

class ServerAntivice(TypedDict):
    id: Annotated[int, "事件ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    map_name: Annotated[str, "地图名称"]
    time: Annotated[int, "事件时间"]

class RankStatistical(TypedDict):
    id: Annotated[int, "榜单ID"]
    class_: Annotated[str, "榜单类型"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "角色名"]
    school: Annotated[str, "门派"]
    index: Annotated[int, "排名"]
    level: Annotated[int, "等级"]
    camp_name: Annotated[str, "阵营"]
    tong_name: Annotated[str, "帮会"]
    score: Annotated[int, "分数"]
    datetime: Annotated[str, "时间"]

class RankServerStatistical(TypedDict):
    id: Annotated[int, "榜单ID"]
    class_: Annotated[str, "榜单类型"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "角色名"]
    school: Annotated[str, "门派"]
    index: Annotated[int, "排名"]
    level: Annotated[int, "等级"]
    camp_name: Annotated[str, "阵营"]
    tong_name: Annotated[str, "帮会"]
    score: Annotated[int, "分数"]
    datetime: Annotated[str, "时间"]

class SchoolRankStatistical(TypedDict):
    name: Annotated[str, "玩家名称"]
    role: Annotated[str, "角色名"]
    school: Annotated[str, "门派简称"]
    server: Annotated[str, "区服"]
    zone: Annotated[str, "区服"]
    value: Annotated[int, "资历值"]
    avatar: Annotated[str, "头像地址"]

class _ActiveMonster(TypedDict):
    name: Annotated[str, "首领名称"]
    list: Annotated[list, "特殊效果列表"]
    desc: Annotated[str, "特殊效果描述"]

class ActiveMonsterSkill(TypedDict):
    level: Annotated[int, "首领等级"]
    name: Annotated[str, "首领名称"]
    skill: Annotated[list[str], "首领技能"]
    data: Annotated[_ActiveMonster, "特殊效果"]

class ActiveMonster(TypedDict):
    start: Annotated[int, "活动开始时间戳"]
    end: Annotated[int, "活动结束时间戳"]
    data: Annotated[list[ActiveMonsterSkill], "首领列表"]

class HorseRecords(TypedDict):
    id: Annotated[int, "记录ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "马匹名称"]
    level: Annotated[int, "马匹等级"]
    map_name: Annotated[str, "马匹所在地图"]
    refresh_time: Annotated[int, "刷新时间"]
    capture_role_name: Annotated[str, "捕捉玩家"]
    capture_camp_name: Annotated[str, "捕捉阵营"]
    capture_time: Annotated[int, "捕捉时间"]
    auction_role_name: Annotated[str, "拍卖玩家"]
    auction_camp_name: Annotated[str, "拍卖阵营"]
    auction_time: Annotated[int, "拍卖时间"]
    auction_amount: Annotated[str, "拍卖价格"]
    start_time: Annotated[int, "活动开始时间"]
    end_time: Annotated[int, "活动结束时间"]

class _HorseRanch(TypedDict):
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    data: Annotated[dict[str, Sequence[str]], "马场刷新记录"]
    note: Annotated[str, "备注"]

class HorseRanch(TypedDict):
    code: Annotated[int, "状态码"]
    msg: Annotated[str, "状态信息"]
    data: _HorseRanch
    time: Annotated[int, "时间戳"]

class FireworksRecords(TypedDict):
    id: Annotated[int, "记录ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "角色名称"]
    map_name: Annotated[str, "地图名称"]
    sender: Annotated[str, "发送者"]
    recipient: Annotated[str, "接收者"]
    status: Annotated[int, "状态"]
    time: Annotated[int, "时间戳"]

class FireworksStatistical(TypedDict):
    id: Annotated[int, "烟花ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "烟花名称"]
    map_name: Annotated[str, "地图名称"]
    sender: Annotated[str, "发送者"]
    recipient: Annotated[str, "接收者"]
    mode: Annotated[int, "模式"]
    status: Annotated[int, "状态"]
    time: Annotated[int, "时间"]

class FireworksCollect(TypedDict):
    server: Annotated[str, "区服"]
    sender: Annotated[str, "发送者"]
    recipient: Annotated[str, "接收者"]
    name: Annotated[str, "烟花名称"]
    count: Annotated[int, "烟花数量"]
    time: Annotated[int, "时间戳"]

class FireworksRankStatistical(TypedDict):
    server: Annotated[str, "区服"]
    sender: Annotated[str, "赠送者"]
    recipient: Annotated[str, "接收者"]
    name: Annotated[str, "烟花名称"]
    count: Annotated[int, "数量"]
    time: Annotated[int, "时间戳"]

class ShowCard(TypedDict):
    zoneName: Annotated[str, "区服"]
    serverName: Annotated[str, "服务器"]
    roleName: Annotated[str, "角色名称"]
    showHash: Annotated[str, "名片图片哈希"]
    showAvatar: Annotated[str, "名片图片地址"]
    cacheTime: Annotated[int, "缓存时间戳"]

class ShowCache(TypedDict):
    zoneName: Annotated[str, "区服"]
    serverName: Annotated[str, "服务器"]
    roleName: Annotated[str, "角色名称"]
    showHash: Annotated[str, "名片图片哈希"]
    showAvatar: Annotated[str, "名片图片地址"]
    cacheTime: Annotated[int, "缓存时间戳"]

class ShowRandom(TypedDict):
    server: Annotated[str, "区服"]
    name: Annotated[str, "角色名"]
    avatar: Annotated[str, "头像地址"]
    status: Annotated[int, "状态"]

class MixedChat(TypedDict):
    id: Annotated[int, "聊天记录 ID"]
    answer: Annotated[str, "聊天回复"]

class MusicTencent(TypedDict):
    id: Annotated[str, "歌曲编号"]
    name: Annotated[str, "歌曲名称"]
    singer: Annotated[str, "歌手"]

class MusicNetease(TypedDict):
    id: Annotated[int, "歌曲编号"]
    name: Annotated[str, "歌曲名称"]
    singer: Annotated[str, "歌手"]

class MusicKugou(TypedDict):
    SongName: Annotated[str, "歌曲名称"]
    AlbumID: Annotated[str, "专辑 ID"]
    FileHash: Annotated[str, "文件Hash"]
    SQFileHash: Annotated[str, "SQ文件Hash"]
    HQFileHash: Annotated[str, "HQ文件Hash"]
    MvHash: Annotated[str, "MV Hash"]
    Audioid: Annotated[int, "音频 ID"]
    SingerName: Annotated[str, "歌手名称"]
    PlayUrl: Annotated[str, "播放地址"]
    Img: Annotated[str, "图片地址"]

class FraudDetailedData(TypedDict):
    title: Annotated[str, "帖子标题"]
    tid: Annotated[int, "帖子 ID"]
    text: Annotated[str, "帖子内容"]
    time: Annotated[int, "帖子时间"]

class FraudDetailedRecord(TypedDict):
    server: Annotated[str, "服务器"]
    tieba: Annotated[str, "贴吧"]
    data: Annotated[Sequence[FraudDetailedData], "帖子数据"]

class FraudDetailed(TypedDict):
    records: Annotated[Sequence[FraudDetailedRecord], "骗子记录"]

class IdiomSolitaireQuestion(TypedDict):
    id: Annotated[int, "成语ID"]
    name: Annotated[str, "成语名称"]
    tone: Annotated[str, "成语音调"]
    pinyin: Annotated[str, "成语拼音"]
    abbreviation: Annotated[str, "成语缩写"]
    first: Annotated[str, "成语首字"]
    last: Annotated[str, "成语末字"]
    derivation: Annotated[str, "成语出处"]
    example: Annotated[str, "成语例句"]
    explanation: Annotated[str, "成语解释"]

class IdiomSolitaire(TypedDict):
    question: IdiomSolitaireQuestion

class SaohuaRandom(TypedDict):
    id: Annotated[int, "骚话 ID"]
    text: Annotated[str, "骚话内容"]

class SaohuaContent(TypedDict):
    id: Annotated[int, "舔狗日记 ID"]
    text: Annotated[str, "舔狗日记内容"]

class SoundConverter(TypedDict):
    text: Annotated[str, "合成的内容"]
    token: Annotated[str, "token"]
    url: Annotated[str, "音频地址"]

class JX3API:
    def __init__(
        self,
        *,
        token: Annotated[str | None, "站点标识"] = None,
        ticket: Annotated[str | None, "推栏标识"] = None,
        base_url: str = "https://www.jx3api.com",
    ) -> None:
        pass

    def active_calendar(
        self,
        server: Annotated[str | None, "区服名称，查找该区服的记录。"] = None,
        num: Annotated[
            int,
            "指定日期，查询指定日期的日常，默认值 : ``0`` 为当天，``1`` 为明天，以此类推。",
        ] = 0,
    ) -> Annotated[ActiveCalendar, "今天、明天、后天、日常任务"]:
        """
        active_calendar 活动日历

        今天、明天、后天、日常任务。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。
            num (int, optional): 指定日期，查询指定日期的日常，默认值 : ``0`` 为当天，``1`` 为明天，以此类推。

        Returns:
            ActiveCalendar: 今天、明天、后天、日常任务。
        """
        pass

    def active_celebs(
        self,
        *,
        name: Annotated[str, "名称，查询指定事件的记录"],
    ) -> Annotated[Sequence[ActiveCelebs], "当前时间的楚天社/云从社/披风会进度"]:
        """
        active_celebs 行侠事件

        当前时间的楚天社/云从社/披风会进度。

        Args:
            name (str): 名称，查询指定事件的记录。

        Returns:
            Sequence[ActiveCelebs]: 当前时间的楚天社/云从社/披风会进度。
        """
        pass

    def active_list_calendar(
        self,
        *,
        num: Annotated[
            int, "预测时间，查询指定时间内的月历，默认值 : ``15`` 为前后15天的月历"
        ] = 15,
    ) -> Annotated[ActiveListCalendar, "预测每天的日常任务"]:
        """
        active_list_calendar 活动月历

        预测每天的日常任务。

        Args:
            num (int, optional): 预测时间，查询指定时间内的月历，默认值 : ``15`` 为前后15天的月历。

        Returns:
            ActiveListCalendar: 预测每天的日常任务。
        """
        pass

    def exam_answer(
        self,
        *,
        subject: Annotated[str, "科举试题，支持首字母，支持模糊查询"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Sequence[ExamAnswer], "科举答题"]:
        """
        exam_answer 科举试题

        科举答题

        Args:
            subject (str): 科举试题，支持首字母，支持模糊查询。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[ExamAnswer]: 科举答题。
        """
        pass

    def home_furniture(
        self,
        *,
        name: Annotated[str, "指定装饰，查找该装饰的详细记录"],
    ) -> Annotated[HomeFurniture, "装饰详情"]:
        """
        home_furniture 家园装饰

        装饰详情

        Args:
            name (str): 指定装饰，查找该装饰的详细记录。

        Returns:
            HomeFurniture: 装饰详情。
        """
        pass

    def home_travel(
        self,
        *,
        name: Annotated[str, "地图，查找该地图的装饰产出"],
    ) -> Annotated[Sequence[HomeTravel], "器物谱地图产出装饰"]:
        """
        home_travel 器物图谱

        器物谱地图产出装饰

        Args:
            name (str): 地图，查找该地图的装饰产出。

        Returns:
            Sequence[HomeTravel]: 器物谱地图产出装饰。
        """
        pass

    def news_allnews(
        self,
        *,
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Sequence[NewsAllnews], "官方最新公告及新闻"]:
        """
        news_allnews 新闻资讯

        官方最新公告及新闻

        Args:
            limit (int, optional): 限制查询结果的数量，默认值 10.

        Returns:
            Sequence[NewsAllnews]: 官方最新公告及新闻。
        """
        pass

    def news_announce(
        self,
        *,
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Sequence[NewsAnnounce], "官方最新维护公告"]:
        """
        news_announce 维护公告

        官方最新维护公告

        Args:
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[NewsAnnounce]: 官方最新维护公告。
        """
        pass

    def server_master(
        self,
        *,
        name: Annotated[str, "指定区服，查找该区服的相关记录"],
    ) -> Annotated[ServerMaster, "简称搜索主次服务器"]:
        """
        server_master 搜索区服

        简称搜索主次服务器

        Args:
            name (str): 指定区服，查找该区服的相关记录。

        Returns:
            ServerMaster: 简称搜索主次服务器。
        """
        pass

    def server_check(
        self,
        *,
        server: Annotated[
            str | None,
            "可选的服务器名称，查找该区服的相关记录；未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)",
        ] = None,
    ) -> Annotated[ServerCheck, "服务器当前状态 [ 已开服/维护中 ]"]:
        """
        server_check 开服检查

        服务器当前状态 [ 已开服/维护中 ]

        Args:
            server (str, optional): 可选的服务器名称，查找该区服的相关记录；未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)。

        Returns:
            ServerCheck: 服务器当前状态 [ 已开服/维护中 ]
        """
        pass

    def server_status(
        self,
        *,
        server: Annotated[str, "指定区服，查找该区服的相关记录"],
    ) -> Annotated[ServerStatus, "服务器当前状态"]:
        """
        server_status 查看状态

        服务器当前状态 [ 维护/正常/繁忙/爆满 ]

        Args:
            server (str): 指定区服，查找该区服的相关记录。

        Returns:
            ServerStatus: 服务器当前状态。
        """
        pass

    def home_flower(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str | None, "鲜花，查找该鲜花的相关记录"] = None,
        map: Annotated[str | None, "地图，查找该地图的相关记录"] = None,
    ) -> Annotated[HomeFlower, "家园鲜花最高价格线路"]:
        """
        home_flower 鲜花价格

        家园鲜花最高价格线路。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str, optional): 鲜花，查找该鲜花的相关记录。
            map (str, optional): 地图，查找该地图的相关记录。

        Returns:
            HomeFlowerData: 家园鲜花最高价格线路。
        """
        pass

    ##########
    # VIP  I #
    ##########

    def save_detailed(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        roleid: Annotated[str, "角色UID，保存该角色的详细记录"],
    ) -> Annotated[SaveDetailed, "自动更新角色信息"]:
        """
        save_detailed 角色更新

        自动更新角色信息。

        Args:
            server (str): 区服，查找该区服的相关记录。
            roleid (str): 角色UID，保存该角色的详细记录。

        Returns:
            SaveDetailed: 自动更新角色信息。
        """
        pass

    def role_detailed(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找目标角色的相关记录"],
    ) -> Annotated[RoleDetailed, "角色详细信息"]:
        """
        role_detailed 角色信息

        角色详细信息

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找目标角色的相关记录。

        Returns:
            RoleDetailed: 角色详细信息。
        """
        pass

    def school_matrix(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[SchoolMatrix, "职业阵眼效果"]:
        """
        school_matrix 阵眼效果

        职业阵眼效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            SchoolMatrix: 职业阵眼效果。
        """
        pass

    def school_force(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[Sequence[SchoolForce], "奇穴详细效果"]:
        """
        school_force 奇穴效果

        奇穴详细效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            Sequence[SchoolForce]: 奇穴详细效果。
        """
        pass

    def school_skills(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[Sequence[SchoolSkills], "技能详细效果"]:
        """
        school_skills 技能效果

        技能详细效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            Sequence[SchoolSkills]: 技能详细效果。
        """
        pass

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
    ) -> Annotated[Sequence[TiebaRandom], "随机搜索贴吧 : 818/616...."]:
        """
        tieba_random 八卦帖子

        禁止轮询，随机搜索贴吧 : 818/616....

        Args:
            class (str): 帖子分类，可选范围：``818`` ``616`` ``鬼网三`` ``鬼网3`` ``树洞`` ``记录`` ``教程`` ``街拍`` ``故事`` ``避雷`` ``吐槽`` ``提问``
            server (str, optional): 区服名称，查找该区服的相关记录，默认值：``-`` 为全区服。
            limit (int, optional): 限制查询结果的数量，默认值 ``10``。

        Returns:
            Sequence[TiebaRandom]: 随机搜索贴吧 : 818/616....
        """
        pass

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
        pass

    def role_team_cd_list(
        self,
        *,
        server: Annotated[str, "区服名称，查找该区服的记录"],
        name: Annotated[str, "角色名称，查找该角色的记录"],
    ) -> Annotated[RoleTeamCdList, "角色副本记录"]:
        """
        role_team_cd_list 副本记录

        角色副本记录

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            RoleTeamCdList: 角色副本记录。
        """
        pass

    def luck_adventure(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
    ) -> Annotated[Sequence[LuckAdventure], "角色奇遇触发记录(不保证遗漏)"]:
        """
        luck_adventure 奇遇记录

        角色奇遇触发记录(不保证遗漏)

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。

        Returns:
            Sequence[LuckAdventure]: 角色奇遇触发记录(不保证遗漏)。
        """
        pass

    def luck_statistical(
        self,
        *,
        server: Annotated[str, "区服名称，查找该区服的记录"],
        name: Annotated[str, "奇遇名称，查找该奇遇的记录"],
        limit: Annotated[int, "单页数量，单页返回的数量，默认值 : 20"] = 20,
    ) -> Annotated[Sequence[LuckStatistical], "奇遇近期触发统计"]:
        """
        luck_statistical 奇遇统计

        奇遇近期触发统计

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 奇遇名称，查找该奇遇的记录。
            limit (int, optional): 单页数量，单页返回的数量，默认值 : 20。

        Returns:
            Sequence[LuckStatistical]: 奇遇近期触发统计。
        """
        pass

    def luck_server_statistical(
        self,
        *,
        name: Annotated[str, "奇遇名称，查找该奇遇的全服统计"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Sequence[LuckServerStatistical], "统计全服近期奇遇记录，不区分区服"]:
        """
        luck_server_statistical 全服统计

        统计全服近期奇遇记录，不区分区服。

        Args:
            name (str): 奇遇名称，查找该奇遇的全服统计。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[LuckServerStatistical]: 统计全服近期奇遇记录，不区分区服。
        """
        pass

    def luck_collect(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        num: Annotated[int, "汇总时间，汇总指定天数内的记录，默认值 : 7"] = 7,
    ) -> Annotated[Sequence[LuckCollect], "统计奇遇近期触发角色记录"]:
        """
        luck_collect 奇遇汇总

        统计奇遇近期触发角色记录

        Args:
            server (str): 区服，查找该区服的相关记录。
            num (int, optional): 汇总时间，汇总指定天数内的记录，默认值 : 7。

        Returns:
            Sequence[LuckCollect]: 统计奇遇近期触发角色记录。
        """
        pass

    def role_achievement(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        role: Annotated[str, "角色名称，查找该角色的成就记录"],
        name: Annotated[str, "成就/系列名称，查询该成就/系列的完成进度"],
    ) -> Annotated[RoleAchievement, "角色成就进度"]:
        """
        role_achievement 成就百科

        角色成就进度

        Args:
            server (str): 区服，查找该区服的相关记录。
            role (str): 角色名称，查找该角色的成就记录。
            name (str): 成就/系列名称，查询该成就/系列的完成进度。

        Returns:
            RoleAchievement: 角色成就进度。
        """
        pass

    def arena_recent(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
        mode: Annotated[int | None, "比赛模式，查找该模式的相关记录"] = None,
    ) -> Annotated[ArenaRecent, "角色近期战绩记录"]:
        """
        arena_recent 名剑战绩

        角色近期战绩记录

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。
            mode (int, optional): 比赛模式，查找该模式的相关记录。

        Returns:
            ArenaRecent: 角色近期战绩记录。
        """
        pass

    def arena_awesome(
        self,
        *,
        mode: Annotated[int, "比赛模式，查找该模式的相关记录，默认值 : 33"] = 33,
        limit: Annotated[int, "限制查询结果的数量，默认值 20"] = 20,
    ) -> Annotated[Sequence[ArenaAwesome], "角色近期战绩记录"]:
        """
        arena_awesome 名剑排行

        角色近期战绩记录。

        Args:
            mode (int, optional): 比赛模式，查找该模式的相关记录，默认值 : 33. Defaults to 33.
            limit (int, optional): 限制查询结果的数量，默认值 20。

        Returns:
            Sequence[ArenaAwesome]: 角色近期战绩记录。
        """
        pass

    def arena_schools(
        self,
        *,
        mode: Annotated[int, "比赛模式，查找该模式的相关记录，默认值 : 33"] = 33,
    ) -> Annotated[Sequence[ArenaSchools], "角色近期战绩记录"]:
        """
        arena_schools 名剑统计

        角色近期战绩记录

        Args:
            mode (int, optional): 比赛模式，查找该模式的相关记录，默认值 : 33。

        Returns:
            Sequence[ArenaSchools]: 角色近期战绩记录.
        """
        pass

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
    ) -> Annotated[MemberRecruit, "团队招募信息"]:
        """
        member_recruit 团队招募

        团队招募信息

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，模糊匹配记录，用``=关键字``完全匹配记录。
            table (int, optional): 指定表记录，``1``=``本服+跨服``，``2``=``本服``，``3``=``跨服``，默认值：``1``。

        Returns:
            MemberRecruit: 团队招募信息。
        """
        pass

    def member_teacher(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        keyword: Annotated[str | None, "关键字，查找该关键字的相关记录"] = None,
    ) -> Annotated[MemberTeacher, "师父列表"]:
        """
        member_teacher 师父列表

        客户端师徒系统

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，查找该关键字的相关记录。

        Returns:
            MemberTeacher: 师父列表。
        """
        pass

    def member_student(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        keyword: Annotated[str | None, "关键字，查找该关键字的相关记录"] = None,
    ) -> Annotated[MemberStudent, "徒弟列表"]:
        """
        member_student 徒弟列表

        客户端师徒系统

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，查找该关键字的相关记录。

        Returns:
            MemberStudent: 徒弟列表。
        """
        pass

    def server_sand(
        self, *, server: Annotated[str, "区服，查找该区服的相关记录"]
    ) -> Annotated[ServerSand, "阵营沙盘信息"]:
        """
        server_sand 沙盘信息

        查看阵营沙盘信息。

        Args:
            server (str): 区服，查找该区服的相关记录。

        Returns:
            ServerSand: 阵营沙盘信息。
        """
        pass

    def server_event(
        self,
        *,
        name: Annotated[str | None, "阵营名称，查找该阵营的相关记录"] = None,
        limit: Annotated[int, "限制查询结果的数量，默认值 100", 100],
    ) -> Annotated[Sequence[ServerEvent], "全服阵营大事件"]:
        """
        server_event 阵营事件

        全服阵营大事件

        Args:
            name (str, optional): 阵营名称，查找该阵营的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 100。

        Returns:
            Sequence[ServerEvent]: 全服阵营大事件。
        """
        pass

    def table_records(
        self, *, name: Annotated[str, "指定挂件名称，查找目标挂件的相关信息"]
    ) -> Annotated[Sequence[TableRecords], "查询挂件的效果以及获取方式"]:
        """
        table_records 挂件效果

        查询挂件的效果以及获取方式。

        Args:
            name (str): 指定挂件名称，查找目标挂件的相关信息。

        Returns:
            Sequence[TableRecords]: 查询挂件的效果以及获取方式。
        """
        pass

    def trade_demon(
        self,
        *,
        server: Annotated[str | None, "指定区服，查找该区服的相关记录，可选"] = None,
        limit: Annotated[int, "限制查询结果的数量，默认值 10，可选"] = 10,
    ) -> Annotated[Sequence[TradeDemon], "金价比例信息"]:
        """
        trade_demon 金币比例

        金价比例信息

        Args:
            server (str, optional): 指定区服，查找该区服的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[TradeDemon]: 金价比例信息
        """
        pass

    def trade_records(
        self,
        *,
        name: Annotated[str, "外观名称，查找该外观的记录"],
        server: Annotated[str | None, "区服，查找该区服的相关记录"] = None,
    ) -> Annotated[TradeRecords, "黑市物品价格统计"]:
        """
        trade_records 物品价格

        黑市物品价格统计

        Args:
            name (str): 外观名称，查找该外观的记录。
            server (str, optional): 区服，查找该区服的相关记录。

        Returns:
            TradeRecords: 黑市物品价格统计。
        """
        pass

    def tieba_item_records(
        self,
        *,
        server: Annotated[
            str, "区服，查找该区服的相关记录，默认值：``-`` 为全区服"
        ] = "-",
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 ``10``"] = 10,
    ) -> Annotated[Sequence[TiebaItemRecords], "来自贴吧的外观记录"]:
        """
        tieba_item_records 贴吧记录

        来自贴吧的外观记录。

        Args:
            server (str, optional): 区服，查找该区服的相关记录，默认值：``-`` 为全区服。
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 ``10``。

        Returns:
            Sequence[TiebaItemRecords]: 来自贴吧的外观记录。
        """
        pass

    def valuables_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 20"] = 20,
    ) -> Annotated[Sequence[ValuablesStatistical], "统计副本掉落的贵重物品"]:
        """
        valuables_statistical 掉落统计

        统计副本掉落的贵重物品。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 20。

        Returns:
            Sequence[ValuablesStatistical]: 统计副本掉落的贵重物品。
        """
        pass

    def valuables_server_statistical(
        self,
        *,
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[
        Sequence[ValuablesServerStatistical], "统计当前赛季副本掉落的特殊物品"
    ]:
        """
        valuables_server_statistical 全服掉落

        统计当前赛季副本掉落的特殊物品。

        Args:
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[ValuablesServerStatistical]: 统计当前赛季副本掉落的特殊物品。
        """
        pass

    def server_antivice(
        self, *, server: Annotated[str | None, "服务器"] = None
    ) -> Annotated[Sequence[ServerAntivice], "诛恶事件历史记录(不允许轮询)"]:
        """
        server_antivice 诛恶事件

        诛恶事件历史记录(不允许轮询)

        Args:
            server (str, optional): 服务器。

        Returns:
            Sequence[ServerAntivice]: 诛恶事件历史记录(不允许轮询)。
        """
        pass

    def rank_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        table: Annotated[str, "榜单类型"],
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[Sequence[RankStatistical], "客户端战功榜与风云录"]:
        """
        rank_statistical 风云榜单

        客户端战功榜与风云录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            table (str): 榜单类型。
            name (str): 榜单名称。

        Returns:
            Sequence[RankStatistical]: 客户端战功榜与风云录。
        """
        pass

    def rank_server_statistical(
        self,
        *,
        table: Annotated[str, "榜单类型，个人/帮会/阵营/试炼"],
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[Sequence[RankServerStatistical], "客户端战功榜与风云录"]:
        """
        rank_server_statistical 全服榜单

        客户端战功榜与风云录。

        Args:
            table (str): 榜单类型，个人/帮会/阵营/试炼。
            name (str): 榜单名称。

        Returns:
            Sequence[RankServerStatistical]: 客户端战功榜与风云录。
        """
        pass

    def school_rank_statistical(
        self,
        *,
        school: Annotated[str, "门派简称，查找该心法的相关记录，默认值 : ALL"] = "ALL",
        server: Annotated[str, "指定区服，查找该区服的相关记录，默认值 : ALL"] = "ALL",
    ) -> Annotated[Sequence[SchoolRankStatistical], "游戏资历榜单"]:
        """
        school_rank_statistical 资历榜单

        游戏资历榜单

        Args:
            school (str, optional): 门派简称，查找该心法的相关记录，默认值 : ALL。
            server (str, optional): 指定区服，查找该区服的相关记录，默认值 : ALL。

        Returns:
            Sequence[SchoolRankStatistical]: 游戏资历榜单。
        """
        pass

    ##########
    # VIP II #
    ##########

    def active_monster(
        self,
    ) -> Annotated[ActiveMonster, "本周百战异闻录刷新的首领以及特殊效果"]:
        """
        active_monster 百战首领

        本周百战异闻录刷新的首领以及特殊效果。

        Returns:
            ActiveMonster: 本周百战异闻录刷新的首领以及特殊效果。
        """
        pass

    def horse_records(
        self, *, server: Annotated[str, "可选的服务器，查找该区服的相关记录"]
    ) -> Annotated[Sequence[HorseRecords], "客户端的卢刷新记录"]:
        """
        horse_records 的卢统计

        客户端的卢刷新记录。

        Args:
            server (str): 可选的服务器，查找该区服的相关记录。

        Returns:
            Sequence[HorseRecords]: 客户端的卢刷新记录。
        """
        pass

    def horse_ranch(
        self, *, server: Annotated[str, "区服，查找该区服的相关记录"]
    ) -> Annotated[HorseRanch, "客户端马场刷新记录"]:
        """
        horse_ranch 马场事件

        客户端马场刷新记录。

        Args:
            server (str): 区服，查找该区服的相关记录。

        Returns:
            HorseRanch: 客户端马场刷新记录。
        """
        pass

    def fireworks_records(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
    ) -> Annotated[Sequence[FireworksRecords], "烟花赠送与接收的历史记录，不保证遗漏"]:
        """
        fireworks_records 烟花记录

        烟花赠送与接收的历史记录，不保证遗漏。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。

        Returns:
            Sequence[FireworksRecords]: 烟花赠送与接收的历史记录，不保证遗漏。
        """
        pass

    def fireworks_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "烟花名称，查找该烟花的相关统计"],
        limit: Annotated[int, "单页数量，设置返回的数量，默认值 : 20"] = 20,
    ) -> Annotated[Sequence[FireworksStatistical], "统计烟花记录"]:
        """
        fireworks_statistical 烟花统计

        统计烟花记录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 烟花名称，查找该烟花的相关统计。
            limit (int, optional): 单页数量，设置返回的数量，默认值 : 20。

        Returns:
            Sequence[FireworksStatistical]: 统计烟花记录。
        """
        pass

    def fireworks_collect(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        num: Annotated[int, "统计时间，默认值：7 天"] = 7,
    ) -> Annotated[Sequence[FireworksCollect], "汇总烟花记录"]:
        """
        fireworks_collect 烟花汇总

        汇总烟花记录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            num (int, optional): 统计时间，默认值：7 天。

        Returns:
            Sequence[FireworksCollect]: 汇总烟花记录。
        """
        pass

    def fireworks_rank_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        column: Annotated[str, "可选范围：[sender recipient name]"],
        this_time: Annotated[int, "统计开始的时间，与结束的时间不得超过3个月"],
        that_time: Annotated[int, "统计结束的时间，与开始的时间不得超过3个月"],
    ) -> Annotated[Sequence[FireworksRankStatistical], "烟花赠送与接收的榜单"]:
        """
        fireworks_rank_statistical 烟花排行

        烟花赠送与接收的榜单。

        Args:
            server (str): 区服，查找该区服的相关记录。
            column (str): 可选范围：[sender recipient name]。
            this_time (int): 统计开始的时间，与结束的时间不得超过3个月。
            that_time (int): 统计结束的时间，与开始的时间不得超过3个月。

        Returns:
            Sequence[FireworksRankStatistical]: 烟花赠送与接收的榜单。
        """
        pass

    def show_card(
        self,
        *,
        server: Annotated[str, "目标区服，查找目标区服的相关信息"],
        name: Annotated[str, "角色名称，查找目标角色的相关信息"],
    ) -> Annotated[ShowCard, "客户端的名片墙"]:
        """
        show_card 角色名片

        客户端的名片墙。

        Args:
            server (str): 目标区服，查找目标区服的相关信息。
            name (str): 角色名称，查找目标角色的相关信息。

        Returns:
            ShowCard: 客户端的名片墙。
        """
        pass

    def show_cache(
        self,
        *,
        server: Annotated[str, "目标区服，查找目标区服的相关信息"],
        name: Annotated[str, "角色名称，查找目标角色的相关信息"],
    ) -> Annotated[ShowCache, "客户端的名片墙"]:
        """
        show_cache 名片缓存

        此接口用于查询指定角色的名片墙信息。注意，该接口从缓存中读取数据，非实时更新。建议与装备属性接口搭配使用。。

        Args:
            server (str): 目标区服，查找目标区服的相关信息。
            name (str): 角色名称，查找目标角色的相关信息。

        Returns:
            ShowCache: 客户端的名片墙。
        """
        pass

    def show_random(
        self,
        *,
        server: Annotated[str, "目标区服，查找目标区服的相关信息"],
        body: Annotated[str | None, "角色体型，查找目标体型的相关信息"] = None,
        force: Annotated[str | None, "门派名称，查找目标门派的相关信息"] = None,
    ) -> Annotated[ShowRandom, "客户端的随机名片"]:
        """
        show_random 随机名片

        客户端的随机名片。

        Args:
            server (str): 目标区服，查找目标区服的相关信息。
            body (str, optional): 角色体型，查找目标体型的相关信息。 Defaults to None.
            force (str, optional): 门派名称，查找目标门派的相关信息。 Defaults to None.

        Returns:
            ShowRandom: 客户端的随机名片。
        """
        pass

    def fraud_detailed(
        self, *, uid: Annotated[int, "用户QQ号，查找是否存在行骗记录"]
    ) -> Annotated[FraudDetailed, "搜索贴吧的行骗记录"]:
        """
        fraud_detailed 骗子记录

        搜索贴吧的行骗记录

        Args:
            uid (int): 用户QQ号，查找是否存在行骗记录。

        Returns:
            FraudDetailed: 搜索贴吧的行骗记录。
        """
        pass

    #############
    #    VRF    #
    #############

    def mixed_chat(
        self,
        *,
        name: Annotated[str, "机器人的名称"],
        text: Annotated[str, "聊天的完整内容"],
    ) -> Annotated[MixedChat, "智障聊天"]:
        """
        mixed_chat 智障聊天

        Args:
            name (str): 机器人的名称。
            text (str): 聊天的完整内容。

        Returns:
            MixedChat: 智障聊天。
        """
        pass

    def music_tencent(
        self,
        *,
        name: Annotated[str, "歌曲名称，查找歌曲的编号"],
    ) -> Annotated[Sequence[MusicTencent], "搜索腾讯音乐歌曲编号"]:
        """
        music_tencent 腾讯音乐

        搜索腾讯音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找歌曲的编号。

        Returns:
            Sequence[MusicTencent]: 搜索腾讯音乐歌曲编号。
        """
        pass

    def music_netease(
        self,
        *,
        name: Annotated[str, "歌曲名称，查找该歌曲的编号"],
    ) -> Annotated[Sequence[MusicNetease], "搜索网易云音乐歌曲编号"]:
        """
        music_netease 网易音乐

        搜索网易云音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找该歌曲的编号。

        Returns:
            Sequence[MusicNetease]: 搜索网易云音乐歌曲编号。
        """
        pass

    def music_kugou(
        self,
        *,
        name: Annotated[str, "歌曲名称，查找该歌曲的编号"],
    ) -> Annotated[Sequence[MusicKugou], "搜索酷狗音乐歌曲编号"]:
        """
        music_kugou 酷狗音乐

        搜索酷狗音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找该歌曲的编号。

        Returns:
            Sequence[MusicKugou]: 搜索酷狗音乐歌曲编号。
        """
        pass

    def idiom_solitaire(
        self, *, name: Annotated[str, "查找对应词语"]
    ) -> Annotated[IdiomSolitaire, "校对成语并返回相关成语"]:
        """
        idiom_solitaire 成语接龙

        校对成语并返回相关成语

        Args:
            name (str): 查找对应词语。

        Returns:
            IdiomSolitaire: 校对成语并返回相关成语。
        """
        pass

    def saohua_random(
        self,
    ) -> Annotated[SaohuaRandom, "万花门派骚话"]:
        """
        saohua_random 撩人骚话

        万花门派骚话

        Returns:
            SaohuaRandom: 万花门派骚话
        """
        pass

    def saohua_content(self) -> Annotated[SaohuaContent, "召唤一条舔狗日记"]:
        """
        saohua_content 舔狗日记

        召唤一条舔狗日记。

        Returns:
            SaohuaContent: 召唤一条舔狗日记。
        """
        pass

    def sound_converter(
        self,
        *,
        appkey: Annotated[str, "阿里云身份识别 appkey"],
        access: Annotated[str, "阿里云身份识别 access"],
        secret: Annotated[str, "阿里云身份识别 secret"],
        text: Annotated[str, "合成的内容"],
        voice: Annotated[Literal["Aitong"], "发音人，默认值 Aitong"] = "Aitong",
        format: Annotated[
            Literal["PCM", "WAV", "MP3"], "编码格式，范围 PCM, WAV, MP3，默认值 MP3"
        ] = "MP3",
        sample_rate: Annotated[int, "采样率，默认值 16000"] = 16000,
        volume: Annotated[int, "音量，范围 0～100，默认值 50"] = 50,
        speech_rate: Annotated[int, "语速，范围 -500～500，默认值 0"] = 0,
        pitch_rate: Annotated[int, "音调，范围 -500～500，默认值 0"] = 0,
    ) -> Annotated[SoundConverter, "阿里云语音合成（TTS）"]:
        """
        sound_converter 语音合成

        阿里云语音合成（TTS）

        Args:
            appkey (str): 阿里云身份识别 appkey。
            access (str): 阿里云身份识别 access。
            secret (str): 阿里云身份识别 secret。
            text (str): 合成的内容。
            voice (Literal["Aitong"], optional): 发音人，默认值 Aitong。 Defaults to "Aitong".
            format (Literal["PCM", "WAV", "MP3"], optional): 编码格式，范围 PCM, WAV, MP3，默认值 MP3。 Defaults to "MP3".
            sample_rate (int, optional): 采样率，默认值 16000。 Defaults to 16000.
            volume (int, optional): 音量，范围 0～100，默认值 50。 Defaults to 50.
            speech_rate (int, optional): 语速，范围 -500～500，默认值 0。 Defaults to 0.
            pitch_rate (int, optional): 音调，范围 -500～500，默认值 0。 Defaults to 0.

        Returns:
            SoundConverter: 阿里云语音合成（TTS）。
        """
        pass

class AsyncJX3API:
    def __init__(
        self,
        *,
        token: Annotated[str | None, "站点标识"] = None,
        ticket: Annotated[str | None, "推栏标识"] = None,
        base_url: str = "https://www.jx3api.com",
    ) -> None:
        pass

    async def active_calendar(
        self,
        *,
        server: Annotated[str | None, "区服名称，查找该区服的记录。"] = None,
        num: Annotated[
            int,
            "指定日期，查询指定日期的日常，默认值 : ``0`` 为当天，``1`` 为明天，以此类推。",
        ] = 0,
    ) -> Annotated[Awaitable[ActiveCalendar], "今天、明天、后天、日常任务"]:
        """
        active_calendar 活动日历

        今天、明天、后天、日常任务。

        Args:
            server (str, optional): 区服名称，查找该区服的记录。
            num (int, optional): 指定日期，查询指定日期的日常，默认值 : ``0`` 为当天，``1`` 为明天，以此类推。

        Returns:
            Awaitable[ActiveCalendar]: 今天、明天、后天、日常任务。
        """
        pass

    async def active_celebs(
        self,
        *,
        name: Annotated[str, "名称，查询指定事件的记录"],
    ) -> Annotated[
        Awaitable[Sequence[ActiveCelebs]], "当前时间的楚天社/云从社/披风会进度"
    ]:
        """
        active_celebs 行侠事件

        当前时间的楚天社/云从社/披风会进度。

        Args:
            name (str): 名称，查询指定事件的记录。

        Returns:
            Awaitable[Sequence[ActiveCelebs]]: 当前时间的楚天社/云从社/披风会进度。
        """
        pass

    async def active_list_calendar(
        self,
        *,
        num: Annotated[
            int, "预测时间，查询指定时间内的月历，默认值 : ``15`` 为前后15天的月历"
        ] = 15,
    ) -> Annotated[Awaitable[ActiveListCalendar], "预测每天的日常任务"]:
        """
        active_list_calendar 活动月历

        预测每天的日常任务。

        Args:
            num (int, optional): 预测时间，查询指定时间内的月历，默认值 : ``15`` 为前后15天的月历。

        Returns:
            Awaitable[ActiveListCalendar]: 预测每天的日常任务。
        """
        pass

    async def exam_answer(
        self,
        *,
        subject: Annotated[str, "科举试题，支持首字母，支持模糊查询"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Awaitable[Sequence[ExamAnswer]], "科举答题"]:
        """
        exam_answer 科举试题

        科举答题

        Args:
            subject (str): 科举试题，支持首字母，支持模糊查询。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Awaitable[Sequence[ExamAnswer]]: 科举答题。
        """
        pass

    async def home_furniture(
        self,
        *,
        name: Annotated[str, "指定装饰，查找该装饰的详细记录"],
    ) -> Annotated[Awaitable[HomeFurniture], "装饰详情"]:
        """
        home_furniture 家园装饰

        装饰详情

        Args:
            name (str): 指定装饰，查找该装饰的详细记录。

        Returns:
            Awaitable[HomeFurniture]: 装饰详情。
        """
        pass

    async def home_travel(
        self,
        *,
        name: Annotated[str, "地图，查找该地图的装饰产出"],
    ) -> Annotated[Awaitable[Sequence[HomeTravel]], "器物谱地图产出装饰"]:
        """
        home_travel 器物图谱

        器物谱地图产出装饰

        Args:
            name (str): 地图，查找该地图的装饰产出。

        Returns:
            Awaitable[Sequence[HomeTravel]]: 器物谱地图产出装饰。
        """
        pass

    async def news_allnews(
        self,
        *,
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Awaitable[Sequence[NewsAllnews]], "官方最新公告及新闻"]:
        """
        news_allnews 新闻资讯

        官方最新公告及新闻

        Args:
            limit (int, optional): 限制查询结果的数量，默认值 10.

        Returns:
            Awaitable[Sequence[NewsAllnews]]: 官方最新公告及新闻。
        """
        pass

    async def news_announce(
        self,
        *,
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[Awaitable[Sequence[NewsAnnounce]], "官方最新维护公告"]:
        """
        news_announce 维护公告

        官方最新维护公告

        Args:
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Awaitable[Sequence[NewsAnnounce]]: 官方最新维护公告。
        """
        pass

    async def server_master(
        self,
        *,
        name: Annotated[str, "指定区服，查找该区服的相关记录"],
    ) -> Annotated[Awaitable[ServerMaster], "简称搜索主次服务器"]:
        """
        server_master 搜索区服

        简称搜索主次服务器

        Args:
            name (str): 指定区服，查找该区服的相关记录。

        Returns:
            Awaitable[ServerMaster]: 简称搜索主次服务器。
        """
        pass

    async def server_check(
        self,
        *,
        server: Annotated[
            str | None,
            "可选的服务器名称，查找该区服的相关记录；未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)",
        ] = None,
    ) -> Annotated[Awaitable[ServerCheck], "服务器当前状态 [ 已开服/维护中 ]"]:
        """
        server_check 开服检查

        服务器当前状态 [ 已开服/维护中 ]

        Args:
            server (str, optional): 可选的服务器名称，查找该区服的相关记录；未输入区服名称或输入错误区服名称时，将返回全部区服的状态数据，可用于开服监控(支持轮询请求)。

        Returns:
            Awaitable[ServerCheck]: 服务器当前状态 [ 已开服/维护中 ]
        """
        pass

    async def server_status(
        self,
        *,
        server: Annotated[str, "指定区服，查找该区服的相关记录"],
    ) -> Annotated[Awaitable[ServerStatus], "服务器当前状态"]:
        """
        server_status 查看状态

        服务器当前状态 [ 维护/正常/繁忙/爆满 ]

        Args:
            server (str): 指定区服，查找该区服的相关记录。

        Returns:
            Awaitable[ServerStatus]: 服务器当前状态。
        """
        pass

    async def home_flower(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str | None, "鲜花，查找该鲜花的相关记录"] = None,
        map: Annotated[str | None, "地图，查找该地图的相关记录"] = None,
    ) -> Annotated[Awaitable[HomeFlower], "家园鲜花最高价格线路"]:
        """
        home_flower 鲜花价格

        家园鲜花最高价格线路。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str, optional): 鲜花，查找该鲜花的相关记录。
            map (str, optional): 地图，查找该地图的相关记录。

        Returns:
            Awaitable[HomeFlowerData]: 家园鲜花最高价格线路。
        """
        pass

    ##########
    # VIP  I #
    ##########

    async def save_detailed(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        roleid: Annotated[str, "角色UID，保存该角色的详细记录"],
    ) -> Annotated[Awaitable[SaveDetailed], "自动更新角色信息"]:
        """
        save_detailed 角色更新

        自动更新角色信息。

        Args:
            server (str): 区服，查找该区服的相关记录。
            roleid (str): 角色UID，保存该角色的详细记录。

        Returns:
            Awaitable[SaveDetailed]: 自动更新角色信息。
        """
        pass

    async def role_detailed(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找目标角色的相关记录"],
    ) -> Annotated[Awaitable[RoleDetailed], "角色详细信息"]:
        """
        role_detailed 角色信息

        角色详细信息

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找目标角色的相关记录。

        Returns:
            Awaitable[RoleDetailed]: 角色详细信息。
        """
        pass

    async def school_matrix(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[Awaitable[SchoolMatrix], "职业阵眼效果"]:
        """
        school_matrix 阵眼效果

        职业阵眼效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            Awaitable[SchoolMatrix]: 职业阵眼效果。
        """
        pass

    async def school_force(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[Awaitable[Sequence[SchoolForce]], "奇穴详细效果"]:
        """
        school_force 奇穴效果

        奇穴详细效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            Awaitable[Sequence[SchoolForce]]: 奇穴详细效果。
        """
        pass

    async def school_skills(
        self, *, name: Annotated[str, "心法名称，查找该心法的相关记录"]
    ) -> Annotated[Awaitable[Sequence[SchoolSkills]], "技能详细效果"]:
        """
        school_skills 技能效果

        技能详细效果

        Args:
            name (str): 心法名称，查找该心法的相关记录。

        Returns:
            Awaitable[Sequence[SchoolSkills]]: 技能详细效果。
        """
        pass

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
    ) -> Annotated[Awaitable[Sequence[TiebaRandom]], "随机搜索贴吧 : 818/616...."]:
        """
        tieba_random 八卦帖子

        禁止轮询，随机搜索贴吧 : 818/616....

        Args:
            class (str): 帖子分类，可选范围：``818`` ``616`` ``鬼网三`` ``鬼网3`` ``树洞`` ``记录`` ``教程`` ``街拍`` ``故事`` ``避雷`` ``吐槽`` ``提问``
            server (str, optional): 区服名称，查找该区服的相关记录，默认值：``-`` 为全区服。
            limit (int, optional): 限制查询结果的数量，默认值 ``10``。

        Returns:
            Awaitable[Sequence[TiebaRandom]]: 随机搜索贴吧 : 818/616....
        """
        pass

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
        pass

    async def role_team_cd_list(
        self,
        *,
        server: Annotated[str, "区服名称，查找该区服的记录"],
        name: Annotated[str, "角色名称，查找该角色的记录"],
    ) -> Annotated[Awaitable[RoleTeamCdList], "角色副本记录"]:
        """
        role_team_cd_list 副本记录

        角色副本记录

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 角色名称，查找该角色的记录。

        Returns:
            Awaitable[RoleTeamCdList]: 角色副本记录。
        """
        pass

    async def luck_adventure(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
    ) -> Annotated[Awaitable[Sequence[LuckAdventure]], "角色奇遇触发记录(不保证遗漏)"]:
        """
        luck_adventure 奇遇记录

        角色奇遇触发记录(不保证遗漏)

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。

        Returns:
            Awaitable[Sequence[LuckAdventure]]: 角色奇遇触发记录(不保证遗漏)。
        """
        pass

    async def luck_statistical(
        self,
        *,
        server: Annotated[str, "区服名称，查找该区服的记录"],
        name: Annotated[str, "奇遇名称，查找该奇遇的记录"],
        limit: Annotated[int, "单页数量，单页返回的数量，默认值 : 20"] = 20,
    ) -> Annotated[Awaitable[Sequence[LuckStatistical]], "奇遇近期触发统计"]:
        """
        luck_statistical 奇遇统计

        奇遇近期触发统计

        Args:
            server (str): 区服名称，查找该区服的记录。
            name (str): 奇遇名称，查找该奇遇的记录。
            limit (int, optional): 单页数量，单页返回的数量，默认值 : 20。

        Returns:
            Awaitable[Sequence[LuckStatistical]]: 奇遇近期触发统计。
        """
        pass

    async def luck_server_statistical(
        self,
        *,
        name: Annotated[str, "奇遇名称，查找该奇遇的全服统计"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[
        Awaitable[Sequence[LuckServerStatistical]],
        "统计全服近期奇遇记录，不区分区服",
    ]:
        """
        luck_server_statistical 全服统计

        统计全服近期奇遇记录，不区分区服。

        Args:
            name (str): 奇遇名称，查找该奇遇的全服统计。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Awaitable[Sequence[LuckServerStatistical]]: 统计全服近期奇遇记录，不区分区服。
        """
        pass

    async def luck_collect(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        num: Annotated[int, "汇总时间，汇总指定天数内的记录，默认值 : 7"] = 7,
    ) -> Annotated[Awaitable[Sequence[LuckCollect]], "统计奇遇近期触发角色记录"]:
        """
        luck_collect 奇遇汇总

        统计奇遇近期触发角色记录

        Args:
            server (str): 区服，查找该区服的相关记录。
            num (int, optional): 汇总时间，汇总指定天数内的记录，默认值 : 7。

        Returns:
            Awaitable[Sequence[LuckCollect]]: 统计奇遇近期触发角色记录。
        """
        pass

    async def role_achievement(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        role: Annotated[str, "角色名称，查找该角色的成就记录"],
        name: Annotated[str, "成就/系列名称，查询该成就/系列的完成进度"],
    ) -> Annotated[Awaitable[RoleAchievement], "角色成就进度"]:
        """
        role_achievement 成就百科

        角色成就进度

        Args:
            server (str): 区服，查找该区服的相关记录。
            role (str): 角色名称，查找该角色的成就记录。
            name (str): 成就/系列名称，查询该成就/系列的完成进度。

        Returns:
            Awaitable[RoleAchievement]: 角色成就进度。
        """
        pass

    async def arena_recent(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
        mode: Annotated[int | None, "比赛模式，查找该模式的相关记录"] = None,
    ) -> Annotated[Awaitable[ArenaRecent], "角色近期战绩记录"]:
        """
        arena_recent 名剑战绩

        角色近期战绩记录

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。
            mode (int, optional): 比赛模式，查找该模式的相关记录。

        Returns:
            Awaitable[ArenaRecent]: 角色近期战绩记录。
        """
        pass

    async def arena_awesome(
        self,
        *,
        mode: Annotated[int, "比赛模式，查找该模式的相关记录，默认值 : 33"] = 33,
        limit: Annotated[int, "限制查询结果的数量，默认值 20"] = 20,
    ) -> Annotated[Awaitable[Sequence[ArenaAwesome]], "角色近期战绩记录"]:
        """
        arena_awesome 名剑排行

        角色近期战绩记录。

        Args:
            mode (int, optional): 比赛模式，查找该模式的相关记录，默认值 : 33. Defaults to 33.
            limit (int, optional): 限制查询结果的数量，默认值 20。

        Returns:
            Awaitable[Sequence[ArenaAwesome]]: 角色近期战绩记录。
        """
        pass

    async def arena_schools(
        self,
        *,
        mode: Annotated[int, "比赛模式，查找该模式的相关记录，默认值 : 33"] = 33,
    ) -> Annotated[Awaitable[Sequence[ArenaSchools]], "角色近期战绩记录"]:
        """
        arena_schools 名剑统计

        角色近期战绩记录

        Args:
            mode (int, optional): 比赛模式，查找该模式的相关记录，默认值 : 33。

        Returns:
            Awaitable[Sequence[ArenaSchools]]: 角色近期战绩记录.
        """
        pass

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
    ) -> Annotated[Awaitable[MemberRecruit], "团队招募信息"]:
        """
        member_recruit 团队招募

        团队招募信息

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，模糊匹配记录，用``=关键字``完全匹配记录。
            table (int, optional): 指定表记录，``1``=``本服+跨服``，``2``=``本服``，``3``=``跨服``，默认值：``1``。

        Returns:
            Awaitable[MemberRecruit]: 团队招募信息。
        """
        pass

    async def member_teacher(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        keyword: Annotated[str | None, "关键字，查找该关键字的相关记录"] = None,
    ) -> Annotated[Awaitable[MemberTeacher], "师父列表"]:
        """
        member_teacher 师父列表

        客户端师徒系统

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，查找该关键字的相关记录。

        Returns:
            Awaitable[MemberTeacher]: 师父列表。
        """
        pass

    async def member_student(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        keyword: Annotated[str | None, "关键字，查找该关键字的相关记录"] = None,
    ) -> Annotated[Awaitable[MemberStudent], "徒弟列表"]:
        """
        member_student 徒弟列表

        客户端师徒系统

        Args:
            server (str): 区服，查找该区服的相关记录。
            keyword (str, optional): 关键字，查找该关键字的相关记录。

        Returns:
            Awaitable[MemberStudent]: 徒弟列表。
        """
        pass

    async def server_sand(
        self, *, server: Annotated[str, "区服，查找该区服的相关记录"]
    ) -> Annotated[Awaitable[ServerSand], "阵营沙盘信息"]:
        """
        server_sand 沙盘信息

        查看阵营沙盘信息。

        Args:
            server (str): 区服，查找该区服的相关记录。

        Returns:
            Awaitable[ServerSand]: 阵营沙盘信息。
        """
        pass

    async def server_event(
        self,
        *,
        name: Annotated[str | None, "阵营名称，查找该阵营的相关记录"] = None,
        limit: Annotated[int, "限制查询结果的数量，默认值 100", 100],
    ) -> Annotated[Awaitable[Sequence[ServerEvent]], "全服阵营大事件"]:
        """
        server_event 阵营事件

        全服阵营大事件

        Args:
            name (str, optional): 阵营名称，查找该阵营的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 100。

        Returns:
            Awaitable[Sequence[ServerEvent]]: 全服阵营大事件。
        """
        pass

    async def table_records(
        self, *, name: Annotated[str, "指定挂件名称，查找目标挂件的相关信息"]
    ) -> Annotated[Awaitable[Sequence[TableRecords]], "查询挂件的效果以及获取方式"]:
        """
        table_records 挂件效果

        查询挂件的效果以及获取方式。

        Args:
            name (str): 指定挂件名称，查找目标挂件的相关信息。

        Returns:
            Awaitable[Sequence[TableRecords]]: 查询挂件的效果以及获取方式。
        """
        pass

    async def trade_demon(
        self,
        *,
        server: Annotated[str | None, "指定区服，查找该区服的相关记录，可选"] = None,
        limit: Annotated[int, "限制查询结果的数量，默认值 10，可选"] = 10,
    ) -> Annotated[Awaitable[Sequence[TradeDemon]], "金价比例信息"]:
        """
        trade_demon 金币比例

        金价比例信息

        Args:
            server (str, optional): 指定区服，查找该区服的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Sequence[TradeDemon]: 金价比例信息
        """
        pass

    async def trade_records(
        self,
        *,
        name: Annotated[str, "外观名称，查找该外观的记录"],
        server: Annotated[str | None, "区服，查找该区服的相关记录"] = None,
    ) -> Annotated[Awaitable[TradeRecords], "黑市物品价格统计"]:
        """
        trade_records 物品价格

        黑市物品价格统计

        Args:
            name (str): 外观名称，查找该外观的记录。
            server (str, optional): 区服，查找该区服的相关记录。

        Returns:
            TradeRecords: 黑市物品价格统计。
        """
        pass

    async def tieba_item_records(
        self,
        *,
        server: Annotated[
            str, "区服，查找该区服的相关记录，默认值：``-`` 为全区服"
        ] = "-",
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 ``10``"] = 10,
    ) -> Annotated[Awaitable[Sequence[TiebaItemRecords]], "来自贴吧的外观记录"]:
        """
        tieba_item_records 贴吧记录

        来自贴吧的外观记录。

        Args:
            server (str, optional): 区服，查找该区服的相关记录，默认值：``-`` 为全区服。
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 ``10``。

        Returns:
            Awaitable[Sequence[TiebaItemRecords]]: 来自贴吧的外观记录。
        """
        pass

    async def valuables_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 20"] = 20,
    ) -> Annotated[Awaitable[Sequence[ValuablesStatistical]], "统计副本掉落的贵重物品"]:
        """
        valuables_statistical 掉落统计

        统计副本掉落的贵重物品。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 20。

        Returns:
            Awaitable[Sequence[ValuablesStatistical]]: 统计副本掉落的贵重物品。
        """
        pass

    async def valuables_server_statistical(
        self,
        *,
        name: Annotated[str, "物品名称，查找该物品的相关记录"],
        limit: Annotated[int, "限制查询结果的数量，默认值 10"] = 10,
    ) -> Annotated[
        Awaitable[Sequence[ValuablesServerStatistical]],
        "统计当前赛季副本掉落的特殊物品",
    ]:
        """
        valuables_server_statistical 全服掉落

        统计当前赛季副本掉落的特殊物品。

        Args:
            name (str): 物品名称，查找该物品的相关记录。
            limit (int, optional): 限制查询结果的数量，默认值 10。

        Returns:
            Awaitable[Sequence[ValuablesServerStatistical]]: 统计当前赛季副本掉落的特殊物品。
        """
        pass

    async def server_antivice(
        self, *, server: Annotated[str | None, "服务器"] = None
    ) -> Annotated[Awaitable[Sequence[ServerAntivice]], "诛恶事件历史记录(不允许轮询)"]:
        """
        server_antivice 诛恶事件

        诛恶事件历史记录(不允许轮询)

        Args:
            server (str, optional): 服务器。

        Returns:
            Awaitable[Sequence[ServerAntivice]]: 诛恶事件历史记录(不允许轮询)。
        """
        pass

    async def rank_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        table: Annotated[str, "榜单类型"],
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[Awaitable[Sequence[RankStatistical]], "客户端战功榜与风云录"]:
        """
        rank_statistical 风云榜单

        客户端战功榜与风云录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            table (str): 榜单类型。
            name (str): 榜单名称。

        Returns:
            Awaitable[Sequence[RankStatistical]]: 客户端战功榜与风云录。
        """
        pass

    async def rank_server_statistical(
        self,
        *,
        table: Annotated[str, "榜单类型，个人/帮会/阵营/试炼"],
        name: Annotated[str, "榜单名称"],
    ) -> Annotated[Awaitable[Sequence[RankServerStatistical]], "客户端战功榜与风云录"]:
        """
        rank_server_statistical 全服榜单

        客户端战功榜与风云录。

        Args:
            table (str): 榜单类型，个人/帮会/阵营/试炼。
            name (str): 榜单名称。
            token (str): 站点标识，检查请求权限。

        Returns:
            Awaitable[Sequence[RankServerStatistical]]: 客户端战功榜与风云录。
        """
        pass

    async def school_rank_statistical(
        self,
        *,
        school: Annotated[str, "门派简称，查找该心法的相关记录，默认值 : ALL"] = "ALL",
        server: Annotated[str, "指定区服，查找该区服的相关记录，默认值 : ALL"] = "ALL",
    ) -> Annotated[Awaitable[Sequence[SchoolRankStatistical]], "游戏资历榜单"]:
        """
        school_rank_statistical 资历榜单

        游戏资历榜单

        Args:
            school (str, optional): 门派简称，查找该心法的相关记录，默认值 : ALL。
            server (str, optional): 指定区服，查找该区服的相关记录，默认值 : ALL。

        Returns:
            Awaitable[Sequence[SchoolRankStatistical]]: 游戏资历榜单。
        """
        pass

    async def fraud_detailed(
        self, *, uid: Annotated[int, "用户QQ号，查找是否存在行骗记录"]
    ) -> Annotated[Awaitable[FraudDetailed], "搜索贴吧的行骗记录"]:
        """
        fraud_detailed 骗子记录

        搜索贴吧的行骗记录

        Args:
            uid (int): 用户QQ号，查找是否存在行骗记录。

        Returns:
            Awaitable[FraudDetailed]: 搜索贴吧的行骗记录。
        """
        pass

    ##########
    # VIP II #
    ##########

    async def active_monster(
        self,
    ) -> Annotated[Awaitable[ActiveMonster], "本周百战异闻录刷新的首领以及特殊效果"]:
        """
        active_monster 百战首领

        本周百战异闻录刷新的首领以及特殊效果。

        Returns:
            Awaitable[ActiveMonster]: 本周百战异闻录刷新的首领以及特殊效果。
        """
        pass

    async def horse_records(
        self, *, server: Annotated[str, "可选的服务器，查找该区服的相关记录"]
    ) -> Annotated[Awaitable[Sequence[HorseRecords]], "客户端的卢刷新记录"]:
        """
        horse_records 的卢统计

        客户端的卢刷新记录。

        Args:
            server (str): 可选的服务器，查找该区服的相关记录。

        Returns:
            Awaitable[Sequence[HorseRecords]]: 客户端的卢刷新记录。
        """
        pass

    async def horse_ranch(
        self, *, server: Annotated[str, "区服，查找该区服的相关记录"]
    ) -> Annotated[Awaitable[HorseRanch], "客户端马场刷新记录"]:
        """
        horse_ranch 马场事件

        客户端马场刷新记录。

        Args:
            server (str): 区服，查找该区服的相关记录。

        Returns:
            Awaitable[HorseRanch]: 客户端马场刷新记录。
        """
        pass

    async def fireworks_records(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "角色名称，查找该角色的相关记录"],
    ) -> Annotated[
        Awaitable[Sequence[FireworksRecords]],
        "烟花赠送与接收的历史记录，不保证遗漏",
    ]:
        """
        fireworks_records 烟花记录

        烟花赠送与接收的历史记录，不保证遗漏。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 角色名称，查找该角色的相关记录。

        Returns:
            Awaitable[Sequence[FireworksRecords]]: 烟花赠送与接收的历史记录，不保证遗漏。
        """
        pass

    async def fireworks_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        name: Annotated[str, "烟花名称，查找该烟花的相关统计"],
        limit: Annotated[int, "单页数量，设置返回的数量，默认值 : 20"] = 20,
    ) -> Annotated[Awaitable[Sequence[FireworksStatistical]], "统计烟花记录"]:
        """
        fireworks_statistical 烟花统计

        统计烟花记录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            name (str): 烟花名称，查找该烟花的相关统计。
            limit (int, optional): 单页数量，设置返回的数量，默认值 : 20。

        Returns:
            Awaitable[Sequence[FireworksStatistical]]: 统计烟花记录。
        """
        pass

    async def fireworks_collect(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        num: Annotated[int, "统计时间，默认值：7 天"] = 7,
    ) -> Annotated[Awaitable[Sequence[FireworksCollect]], "汇总烟花记录"]:
        """
        fireworks_collect 烟花汇总

        汇总烟花记录。

        Args:
            server (str): 区服，查找该区服的相关记录。
            num (int, optional): 统计时间，默认值：7 天。

        Returns:
            Awaitable[Sequence[FireworksCollect]]: 汇总烟花记录。
        """
        pass

    async def fireworks_rank_statistical(
        self,
        *,
        server: Annotated[str, "区服，查找该区服的相关记录"],
        column: Annotated[str, "可选范围：[sender recipient name]"],
        this_time: Annotated[int, "统计开始的时间，与结束的时间不得超过3个月"],
        that_time: Annotated[int, "统计结束的时间，与开始的时间不得超过3个月"],
    ) -> Annotated[
        Awaitable[Sequence[FireworksRankStatistical]], "烟花赠送与接收的榜单"
    ]:
        """
        fireworks_rank_statistical 烟花排行

        烟花赠送与接收的榜单。

        Args:
            server (str): 区服，查找该区服的相关记录。
            column (str): 可选范围：[sender recipient name]。
            this_time (int): 统计开始的时间，与结束的时间不得超过3个月。
            that_time (int): 统计结束的时间，与开始的时间不得超过3个月。

        Returns:
            Awaitable[Sequence[FireworksRankStatistical]]: 烟花赠送与接收的榜单。
        """
        pass

    async def show_card(
        self,
        *,
        server: Annotated[str, "目标区服，查找目标区服的相关信息"],
        name: Annotated[str, "角色名称，查找目标角色的相关信息"],
    ) -> Annotated[Awaitable[ShowCard], "客户端的名片墙"]:
        """
        show_card 角色名片

        客户端的名片墙。

        Args:
            server (str): 目标区服，查找目标区服的相关信息。
            name (str): 角色名称，查找目标角色的相关信息。

        Returns:
            Awaitable[ShowCard]: 客户端的名片墙。
        """
        pass

    async def show_cache(
        self,
        *,
        server: Annotated[str, "目标区服，查找目标区服的相关信息"],
        name: Annotated[str, "角色名称，查找目标角色的相关信息"],
    ) -> Annotated[ShowCache, "客户端的名片墙"]:
        """
        show_cache 名片缓存

        此接口用于查询指定角色的名片墙信息。注意，该接口从缓存中读取数据，非实时更新。建议与装备属性接口搭配使用。。

        Args:
            server (str): 目标区服，查找目标区服的相关信息。
            name (str): 角色名称，查找目标角色的相关信息。

        Returns:
            Awaitable[ShowCache]: 客户端的名片墙。
        """
        pass

    async def show_random(
        self,
        *,
        server: Annotated[str, "目标区服，查找目标区服的相关信息"],
        body: Annotated[str | None, "角色体型，查找目标体型的相关信息"] = None,
        force: Annotated[str | None, "门派名称，查找目标门派的相关信息"] = None,
    ) -> Annotated[Awaitable[ShowRandom], "客户端的随机名片"]:
        """
        show_random 随机名片

        客户端的随机名片。

        Args:
            server (str): 目标区服，查找目标区服的相关信息。
            body (str, optional): 角色体型，查找目标体型的相关信息。 Defaults to None.
            force (str, optional): 门派名称，查找目标门派的相关信息。 Defaults to None.

        Returns:
            Awaitable[ShowRandom]: 客户端的随机名片。
        """
        pass

    #############
    #    VRF    #
    #############

    async def mixed_chat(
        self,
        *,
        name: Annotated[str, "机器人的名称"],
        text: Annotated[str, "聊天的完整内容"],
    ) -> Annotated[Awaitable[MixedChat], "智障聊天"]:
        """
        mixed_chat 智障聊天

        Args:
            name (str): 机器人的名称。
            text (str): 聊天的完整内容。

        Returns:
            Awaitable[MixedChat]: 智障聊天。
        """
        pass

    async def music_tencent(
        self,
        *,
        name: Annotated[str, "歌曲名称，查找歌曲的编号"],
    ) -> Annotated[Awaitable[Sequence[MusicTencent]], "搜索腾讯音乐歌曲编号"]:
        """
        music_tencent 腾讯音乐

        搜索腾讯音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找歌曲的编号。

        Returns:
            Awaitable[Sequence[MusicTencent]]: 搜索腾讯音乐歌曲编号。
        """
        pass

    async def music_netease(
        self,
        *,
        name: Annotated[str, "歌曲名称，查找该歌曲的编号"],
    ) -> Annotated[Awaitable[Sequence[MusicNetease]], "搜索网易云音乐歌曲编号"]:
        """
        music_netease 网易音乐

        搜索网易云音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找该歌曲的编号。

        Returns:
            Awaitable[Sequence[MusicNetease]]: 搜索网易云音乐歌曲编号。
        """
        pass

    async def music_kugou(
        self,
        *,
        name: Annotated[str, "歌曲名称，查找该歌曲的编号"],
    ) -> Annotated[Awaitable[Sequence[MusicKugou]], "搜索酷狗音乐歌曲编号"]:
        """
        music_kugou 酷狗音乐

        搜索酷狗音乐歌曲编号。

        Args:
            name (str): 歌曲名称，查找该歌曲的编号。

        Returns:
            Awaitable[Sequence[MusicKugou]]: 搜索酷狗音乐歌曲编号。
        """
        pass

    async def idiom_solitaire(
        self, *, name: Annotated[str, "查找对应词语"]
    ) -> Annotated[Awaitable[IdiomSolitaire], "校对成语并返回相关成语"]:
        """
        idiom_solitaire 成语接龙

        校对成语并返回相关成语

        Args:
            name (str): 查找对应词语。

        Returns:
            Awaitable[IdiomSolitaire]: 校对成语并返回相关成语。
        """
        pass

    async def saohua_random(
        self,
    ) -> Annotated[Awaitable[SaohuaRandom], "万花门派骚话"]:
        """
        saohua_random 撩人骚话

        万花门派骚话

        Returns:
            Awaitable[SaohuaRandom]: 万花门派骚话
        """
        pass

    async def saohua_content(
        self,
    ) -> Annotated[Awaitable[SaohuaContent], "召唤一条舔狗日记"]:
        """
        saohua_content 舔狗日记

        召唤一条舔狗日记。

        Returns:
            Awaitable[SaohuaContent]: 召唤一条舔狗日记。
        """
        pass

    async def sound_converter(
        self,
        *,
        appkey: Annotated[str, "阿里云身份识别 appkey"],
        access: Annotated[str, "阿里云身份识别 access"],
        secret: Annotated[str, "阿里云身份识别 secret"],
        text: Annotated[str, "合成的内容"],
        voice: Annotated[Literal["Aitong"], "发音人，默认值 Aitong"] = "Aitong",
        format: Annotated[
            Literal["PCM", "WAV", "MP3"], "编码格式，范围 PCM, WAV, MP3，默认值 MP3"
        ] = "MP3",
        sample_rate: Annotated[int, "采样率，默认值 16000"] = 16000,
        volume: Annotated[int, "音量，范围 0～100，默认值 50"] = 50,
        speech_rate: Annotated[int, "语速，范围 -500～500，默认值 0"] = 0,
        pitch_rate: Annotated[int, "音调，范围 -500～500，默认值 0"] = 0,
    ) -> Annotated[Awaitable[SoundConverter], "阿里云语音合成（TTS）"]:
        """
        sound_converter 语音合成

        阿里云语音合成（TTS）

        Args:
            appkey (str): 阿里云身份识别 appkey。
            access (str): 阿里云身份识别 access。
            secret (str): 阿里云身份识别 secret。
            text (str): 合成的内容。
            voice (Literal["Aitong"], optional): 发音人，默认值 Aitong。 Defaults to "Aitong".
            format (Literal["PCM", "WAV", "MP3"], optional): 编码格式，范围 PCM, WAV, MP3，默认值 MP3。 Defaults to "MP3".
            sample_rate (int, optional): 采样率，默认值 16000。 Defaults to 16000.
            volume (int, optional): 音量，范围 0～100，默认值 50。 Defaults to 50.
            speech_rate (int, optional): 语速，范围 -500～500，默认值 0。 Defaults to 0.
            pitch_rate (int, optional): 音调，范围 -500～500，默认值 0。 Defaults to 0.

        Returns:
            Awaitable[SoundConverter]: 阿里云语音合成（TTS）。
        """
        pass

    #############
    # Websocket #
    #############

    async def socket(self) -> AsyncGenerator[WebsocketResponse, None]:
        pass
