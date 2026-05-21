import subprocess
import sys

subprocess.run(
    [sys.executable, "-m", "target_finder_toolkit.ninjacursors", "--without-targetfinder"],
    check=True,
)