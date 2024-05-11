import subprocess
import sys

import click
import pyopencl as cl


@click.command()
@click.option("--platform-id", type=int, help="OpenCL Platform ID", default=0)
@click.option(
    "--starts-with",
    type=str,
    help="Public key starts with the indicated prefix.",
    default="",
)
def main(platform_id, starts_with):
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


if __name__ == "__main__":
    main()
