from setuptools import setup, find_packages

setup(
    name = "nonebot-plugin-BingImage",
    version = "0.0.1",
    keywords = ["nonebot","nonebot-plugin","BingImage","Bing", "nonebot-plugin-BingImage"],
    description = "Get Bing Images for NoneBot2",
    long_description = "A NoneBot2 plugin that gets bing images.",
    license = "GPLv3 Licence",
    url = "https://github.com/ericzhang-debug/nonebot_plugin_BingImage",
    author = "EricZhang",
    author_email = "15364519511@163.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [
        "nonebot2>=2.0.0b3",
        "httpx>=0.20.0,<1.0.0",
        "nonebot-adapter-onebot>=2.0.0b1",
        "nonebot-plugin-apscheduler>=0.1.0",
        "requests",
        "parsel",
        "faker"
    ]
)