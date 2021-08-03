## 简介
本项目开源地址：[iCQ](https://github.com/ZeroneBo/iCQ) : https://github.com/ZeroneBo/iCQ ，严禁使用本项目盈利，严禁用于非法用途！

由于考研复习高数时深感无聊且心态略崩，便摸了几天鱼写下这个项目来消遣。本项目基于 Mrs4s 的 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) ，在其基础上增加了几个有意思的小功能，可实现自动回复。

## 开始使用

### 环境配置

本项目基于Mrs4s 的 go-cqhttp v0.9.40-fix5，使用前需先下载并配置 go-cqhttp 。采用
python 开发，故运行需要 python 环境。配置 go-cqhttp 部分可参考其官方文档，此处不再赘述。
- flask
- requests

### 如何启动

直接在配置好的 python 环境中运行 main.py 即可。

### 功能说明

|  功能名   | 注释  |
|  ----  | ----  |
| #  | 列出功能菜单 |
| #功能 #  | 列出该功能的参数 |
| #bot* | 与机器人聊天 |
| #chp | 彩虹屁 |
| #dz | 讲段子 |
| #medal | 2020东京奥运金牌榜 |
| #pyq | 朋友圈文案 |
| #pz* | 喷子（为了共建和谐社会，不建议使用） |
| #wyy | 网易云评论 |
| \*表示该功能可加参数 | 不需输入\* |

## 注意

- 喜欢本项目，点个 star 吧 ^_^ 。

- 由于本人水平有限，开发时间有限，可能存在bug，若您在使用中发现了bug或有更好的建议，请提ISSUE。

- 不建议大号使用。

- _本开源项目仅供个人学习使用，严禁使用本项目盈利，严禁用于非法用途，否则出现的一切后果与本人无关。_


## 致谢

- [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) ，cqhttp的golang实现，轻量、原生跨平台，本项目的基础。

- [QQrobotFramework](https://github.com/luoluo964/QQrobotFramework/tree/main) ，提供了灵感和思路，也是一个不错的方案。
