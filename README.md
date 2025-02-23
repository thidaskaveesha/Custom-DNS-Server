# Custom DNS Server

This project is a **Custom DNS Server** built using Python. It resolves specific domain names based on predefined mappings and forwards unknown queries to an external DNS resolver.

## Features

- Handles DNS queries for a custom set of domain mappings.
- Forwards unresolved queries to a public DNS resolver (e.g., Google DNS).
- Simple and lightweight implementation.

## How It Works

- Listens on `127.0.0.1:53` (default DNS port).
- Resolves custom domains defined in the `DOMAIN_MAP` dictionary.
- Forwards queries not found in the `DOMAIN_MAP` to the specified forwarder (default: Google DNS at `8.8.8.8`).

## Code Explanation

### Main Components

1. **Custom Domain Mapping**
   - Use the `DOMAIN_MAP` dictionary to define custom domain-to-IP mappings.

   ```python
   DOMAIN_MAP = {"Bego.com": "10.10.205.11"}
   ```

2. **Query Handling**
   - Parses incoming DNS queries using the `dnslib` library.
   - Checks if the queried domain is in `DOMAIN_MAP`. If yes, returns the mapped IP address.
   - If not, forwards the query to the public DNS resolver.

3. **Forwarding Queries**
   - Forwards unresolved queries to the external resolver (default: Google DNS).

### Example Query Workflow

- A query for `Bego.com` with record type `A` is resolved to `10.10.205.11`.
- A query for an unknown domain (e.g., `example.com`) is forwarded to `8.8.8.8` for resolution.

## Requirements

- Python 3.7+
- `dnslib` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/thidaskaveesha/Custom-DNS-Server.git
   cd Custom-DNS-Server
   ```

2. Install the required library:
   ```bash
   pip install dnslib
   ```

3. Run the DNS server:
   ```bash
   python dns_server.py
   ```

## Configuration

### Custom Domain Mapping

You can define your own custom mappings in the `DOMAIN_MAP` dictionary:
```python
DOMAIN_MAP = {
    "example.com": "192.168.1.100",
    "mycustomdomain.net": "10.0.0.1"
}
```

### Forwarder

Change the forwarder DNS server by modifying the `FORWARDER` variable:
```python
FORWARDER = "1.1.1.1"  # Use Cloudflare DNS instead of Google DNS
```

## Usage

1. Start the DNS server:
   ```bash
   python dns_server.py
   ```

2. Update your system's DNS settings to point to `127.0.0.1`.

3. Test with `nslookup` or `dig`:
   ```bash
   nslookup Bego.com 127.0.0.1
   ```

## Example Output

When a query is made, the server logs the details:
```
DNS Server started on 127.0.0.1:53
Query for Bego.com., Type: A
```

## Limitations

- This implementation only supports `A` records.
- Only a basic forwarding mechanism is implemented.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

## Contribution

Contributions are welcome! If you have ideas for improvements or additional features, feel free to open an issue or submit a pull request.
