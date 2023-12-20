@test "1.1.6 Ensure /dev/shm is configured  " {
    run bash -c "findmnt -n /dev/shm"
    [ "$status" -eq 0 ]
    [[ "$output" = "/dev/shm "* ]]
}

@test "1.1.7 Ensure nodev option set on /dev/shm partition  " {
    run bash -c "findmnt -n /dev/shm | grep -v nodev"
    [ "$status" -eq 1 ]
    [ "$output" = "" ]
}

@test "1.1.8 Ensure nosuid option set on /dev/shm partition  " {
    run bash -c "findmnt -n /dev/shm | grep -v nosuid"
    [ "$status" -eq 1 ]
    [ "$output" = "" ]
}