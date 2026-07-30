import os
import json
import urllib.request


def get_git_identity():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GITHUB_TOKEN environment variable is not set")

    req = urllib.request.Request(
        "https://api.github.com/user",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
        },
    )

    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)

    name = data.get("name") or data["login"]
    # 邮箱公开则直接用，否则自动构造 noreply 匿名地址
    email = data.get("email") or f"{data['id']}+{data['login']}@users.noreply.github.com"

    return name, email


if __name__ == "__main__":
    name, email = get_git_identity()
    print(f"NAME={name}")
    print(f"EMAIL={email}")
