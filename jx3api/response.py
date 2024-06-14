from typing import (
    Annotated,
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
