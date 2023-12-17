import socket
import requests

def get_local_ip():
    try:
        # Create a socket object and connect to an external server (e.g., Google DNS)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except socket.error:
        return "Unable to get local IP address."

def get_public_ip():
    try:
        # Use a service like 'httpbin' to get the public IP address
        response = requests.get('https://httpbin.org/ip')
        public_ip = response.json()['origin']
        return public_ip
    except requests.RequestException:
        return "Unable to get public IP address."

if __name__ == "__main__":
    local_ip = get_local_ip()
    public_ip = get_public_ip()

    print(f"Local IP Address: {local_ip}")
    print(f"Public IP Address: {public_ip}")
