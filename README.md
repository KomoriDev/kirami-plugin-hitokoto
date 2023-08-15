<div align="center">
  <a href="#"><img src="https://kiramibot.dev/img/logo.svg" width="180" height="180" alt="KiramiBotPluginLogo"></a>
</div>

<div align="center">

# kirami-plugin-hitokoto

_✨ 有一句话能打动你的心 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/owner/kirami-plugin-hitokoto.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/kirami-plugin-hitokoto">
    <img src="https://img.shields.io/pypi/v/kirami-plugin-hitokoto.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="python">

</div>

## 📖 介绍

一言。数据来源于 [Hitokoto](https://hitokoto.cn/)

## 💿 安装

在 KiramiBot 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>
  
```bash
pip install kirami-plugin-hitokoto
```
</details>
<details>
<summary>pdm</summary>

```bash
pdm add kirami-plugin-hitokoto
```
</details>
<details>
<summary>poetry</summary>

```bash
poetry add kirami-plugin-hitokoto
```
</details>
<details>
<summary>conda</summary>

```bash
conda install kirami-plugin-hitokoto
```
</details>

打开 KiramiBot 项目根目录下的配置文件文件, 以 `kirami.toml` 为例，在 `[plugin]` 部分追加写入
```toml
plugins = ["kirami_plugin_hitokoto"]
```

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 一言 | 无 | 是 | 私聊/群聊 | 随机一条一言 |
