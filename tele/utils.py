import subprocess


def notify(message):
    subprocess.run(["notify-send", message])
