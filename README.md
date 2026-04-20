[![Dailyly](https://github.com/TravelTibet/Github-Automatic-check-in/actions/workflows/daily_checkin.yml/badge.svg)](https://github.com/TravelTibet/Github-Automatic-check-in/actions/workflows/daily_checkin.yml)
[![CodeQL](https://github.com/TravelTibet/Github-Automatic-check-in/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/TravelTibet/Github-Automatic-check-in/actions/workflows/github-code-scanning/codeql)

<!-- TOC -->
* [Github-Automatic-check-in](#github-automatic-check-in)
  * [配置过程](#配置过程)
    * [生成个人访问token（PAT）](#生成个人访问tokenpat)
    * [将 PAT 添加到 Secrets](#将-pat-添加到-secrets)
    * [更改自己的账号以及名称](#更改自己的账号以及名称)
  * [⏳ 自动签到状态](#-自动签到状态)
<!-- TOC -->

# Github-Automatic-check-in（GitHub自动签到）
- 随机每日的心情，状态等信息
- 按照年，月进行归档日志

> [!NOTE]
> 
> 这里的自动签到是每天都有自动提交的记录，被记录到Github的贡献记录（Contribution Graph)
> 
> 然后在**GitHub Streak**就能显示连续提交的代码记录不间断


## 配置过程

### 生成个人访问token（PAT）

1. 登录 GitHub，进入 Settings > Developer settings > Personal access tokens。
2. Note填写 **daily-checkin**，Expiration选择**No expiration**（永不过期）
![img.png](pic/token名称.png)
3. 点击 Generate new token，选择以下权限：
   - repo（完全控制仓库）
   - workflow（允许操作 Actions）
![img.png](pic/生成token.png)
4. 生成后，复制 Token 值 **（注意：Token 只会显示一次，务必及时保存）**。

### 将 PAT 添加到 Secrets
1. 进入你的仓库（Github-Automatic-check-in），点击 Settings > Secrets and variables > Actions。
![img.png](pic/仓库设置Action.png)
2. 点击 New repository secret，输入：
   - Name: **DAILY_CHECKIN**
   - Value: 粘贴刚才生成的 PAT。
3. 点击 Add secret

### 更改自己的账号以及名称
在[代码中](checkin.py)的这两行
```python 
    os.system('git config --global user.name "xiname"')
    os.system('git config --global user.email "xinametravel@qq.com"')
```
user.name 以及 user.email更改成自己的**Github**的账户名以及提交的电子邮件

## Star History

<a href="https://www.star-history.com/?repos=TravelTibet%2FGithub-Automatic-check-in&type=date&legend=bottom-right">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=TravelTibet/Github-Automatic-check-in&type=date&theme=dark&legend=bottom-right" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=TravelTibet/Github-Automatic-check-in&type=date&legend=bottom-right" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=TravelTibet/Github-Automatic-check-in&type=date&legend=bottom-right" />
 </picture>
</a>


## ⏳ 自动签到状态

<!-- CHECKIN_START -->
连续签到：1 天  
最近签到：2026-04-20  
状态：持续中 🚀
<!-- CHECKIN_END -->

