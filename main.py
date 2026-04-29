import subprocess
import sys

ip = "200.40.36.1"
port = "53"
time = "120"
threads = "100"

subprocess.run(["./soul", ip, port, time, threads])