import subprocess
import sys
import time
from os import listdir

import click
import pyopencl as cl
import requests


@click.command()
@click.option("--telegram-token", type=str, help="Telegram bot token", required=True)
@click.option("--telegram-chat-id", type=str, help="Telegram chat ID", required=True)
@click.option("--platform-id", type=int, help="OpenCL Platform ID", default=0)
@click.option(
    "--starts-with",
    type=str,
    help="Public key starts with the indicated prefix.",
    default="",
)
def main(telegram_token, telegram_chat_id, platform_id, starts_with):
    platforms = cl.get_platforms()[platform_id]
    devices = platforms.get_devices()

    if len(devices) == 1:
        print("Only one device found, running single instance")
        sys.exit(1)

    for device_index in range(len(devices)):
        subprocess.Popen(
            [
                "python3",
                "main.py",
                "search-pubkey",
                "--device",
                f"{platform_id}:{device_index}",
                "--starts-with",
                starts_with,
            ]
        )

    last_files = None

    while True:
        files = listdir("./")

        if last_files is not None:
            diff = set(files) - set(last_files)

            for file_name in diff:
                if file_name.endswith(".json"):
                    requests.post(
                        f"https://api.telegram.org/bot{telegram_token}/sendMessage",
                        data={
                            "chat_id": telegram_chat_id,
                            "text": f"Found pubkey: {file_name}",
                        },
                    )

            if len(diff) > 0:
                subprocess.run("kill -9 $(ps aux | grep 'python' | awk '{print $2}')")

        last_files = files

        time.sleep(1)


if __name__ == "__main__":
    main()
