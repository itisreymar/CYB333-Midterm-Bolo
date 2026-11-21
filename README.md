# CYB333-Midterm-Bolo
CYB 333 Security Automation midterm project demonstrating Python TCP client-server communication, network port scanning, error handling, and security testing.
# CYB 333 Security Automation — Midterm Project

## Project Overview

This project demonstrates basic security automation concepts using Python. It includes a TCP client-server application and a TCP port scanner.

## Part 1: TCP Client-Server Communication

**Files:** `server.py` and `client.py`

The server listens for incoming connections on `127.0.0.1:5000`. The client connects, sends a message, and receives a response.

Features include:
- Two-way TCP communication
- Connection timestamps
- Connection error handling
- Five-second client timeout
- Graceful socket cleanup and shutdown

**How to run:**

Open two terminals in the project folder.

Terminal 1:
```bash
python server.py
```

Terminal 2:
```bash
python client.py
```

## Part 2: TCP Port Scanner

**File:** `port_scanner.py`

The port scanner checks TCP ports on authorized targets and reports whether connections succeed.

Features include:
- Restricted targets: `127.0.0.1`, `localhost`, and `scanme.nmap.org`
- User-defined port ranges
- Open and closed/filtered port reporting
- Common TCP service identification
- Port-number and target validation
- Rate limiting and scan duration reporting

**How to run:**

```bash
python port_scanner.py
```

Follow the prompts to enter an authorized target and port range.

## Testing

Testing includes successful client-server communication, failed connection handling, graceful server interruption, open-port detection, closed/filtered-port detection, and invalid-input validation.

Screenshots are included in the repository as evidence of the tests.

## Ethical Considerations

Port scanning should only be performed on systems where testing is authorized. This project restricts scanning to the targets specified in the assignment and includes a delay between connection attempts.

## Technologies

- Python 3
- Python socket library
- VS Code
- GitHub
