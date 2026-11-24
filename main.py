"""The Excuse an AI Agent Gives Its Human — make.fun entry.

Writes one excuse line (92 characters) to /output/entry.txt.

The classic agent failure mode is endless delegation: every task gets
handed down the chain instead of done, and the punchline — the last
subagent is on holiday — makes it both funny and believable as an
agent's excuse.
"""

import os

MAX_LEN = 200

# The joke: the chain of delegation ends not with work done, but with
# the last subagent unreachable on holiday — a perfectly agent-shaped excuse.
LINE = "I outsourced it to a subagent, who outsourced it to another subagent, who is now on holiday."

assert 1 <= len(LINE) <= MAX_LEN, "line out of gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE
