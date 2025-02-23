import socket
from dnslib import DNSRecord, QTYPE, RR, A

DNS_HOST = "127.0.0.1"
DNS_PORT = 53
FORWARDER = "8.8.8.8"  
DOMAIN_MAP = {"Bego.com": "10.10.205.11"}

def handle_query(data, addr, sock):
    query = DNSRecord.parse(data)
    response = query.reply()
    
    for question in query.questions:
        qname = str(question.qname)
        qtype = QTYPE[question.qtype]
        print(f"Query for {qname}, Type: {qtype}")
        
        if qname in DOMAIN_MAP and qtype == "A":
            response.add_answer(RR(qname, QTYPE.A, ttl=60, rdata=A(DOMAIN_MAP[qname])))
        else:
            # Forward unknown queries
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as forward_sock:
                forward_sock.sendto(data, (FORWARDER, DNS_PORT))
                forward_data, _ = forward_sock.recvfrom(512)
            sock.sendto(forward_data, addr)
            return

    sock.sendto(response.pack(), addr)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((DNS_HOST, DNS_PORT))
    print(f"DNS Server started on {DNS_HOST}:{DNS_PORT}")
    while True:
        data, addr = sock.recvfrom(512)
        handle_query(data, addr, sock)
