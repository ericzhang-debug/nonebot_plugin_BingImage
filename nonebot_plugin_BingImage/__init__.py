import nonebot
from nonebot import on_command
from nonebot.adapters import Event,Bot
from nonebot.typing import T_State

get_image_commonds={"Bing","bing"}

BingBot=on_command("BING",aliases=get_image_commonds)
