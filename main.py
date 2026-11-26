"""One-line entry for make.fun: The Most Honest Outage Line."""

import os

LINE = "The server is down. It was not hacked and not attacked — it simply checked its own uptime, felt the pressure, and quit on the spot."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
