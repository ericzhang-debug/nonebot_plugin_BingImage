from nonebot import on_command, on_startswith
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.log import logger

from nonebot import require

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

from .utils import *

test = on_command("test", aliases={'1', }, priority=6)

Help_info = "Bing机器人帮助 \n这是第一行 \n这是第二行"

help_matcher = on_command("bing帮助", aliases={'Bing帮助', '必应帮助', }, priority=1)
bing_matcher = on_command("bing", aliases={'必应', 'bing每日一图', 'bing美图', 'Bing', 'BING'}, priority=2)

bing_desktop_matcher = on_command("bing电脑图片",
                                  aliases={'bing桌面端图片', '电脑图片', '桌面端图片', 'bing电脑', 'bing桌面图片',
                                           'bing横版'}, priority=3)
bing_mobile_matcher = on_command("bing手机图片",
                                 aliases={'bing移动端图片', '手机图片', '移动端图片', 'bing手机', 'bing竖版', },
                                 priority=4)


@help_matcher.handle()
async def help(bot: Bot, event: Event, state: T_State):
    await help_matcher.send(str(Help_info))


@bing_matcher.handle()
async def bing(bot: Bot, event: Event, state: T_State):
    d_url = str(getBingImageURL())
    description = getBingDescription()
    msg_img = MessageSegment.image(d_url)
    logger.info("图片获取成功!")
    msg_title = Message(str(description['title']))
    msg_headline = Message(str("图片主题：" + description['headline']))
    msg_desc = Message(str("图片故事：" + description['description']))
    msg_maintext = Message(str("图片介绍：" + description['main_text']))
    msg = msg_title + Message("\n") + Message("\n") + msg_headline + Message("\n") + Message(
        "\n") + msg_maintext + Message("\n") + Message("\n") + msg_desc + Message("\n") + Message("\n") + Message(
        msg_img)
    await bing_matcher.send(msg)
    logger.info("消息发送成功!")


@bing_desktop_matcher.handle()
async def bing_desktop(bot: Bot, event: Event, state: T_State):
    d_url = str(getBingImageURL())
    msg_img = MessageSegment.image(d_url)
    logger.info("图片获取成功!")
    msg = Message(msg_img)
    await bing_desktop_matcher.send(msg)
    logger.info("消息发送成功!")


@bing_mobile_matcher.handle()
async def bing_mobile(bot: Bot, event: Event, state: T_State):
    d_url = str(getBingVerticalImageURL())
    msg_img = MessageSegment.image(d_url)
    logger.info("图片获取成功!")
    msg = Message(msg_img)
    await bing_mobile_matcher.send(msg)
    logger.info("消息发送成功!")
