<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-BingImage

_✨ 🖼️获取Bing每日风景图 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/ericzhang-debug/nonebot_plugin_BingImage.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-example">
    <img src="https://img.shields.io/pypi/v/nonebot_plugin_BingImage.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

🖼️获取Bing每日风景图

输入```/bing帮助``` 获取该插件的帮助信息

输入```/bing``` 获取今天的风景图(图片+故事)

输入```/bing电脑``` 单获取今天的风景图桌面横板

输入```/bing手机``` 单获取今天的风景图移动端竖版


## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot_plugin_BingImage

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot_plugin_BingImage
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot_plugin_BingImage
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot_plugin_BingImage
</details>
<details>
<summary>conda</summary>

    conda install nonebot_plugin_BingImage
</details>

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('nonebot_plugin_BingImage')

</details>

[//]: # (## ⚙️ 配置)

[//]: # ()
[//]: # (在 nonebot2 项目的`.env`文件中添加下表中的必填配置)

[//]: # ()
[//]: # (| 配置项 | 必填 | 默认值 | 说明 |)

[//]: # (|:-----:|:----:|:----:|:----:|)

[//]: # (| 配置项1 | 是 | 无 | 配置说明 |)

## 🎉 使用
### 指令表
| 指令    | 权限  | 需要@ | 范围    | 说明   |
|-------|-----|----|-------|------|
| /bing帮助  | 所有人 | 是 | 私聊/群聊 | 获取插件帮助|
| /bing | 所有人 | 是 | 私聊/群聊 | 获取今天的风景图(图片+故事)|
| /bing电脑 | 所有人 | 是 | 私聊/群聊 | 单获取今天的风景图桌面横板|
| /bing手机 | 所有人 | 是 | 私聊/群聊 | 单获取今天的风景图移动端竖版|

<!-- | 添加图片订阅 | 管理员 | 是  | 私聊/群聊 | 为群聊添加风景图订阅 |
| 删除图片订阅 | 管理员 | 是  | 私聊/群聊    | 为群聊删除风景图订阅 | -->

### 效果图

帮助

![qq_pic_merged_1673250259530.jpg](https://s2.loli.net/2023/01/09/38MHBCoQWdOsVp7.jpg)

获取每日一图及故事

![qq_pic_merged_1673250243461.jpg](https://s2.loli.net/2023/01/09/eRVrgH4bsqoNuKX.jpg)

单独获取桌面端OR移动端图片

![qq_pic_merged_1673250225910.jpg](https://s2.loli.net/2023/01/09/dJa3pGVAUMqnxSu.jpg)

## 📋 已实现功能

指令获取桌面端图片

指令获取移动端图片

指令获取图片故事

## 🛠️ 待实现功能

订阅推送功能

正则匹配规则

异常处理

