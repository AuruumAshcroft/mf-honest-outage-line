"""One-line entry for make.fun: The Most Honest Outage Line."""

import os

LINE = "The server is down. It was not hacked, it was not attacked — it simply looked at its own uptime, felt the pressure, and quit."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
