import socket
import psutil

def log_external_connections():
    connections = psutil.net_connections()
    log = []
    for conn in connections:
        if conn.status == 'ESTABLISHED':
            remote_ip = conn.raddr[0]
            if not remote_ip.startswith("127."):
                local_ip = conn.laddr[0]
                local_port = conn.laddr[1]
                remote_port = conn.raddr[1]
                log.append(f"Established connection from {remote_ip}:{remote_port} to {local_ip}:{local_port}")
    if log:
        with open("external_connections.log", "a") as f:
            for entry in log:
                f.write(entry + "\n")

if __name__ == "__main__":
    log_external_connections()
