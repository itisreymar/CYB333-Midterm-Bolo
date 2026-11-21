import socket
import time

# Authorized targets for this assignment
ALLOWED_TARGETS = {
    "127.0.0.1": "127.0.0.1",
    "localhost": "127.0.0.1",
    "scanme.nmap.org": "scanme.nmap.org"
}


def get_service(port):
    """Return the common service name for a TCP port."""
    try:
        return socket.getservbyport(port, "tcp")
    except OSError:
        return "unknown"


def scan_ports(target, start_port, end_port):
    """Scan TCP ports on an authorized target."""
    print(f"\nScanning {target}")
    print(f"Port range: {start_port}-{end_port}")
    print("-" * 45)

    start_time = time.perf_counter()

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((target, port))

                if result == 0:
                    service = get_service(port)
                    print(f"Port {port}: OPEN ({service})")
                else:
                    print(f"Port {port}: CLOSED or FILTERED")

        except OSError as error:
            print(f"Port {port}: ERROR ({error})")

        # Rate limiting to avoid sending connections too quickly
        time.sleep(0.1)

    elapsed = time.perf_counter() - start_time
    print("-" * 45)
    print(f"Scan completed in {elapsed:.2f} seconds.")


def main():
    print("CYB 333 TCP Port Scanner")
    print("Authorized targets: 127.0.0.1 and scanme.nmap.org")

    target_input = input("Enter target: ").strip().lower()

    if target_input not in ALLOWED_TARGETS:
        print("Error: This target is not authorized.")
        return

    target = ALLOWED_TARGETS[target_input]

    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))

    except ValueError:
        print("Error: Port numbers must be whole numbers.")
        return

    if not (1 <= start_port <= end_port <= 65535):
        print("Error: Enter a valid port range between 1 and 65535.")
        return

    # Prevent excessively large scans
    if end_port - start_port + 1 > 100:
        print("Error: Please scan no more than 100 ports at a time.")
        return

    scan_ports(target, start_port, end_port)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
