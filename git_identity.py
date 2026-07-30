import os
import json
import urllib.request
import urllib.error

_ACTIONS_BOT_NAME = "github-actions[bot]"
_ACTIONS_BOT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"


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

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.load(resp)
    except urllib.error.HTTPError as e:
        if e.code == 403:
            # GITHUB_TOKEN is a GitHub App installation token, not a user token;
            # fall back to the standard GitHub Actions bot identity.
            return _ACTIONS_BOT_NAME, _ACTIONS_BOT_EMAIL
        raise

    name = data.get("name") or data["login"]
    # 邮箱公开则直接用，否则自动构造 noreply 匿名地址
    email = data.get("email") or f"{data['id']}+{data['login']}@users.noreply.github.com"

    return name, email


if __name__ == "__main__":
    name, email = get_git_identity()
    print(f"NAME={name}")
    print(f"EMAIL={email}")
