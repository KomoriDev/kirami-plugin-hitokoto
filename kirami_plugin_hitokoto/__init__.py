from loguru import logger
from kirami import on_prefix
from kirami.matcher import Matcher
from kirami.utils.request import Request


@on_prefix("一言", to_me=True)
async def hitokoto(matcher: Matcher):

    response = await Request.get("https://v1.hitokoto.cn?c=a&c=b&c=c&c=d&c=h")
    if response.is_error:
        logger.error("获取一言失败")
        return
    data = response.json()
    msg = data["hitokoto"]
    add = ""
    if works := data["from"]:
        add += f"《{works}》"
    if from_who := data["from_who"]:
        add += f"{from_who}"
    if add:
        msg += f"\n——{add}"
    await matcher.finish(msg)