@test "1.1.3 Ensure nodev option set on /tmp partition  " {
    run bash -c "findmnt -n /tmp | grep -v nodev"
    [ "$status" -eq 1 ]
    [ "$output" = "" ]
}

@test "1.1.4 Ensure nosuid option set on /tmp partition  " {
    run bash -c "findmnt -n /tmp | grep -v nosuid"
    [ "$status" -eq 1 ]
    [ "$output" = "" ]
}

@test "1.1.5 Ensure noexec option set on /tmp partition  " {
    run bash -c "findmnt -n /tmp | grep -v noexec"
    [ "$status" -eq 1 ]
    [ "$output" = "" ]
}