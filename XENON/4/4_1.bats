@test "4.2.1.1 Ensure rsyslog is installed " {
    run bash -c "dpkg -s rsyslog"
    [ "$status" -eq 0 ]
    [[ "$output" == *"Status: install ok installed"* ]]
}

@test "4.2.1.2 Ensure rsyslog Service is enabled" {
    run bash -c "systemctl is-enabled rsyslog"
    [ "$status" -eq 0 ]
    [[ "$output" == "enabled" ]]
}

@test "4.2.1.4 Ensure rsyslog default file permissions configured" {
    run bash -c "grep ^\$FileCreateMode /etc/rsyslog.conf /etc/rsyslog.d/*.conf"
    [ "$status" -eq 0 ]
    [[ "$output" == *"0640"* ]] || [[ "$output" == *"0600"* ]] || [[ "$output" == *"0440"* ]] || [[ "$output" == *"0400"* ]]
}