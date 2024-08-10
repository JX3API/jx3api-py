from typing import (
    Annotated,
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
    data: T | None


class ResponseActiveCalendar(TypedDict):
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


class ResponseActiveListCalendar(TypedDict):
    today: Annotated[_Today, "日期信息"]
    data: Annotated[Sequence[_ActiveCalendarList], "活动月历"]


class ResponseActiveCelebs(TypedDict):
    map_name: Annotated[str, "地图名称"]
    event: Annotated[str, "事件名称"]
    site: Annotated[str, "地点"]
    desc: Annotated[str, "事件描述"]
    icon: Annotated[str, "事件图标"]
    time: Annotated[str, "事件时间"]


class ResponseExamAnswer(TypedDict):
    id: Annotated[int, "试题 ID"]
    question: Annotated[str, "试题内容"]
    answer: Annotated[str, "试题答案"]
    correctness: Annotated[int, "正确性，1 为正确，0 为错误"]
    index: Annotated[int, "试题序号"]
    pinyin: Annotated[str, "试题拼音"]


class ResponseHomeFurniture(TypedDict):
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


class ResponseHomeTravel(TypedDict):
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


class ResponseNewsAllnews(TypedDict):
    id: Annotated[int, "新闻 ID"]
    token: Annotated[int, "新闻 Token"]
    class_: Annotated[str, "新闻分类"]
    title: Annotated[str, "新闻标题"]
    date: Annotated[str, "新闻日期"]
    url: Annotated[str, "新闻链接"]


class ResponseNewsAnnounce(TypedDict):
    id: Annotated[int, "公告 ID"]
    token: Annotated[int, "公告 Token"]
    class_: Annotated[str, "公告类别"]
    title: Annotated[str, "公告标题"]
    date: Annotated[str, "公告日期"]
    url: Annotated[str, "公告链接"]


class ResponseServerMaster(TypedDict):
    id: Annotated[str, "区服 ID"]
    zone: Annotated[str, "区服所属大区"]
    name: Annotated[str, "区服名称"]
    column: Annotated[str, "c"]
    duowan: Annotated[Dict[str, List[int]], "多玩 ID"]
    abbreviation: Annotated[List[str], "区服简称"]
    subordinate: Annotated[List[str], "区服下属服务器"]


class ResponseServerCheck(TypedDict):
    id: Annotated[int, "服务器 ID"]
    zone: Annotated[str, "服务器所在大区"]
    server: Annotated[str, "服务器名称"]
    status: Annotated[Literal[0, 1], "服务器状态，1 为开服，0 为维护中"]
    time: Annotated[int, "服务器状态更新时间戳"]


class ResponseServerStatus(TypedDict):
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    status: Annotated[str, "服务器状态"]


class _HomeFlower(TypedDict):
    name: Annotated[str, "鲜花名称"]
    color: Annotated[str, "鲜花颜色"]
    price: Annotated[float, "鲜花价格"]
    line: Annotated[Sequence[str], "鲜花线路"]


class ResponseHomeFlower(TypedDict):
    map: Annotated[Sequence[_HomeFlower], "地图鲜花价格"]


class ResponseSaveDetailed(TypedDict):
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


class ResponseRoleDetailed(TypedDict):
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


class ResponseSchoolMatrixDescs(TypedDict):
    desc: Annotated[str, "阵眼效果描述"]
    level: Annotated[int, "阵眼等级"]
    name: Annotated[str, "阵眼等级名称"]


class ResponseSchoolMatrix(TypedDict):
    name: Annotated[str, "心法名称"]
    skillName: Annotated[str, "阵眼名称"]
    descs: Annotated[Sequence[ResponseSchoolMatrixDescs], "阵眼效果列表"]


class _SchoolForce(TypedDict):
    name: Annotated[str, "奇穴名称"]
    class_: Annotated[int, "奇穴分类"]
    desc: Annotated[str, "奇穴效果描述"]
    icon: Annotated[str, "奇穴图标"]
    kind: Annotated[str, "奇穴类型"]
    subKind: Annotated[str, "奇穴子类型"]


class ResponseSchoolForce(TypedDict):
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


class ResponseSchoolSkills(TypedDict):
    class_: Annotated[str, "心法名"]
    data: Annotated[List[_SchoolSkills], "技能"]


class ResponseTiebaRandom(TypedDict):
    id: Annotated[int, "帖子 ID"]
    class_: Annotated[str, "帖子分类"]
    zone: Annotated[str, "大区"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "游戏名称"]
    title: Annotated[str, "帖子标题"]
    url: Annotated[int, "帖子链接"]
    date: Annotated[str, "发布时间"]


class ResponseRoleTeamCdListBossProgress(TypedDict):
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
    bossProgress: Annotated[Sequence[ResponseRoleTeamCdListBossProgress], "BOSS 进度"]


class ResponseRoleTeamCdList(TypedDict):
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


class ResponseLuckAdventure(TypedDict):
    zone: Annotated[str, "大区"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "角色名称"]
    event: Annotated[str, "奇遇名称"]
    level: Annotated[int, "奇遇等级"]
    status: Annotated[int, "奇遇状态"]
    time: Annotated[int, "触发时间"]


class ResponseLuckStatistical(TypedDict):
    id: Annotated[int, "奇遇 ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "奇遇名称"]
    event: Annotated[str, "奇遇事件"]
    status: Annotated[int, "奇遇状态"]
    time: Annotated[int, "触发时间"]


class ResponseLuckServerStatistical(TypedDict):
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


class ResponseLuckCollect(TypedDict):
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


class ResponseRoleAchievement(TypedDict):
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


class ResponseMatchRecentPerformance3v3(TypedDict):
    mmr: Annotated[int, "3v3 竞技场 MMR"]
    grade: Annotated[int, "3v3 竞技场 段位"]
    ranking: Annotated[str, "3v3 竞技场 排名"]
    winCount: Annotated[int, "3v3 竞技场 胜场"]
    totalCount: Annotated[int, "3v3 竞技场 总场"]
    mvpCount: Annotated[int, "3v3 竞技场 MVP 次数"]
    pvpType: Annotated[str, "3v3 竞技场 类型"]
    winRate: Annotated[int, "3v3 竞技场 胜率"]


class ResponseMatchRecentHistory(TypedDict):
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


class ResponseMatchRecentTrend(TypedDict):
    matchDate: Annotated[int, "比赛日期"]
    mmr: Annotated[int, "MMR"]
    winRate: Annotated[float, "胜率"]


class ResponseMatchRecentPerformance(TypedDict, total=False):
    _3v3: ResponseMatchRecentPerformance3v3


class ResponseMatchRecent(TypedDict):
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
    performance: ResponseMatchRecentPerformance
    history: Annotated[Sequence[ResponseMatchRecentHistory], "近期比赛记录"]
    trend: Annotated[Sequence[ResponseMatchRecentTrend], "近期比赛趋势"]


class ResponseMatchAwesome(TypedDict):
    zoneName: Annotated[str, "区服名称"]
    serverName: Annotated[str, "服务器名称"]
    roleName: Annotated[str, "角色名称"]
    forceName: Annotated[str, "门派名称"]
    avatarUrl: Annotated[str, "头像地址"]
    rankNum: Annotated[str, "排名"]
    score: Annotated[str, "积分"]
    upNum: Annotated[str, "上升名次"]
    winRate: Annotated[str, "胜率"]


class ResponseMatchSchools(TypedDict):
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


class ResponseMemberRecruit(TypedDict):
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


class ResponseMemberTeacher(TypedDict):
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


class ResponseMemberStudent(TypedDict):
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


class ResponseServerSand(TypedDict):
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    reset: Annotated[int, "重置时间"]
    update: Annotated[int, "更新时间"]
    data: Annotated[Sequence[_ServerSand], "沙盘信息"]


class ResponseServerEvent(TypedDict):
    id: Annotated[int, "事件ID"]
    camp_name: Annotated[str, "阵营名称"]
    fenxian_zone_name: Annotated[str, "分线区服名称"]
    fenxian_server_name: Annotated[str, "分线服务器名称"]
    friend_zone_name: Annotated[str, "友方区服名称"]
    friend_server_name: Annotated[str, "友方服务器名称"]
    role_name: Annotated[str, "角色名称"]
    add_time: Annotated[int, "添加时间"]


class ResponseTradeDemon(TypedDict):
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
    id: Annotated[int, "记录ID"]
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


class ResponseTradeRecord(TypedDict):
    id: Annotated[int, "物品ID"]
    class_: Annotated[str, "物品类别"]
    subclass: Annotated[str, "物品子类别"]
    name: Annotated[str, "物品名称"]
    alias: Annotated[str, "物品别名"]
    subalias: Annotated[str, "物品别名"]
    row: Annotated[str, "物品行情"]
    level: Annotated[int, "物品等级"]
    desc: Annotated[str, "物品描述"]
    view: Annotated[str, "物品图片"]
    date: Annotated[str, "物品上架日期"]
    data: Annotated[Sequence[Sequence[_TradeRecord]], "物品价格数据"]


class ResponseTiebaItemRecords(TypedDict):
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


class ResponseValuablesStatistical(TypedDict):
    id: Annotated[int, "记录 ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "物品名称"]
    role_name: Annotated[str, "角色名称"]
    map_name: Annotated[str, "副本名称"]
    time: Annotated[int, "掉落时间"]


class ResponseValuablesServerStatistical(TypedDict):
    id: Annotated[int, "记录ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "物品名称"]
    role_name: Annotated[str, "角色名称"]
    map_name: Annotated[str, "副本名称"]
    time: Annotated[int, "掉落时间"]


class ResponseServerAntivice(TypedDict):
    id: Annotated[int, "事件ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    map_name: Annotated[str, "地图名称"]
    time: Annotated[int, "事件时间"]


class ResponseRankStatistical(TypedDict):
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


class ResponseRankServerStatistical(TypedDict):
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


class ResponseSchoolRankStatistical(TypedDict):
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


class ResponseActiveMonsterSkill(TypedDict):
    level: Annotated[int, "首领等级"]
    name: Annotated[str, "首领名称"]
    skill: Annotated[list[str], "首领技能"]
    data: Annotated[_ActiveMonster, "特殊效果"]


class ResponseActiveMonster(TypedDict):
    start: Annotated[int, "活动开始时间戳"]
    end: Annotated[int, "活动结束时间戳"]
    data: Annotated[list[ResponseActiveMonsterSkill], "首领列表"]


class ResponseHorseRecord(TypedDict):
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


class ResponseHorseRanch(TypedDict):
    code: Annotated[int, "状态码"]
    msg: Annotated[str, "状态信息"]
    data: _HorseRanch
    time: Annotated[int, "时间戳"]


class ResponseFireworkRecord(TypedDict):
    id: Annotated[int, "记录ID"]
    zone: Annotated[str, "区服"]
    server: Annotated[str, "服务器"]
    name: Annotated[str, "角色名称"]
    map_name: Annotated[str, "地图名称"]
    sender: Annotated[str, "发送者"]
    recipient: Annotated[str, "接收者"]
    status: Annotated[int, "状态"]
    time: Annotated[int, "时间戳"]


class ResponseFireworkStatistical(TypedDict):
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


class ResponseFireworkCollect(TypedDict):
    server: Annotated[str, "区服"]
    sender: Annotated[str, "发送者"]
    recipient: Annotated[str, "接收者"]
    name: Annotated[str, "烟花名称"]
    count: Annotated[int, "烟花数量"]
    time: Annotated[int, "时间戳"]


class ResponseFireworkRankStatistical(TypedDict):
    server: Annotated[str, "区服"]
    sender: Annotated[str, "赠送者"]
    recipient: Annotated[str, "接收者"]
    name: Annotated[str, "烟花名称"]
    count: Annotated[int, "数量"]
    time: Annotated[int, "时间戳"]
