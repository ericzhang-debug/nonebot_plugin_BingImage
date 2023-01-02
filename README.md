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

输入```BING``` 获取今天的风景图(默认横板)

输入```BING竖屏``` 获取今天的风景图竖屏版本


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
| 添加图片订阅 | 管理员 | 是  | 私聊/群聊 | 为群聊添加风景图订阅 |
| 删除图片订阅 | 管理员 | 是  | 私聊/群聊    | 为群聊删除风景图订阅 |
| BING  | 所有人 | 否 | 私聊/群聊 | 获取风景图|
| BING竖屏 | 所有人 | 否 | 私聊/群聊 | 获取风景图|
### 效果图
如果有效果图的话

## 🧻 已实现功能


## 🛠️ 待实现功能
