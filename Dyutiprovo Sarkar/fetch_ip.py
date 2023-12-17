import socket

def get_local_ip():
    try:
        # Get the hostname of the local machine
        host_name = socket.gethostname()
        # Get the IP address associated with the hostname
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except socket.error as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    local_ip = get_local_ip()
    if local_ip:
        print(f"Local IP Address: {local_ip}")
    else:
        print("Unable to fetch the local IP address.")
