load IPv6-helper

@test "3.5.1.2 Ensure iptables-persistent is not installed with ufw" {
    run bash -c "dpkg-query -s iptables-persistent"
    [ $status -eq 1 ]
    [[ "$output" == *"package 'iptables-persistent' is not installed and no information is available"* ]]
}
