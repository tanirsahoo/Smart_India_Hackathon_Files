import subprocess

def block_tor(username):

  subprocess.run(["sudo", "apt", "install", "ufw"])
  subprocess.run(["sudo", "ufw", "enable"])
  subprocess.run(["sudo", "ufw", "allow", "80"])
  subprocess.run(["sudo", "ufw", "allow", "443"])
  subprocess.run(["sudo", "ufw", "default", "deny"])
  subprocess.run(["sudo", "ufw", "deny", "out", "on", "tor", "reject-with", "icmp-host-prohibited"])
  subprocess.run(["sudo", "ufw", "reload"])

if __name__ == "__main__":
  username = input("Enter the username of the user whose TOR access should be blocked: ")
  block_tor(username)