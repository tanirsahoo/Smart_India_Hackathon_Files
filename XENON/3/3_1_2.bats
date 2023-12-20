load IPv6-helper

# 3.5.1 Configure UncomplicatedFirewall

@test "3.5.1.1 Ensure ufw is installed" {
    [[ $(dpkg -s ufw | grep 'Status: install') == "Status: install ok installed" ]]
}

