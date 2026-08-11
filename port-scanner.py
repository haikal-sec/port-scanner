import socket
import concurrent.futures

def check_port(target_ip, port):
    """Attempt to connect to a specific port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1.0)
        if sock.connect_ex((target_ip, port)) == 0:
            return port
    return None

def fast_port_scanner(target_host, ports_to_scan):
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("Hostname could not be resolved.")
        return

    print(f"Starting multithreaded scan on {target_ip}...")
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        # Submit all tasks to the executor
        futures = {executor.submit(check_port, target_ip, port): port for port in ports_to_scan}
        
        for future in concurrent.futures.as_completed(futures):
            port = future.result()
            if port is not None:
                print(f"[+] Port {port} is OPEN")
                open_ports.append(port)

    print(f"Scan complete. Open ports: {sorted(open_ports)}")

# scanning the first 1000 ports
if __name__ == "__main__":
    target = "127.0.0.1" 
    ports = range(1, 1025)
    fast_port_scanner(target, ports)
    
    # Note: This script is for educational purposes only.
    # by haikal-sec