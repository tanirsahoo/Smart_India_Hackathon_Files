@test "1.1.12 Ensure /var/tmp partition includes the nodev option (Automated)" {
    run bash -c "findmnt -n /var/tmp | grep -v nodev"
    [ "$status" -eq 1 ]
    [ "$output" = "" ]
}

@test "1.1.13 Ensure /var/tmp partition includes the nosuid option (Automated)" {
    run bash -c "findmnt -n /var/tmp | grep -v nosuid"
    [ "$status" -eq 1 ]
    [ "$output" = "" ]
}

@test "1.1.14 Ensure /var/tmp partition includes the noexec option (Automated)" {
    run bash -c "findmnt -n /var/tmp | grep -v noexec"
    [ "$status" -eq 1 ]
    [ "$output" = "" ]
}
