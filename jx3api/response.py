from typing import (
    Annotated,
    Any,
    Generic,
    Literal,
    NotRequired,
    Sequence,
    TypedDict,
    TypeVar,
)

T = TypeVar("T")


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
    luck: Annotated[Sequence[str], "福缘宠物"]
    card: Annotated[Sequence[str], "家园声望·加倍道具"]
    leader: NotRequired[Annotated[str, "世界首领"]]
    draw: NotRequired[Annotated[str, "美人图"]]
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


class ResponseActiveListCalendar(TypedDict):
    today: Annotated[_Today, "今天日期信息"]
    data: Annotated[Sequence[ResponseActiveCalendar], "日常任务列表"]


class ResponseActiveCelebrity(TypedDict):
    map_name: Annotated[str, "地图名称"]
    event: Annotated[str, "事件"]
    site: Annotated[str, "地点"]
    desc: Annotated[str, "描述信息"]
    icon: Annotated[str, "图标"]
    time: Annotated[str, "时间"]


class ResponseExamAnswer(TypedDict):
    id: Annotated[int, "id"]
    question: Annotated[str, "科举问题"]
    answer: Annotated[str, "科举答案"]
    correctness: Annotated[int, "是否正确"]
    index: Annotated[int, "索引位置"]
    pinyin: Annotated[str, "拼音"]


class ResponseHomeFurniture(TypedDict):
    id: Annotated[int, "id"]
    name: Annotated[str, "家具名称"]
    type: Annotated[int, "type"]
    color: Annotated[int, "color"]
    source: Annotated[str, "家具来源"]
    architecture: Annotated[int, "architecture"]
    limit: Annotated[int, "limit"]
    quality: Annotated[int, "家具品质"]
    view: Annotated[int, "观赏值"]
    practical: Annotated[int, "实用值"]
    hard: Annotated[int, "坚固值"]
    geomantic: Annotated[int, "风水值"]
    interesting: Annotated[int, "趣味值"]
    produce: Annotated[Any, "produce"]
    image: Annotated[str, "图片路径"]
    tip: Annotated[str, "tip"]


class ResponseHomeTravel(TypedDict):
    id: Annotated[int, "id"]
    name: Annotated[str, "家具名称"]
    type: Annotated[int, "type"]
    color: Annotated[int, "color"]
    source: Annotated[str, "家具来源"]
    architecture: Annotated[int, "architecture"]
    limit: Annotated[int, "limit"]
    quality: Annotated[int, "家具品质"]
    view: Annotated[int, "观赏值"]
    practical: Annotated[int, "实用值"]
    hard: Annotated[int, "坚固值"]
    geomantic: Annotated[int, "风水值"]
    interesting: Annotated[int, "趣味值"]
    produce: Annotated[Any, "produce"]
    image: Annotated[str, "图片路径"]
    tip: Annotated[str, "tip"]


class ResponseNewsAllNews(TypedDict):
    id: Annotated[int, "id"]
    value: Annotated[int, "编号"]
    type: Annotated[str, "类型"]
    title: Annotated[str, "标题"]
    date: Annotated[str, "日期"]
    url: Annotated[str, "网址"]
