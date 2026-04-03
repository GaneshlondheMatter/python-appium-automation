import subprocess
import time

def start_ssh_tunnel():
    command = [
        "ssh",
        "-L", "127.0.0.1:5432:matter-orbit-postgresql.postgres.database.azure.com:5432",
        "matmot_bk_user@20.219.252.229",
        "-p", "22",
        "-N"
    ]

    process = subprocess.Popen(command)
    time.sleep(3)

    print("✅ SSH Tunnel Established")
    return process

def stop_ssh_tunnel(process):
    if process:
        process.terminate()
        print("🛑 SSH Tunnel Closed")