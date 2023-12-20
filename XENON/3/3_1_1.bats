load IPv6-helper

@test "3.2.2 Ensure IP forwarding is disabled (Automated)" {
    # IPv4
    run bash -c "sysctl net.ipv4.ip_forward"
    [ "$status" -eq 0 ]
    [ "$output" = "net.ipv4.ip_forward = 0" ]
    run bash -c "grep -E -s \"^\s*net\.ipv4\.ip_forward\s*=\s*1\" /etc/sysctl.conf /etc/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /run/sysctl.d/*.conf"
    [ "$status" -ne 0 ]
    [ "$output" = "" ]
    # IPv6
    run check_ip_v6
    [ "$status" -eq 0 ]
    if [[ "$output" == *"*** IPv6 is enabled on the system ***"* ]]; then
        run bash -c "sysctl net.ipv6.conf.all.forwarding"
        [ "$status" -eq 0 ]
        [ "$output" = "net.ipv6.conf.all.forwarding = 0" ]
        run bash -c "grep -E -s \"^\s*net\.ipv6\.conf\.all\.forwarding\s*=\s*1\" /etc/sysctl.conf /etc/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /run/sysctl.d/*.conf"
        [ "$status" -ne 0 ]
        [ "$output" = "" ]
    fi
}