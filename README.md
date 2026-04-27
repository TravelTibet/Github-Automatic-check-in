[![Dailyly](https://github.com/TravelTibet/Github-Automatic-check-in/actions/workflows/daily_checkin.yml/badge.svg)](https://github.com/TravelTibet/Github-Automatic-check-in/actions/workflows/daily_checkin.yml)
[![CodeQL](https://github.com/TravelTibet/Github-Automatic-check-in/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/TravelTibet/Github-Automatic-check-in/actions/workflows/github-code-scanning/codeql)

# Github-Automatic-check-in（GitHub 自动签到）

> 每天自动提交一次记录，写入 GitHub 贡献图（Contribution Graph），让 GitHub Streak 保持不间断。

功能特性：
- 随机生成每日心情、状态等信息
- 按照年/月自动归档日志

> [!NOTE]
> 这里的"签到"是每天自动向仓库提交一次 commit，记录到 GitHub 的贡献记录（Contribution Graph）。在 **GitHub Streak** 中即可看到连续提交不间断的记录。

---

## 配置过程

### 第一步：Fork 本仓库

点击右上角 **Fork** 按钮，将本仓库 Fork 到你自己的账号下。

> [!IMPORTANT]
> Fork 完成后，**必须先启用 Actions**：
> 1. 进入你 Fork 后的仓库
> 2. 点击顶部 **Actions** 标签页
> 3. 点击绿色按钮 **"I understand my workflows, go ahead and enable them"**
>
> ⚠️ 如果跳过这一步，GitHub 默认禁用 Fork 仓库的 Actions，自动签到将**永远不会运行**。

---

### 第二步：生成个人访问 Token（PAT）

1. 登录 GitHub，进入 **Settings > Developer settings > Personal access tokens > Tokens (classic)**
2. 点击 **Generate new token (classic)**
3. 填写信息：
   - **Note**：填写 `daily-checkin`
   - **Expiration**：选择 `No expiration`（永不过期）

   ![token名称](pic/token名称.png)

4. 勾选以下权限：
   - ✅ `repo`（完全控制仓库）
   - ✅ `workflow`（允许操作 Actions）

   ![生成token](pic/生成token.png)

5. 点击 **Generate token**，生成后**立即复制保存 Token 值**。

> [!WARNING]
> Token 只会显示一次，离开页面后无法再次查看，请务必及时保存。

---

### 第三步：将 PAT 添加到仓库 Secrets

1. 进入你 Fork 后的仓库，点击 **Settings > Secrets and variables > Actions**

   ![仓库设置Action](pic/仓库设置Action.png)

2. 点击 **New repository secret**，填写：
   - **Name**：`DAILY_CHECKIN`（名称必须完全一致，区分大小写）
   - **Secret**：粘贴刚才保存的 PAT

3. 点击 **Add secret** 保存。

---

### 第四步：修改 checkin.py 中的用户信息

1. 在仓库页面点击 **`checkin.py`** 文件
2. 点击右上角 ✏️ **铅笔图标** 进入编辑模式
3. 找到以下两行，改为你自己的 GitHub 用户名和邮箱：

```python
os.system('git config --global user.name "你的GitHub用户名"')
os.system('git config --global user.email "你的GitHub注册邮箱"')
```

> 例如：
> ```python
> os.system('git config --global user.name "myusername"')
> os.system('git config --global user.email "myemail@example.com"')
> ```

4. 点击页面右上角 **Commit changes** 保存。

> [!NOTE]
> GitHub 用户名可在页面右上角头像旁看到；邮箱可在 **Settings > Emails** 中查看。

---

### 第五步：验证是否成功

配置完成后，可以手动触发一次测试：

1. 点击仓库顶部 **Actions** 标签页
2. 左侧选择 **Dailyly** workflow
3. 点击右侧 **Run workflow > Run workflow**

几秒后刷新页面，如果显示 ✅ 绿色对勾，说明配置成功，之后会每天自动运行。

如果显示 ❌ 红色，点进去查看日志，常见错误：
- `remote: Permission denied` → Secret 名称填错，或 PAT 权限不足
- `Author identity unknown` → `checkin.py` 中的用户名/邮箱未修改

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=TravelTibet/Github-Automatic-check-in&type=date&legend=bottom-right)](https://www.star-history.com/?repos=TravelTibet%2FGithub-Automatic-check-in&type=date&legend=bottom-right)

## ⏳ 自动签到状态

<!-- CHECKIN_START -->
连续签到：90 天  
最近签到：2026-04-27  
状态：持续中 🚀
<!-- CHECKIN_END -->
