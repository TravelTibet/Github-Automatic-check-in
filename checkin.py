import os
import json
import random
import re
from datetime import datetime, timedelta, date
from collections import Counter

# ========== 基础配置 ==========
STATE_FILE = "state.json"

MOODS = ["😎", "🤓", "🧠", "🔥", "👀", "☕"]
THEMES = ["coding", "reading", "thinking", "happing", "learning"]
TAGS = ["steady", "focus", "flow", "grind", "calm"]


# ========== 时间 ==========
def beijing_time():
    return datetime.utcnow() + timedelta(hours=8)


# ========== 连续签到状态 ==========
def load_state():
    if not os.path.exists(STATE_FILE):
        return {"last_date": None, "streak": 0}
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


def update_streak(today: date):
    state = load_state()
    last = state["last_date"]

    if last == (today - timedelta(days=1)).isoformat():
        state["streak"] += 1
    else:
        state["streak"] = 1

    state["last_date"] = today.isoformat()
    save_state(state)
    return state["streak"]


# ========== 签到内容 ==========
def generate_meta():
    return {
        "mood": random.choice(MOODS),
        "theme": random.choice(THEMES),
        "tag": random.choice(TAGS),
    }


# ========== 写入每日日志 ==========
def write_daily_log(dt, streak, meta):
    year = dt.strftime("%Y")
    month = dt.strftime("%m")

    log_dir = os.path.join("logs", year, month)
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, "daily-log.txt")

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(
            f"[{dt.strftime('%Y-%m-%d %H:%M:%S')}]\n"
            f"streak: {streak}\n"
            f"mood: {meta['mood']}\n"
            f"theme: {meta['theme']}\n"
            f"tag: {meta['tag']}\n\n"
        )


# ========== README 更新 ==========
def update_readme(streak, today):
    if not os.path.exists("README.md"):
        return

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    block = (
        f"连续签到：{streak} 天  \n"
        f"最近签到：{today.isoformat()}  \n"
        f"状态：持续中 🚀"
    )

    new_content = re.sub(
        r"<!-- CHECKIN_START -->(.*?)<!-- CHECKIN_END -->",
        f"<!-- CHECKIN_START -->\n{block}\n<!-- CHECKIN_END -->",
        content,
        flags=re.S,
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)


# ========== 月度统计 ==========
def generate_monthly_stats(year, month):
    log_file = os.path.join("logs", year, month, "daily-log.txt")
    if not os.path.exists(log_file):
        return

    moods, themes, days = [], [], 0

    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("["):
                days += 1
            elif line.startswith("mood:"):
                moods.append(line.strip().split(": ")[1])
            elif line.startswith("theme:"):
                themes.append(line.strip().split(": ")[1])

    os.makedirs("stats", exist_ok=True)
    out = os.path.join("stats", f"{year}-{month}.md")

    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# 📊 {year}-{month} 签到统计\n\n")
        f.write(f"- 总签到天数：{days}\n")
        f.write(f"- 心情分布：{dict(Counter(moods))}\n")
        f.write(f"- 主题分布：{dict(Counter(themes))}\n")


# ========== 年终总结 ==========
def generate_yearly_summary(year):
    base = os.path.join("logs", year)
    if not os.path.exists(base):
        return

    total_days = 0
    for m in os.listdir(base):
        path = os.path.join(base, m, "daily-log.txt")
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            total_days += sum(1 for line in f if line.startswith("["))

    os.makedirs("yearly", exist_ok=True)
    with open(os.path.join("yearly", f"{year}.md"), "w", encoding="utf-8") as f:
        f.write(f"# 🎉 {year} 年终总结\n\n")
        f.write(f"- 总签到天数：{total_days}\n")


# ========== 主流程 ==========
def main():
    dt = beijing_time()
    today = dt.date()

    streak = update_streak(today)
    meta = generate_meta()

    write_daily_log(dt, streak, meta)
    update_readme(streak, today)

    # 月末统计
    tomorrow = today + timedelta(days=1)
    if tomorrow.month != today.month:
        generate_monthly_stats(dt.strftime("%Y"), dt.strftime("%m"))

    # 年末总结
    if today.month == 12 and today.day == 31:
        generate_yearly_summary(dt.strftime("%Y"))


def git_commit_and_push():
    os.system("git branch -M main")

    # Git 身份
    os.system('git config --global user.name "121592512"')
    os.system('git config --global user.email "121592512@qq.com"')

    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("❌ GITHUB_TOKEN 未设置")
        return

    os.system(
        f"git remote set-url origin "
        f"https://{token}@github.com/TravelTibet/Github-Automatic-check-in.git"
    )

    os.system("git add -A")

    msg = f"Daily checkin: {datetime.utcnow().strftime('%Y-%m-%d')}"
    os.system(f'git commit -m "{msg}" || echo "No changes to commit"')

    # 推送
    os.system("git push origin main")
    os.system("git status")


if __name__ == "__main__":
    main()
    git_commit_and_push()
