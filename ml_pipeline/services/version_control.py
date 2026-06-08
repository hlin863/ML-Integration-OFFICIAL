import os
import subprocess


def current_git_sha():
    sha = os.environ.get("GITHUB_SHA")
    if sha:
        return sha[:40]

    try:
        completed = subprocess.run(
            ["git", "rev-parse", "--short=12", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return ""

    return completed.stdout.strip()
