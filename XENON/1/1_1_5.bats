@test "1.1.23 Disable Automounting  " {
    run bash -c "systemctl is-enabled autofs"
    if [ "$status" -eq 0 ]; then
        [ "$output" != "enabled" ]
    fi
}

@test "1.5.2 Ensure address space layout randomization (ASLR) is enabled  " {
    run bash -c "sysctl kernel.randomize_va_space"
    [ "$status" -eq 0 ]
    [[ "$output" == "kernel.randomize_va_space = 2" ]]
    run bash -c "grep -Es \"^\s*kernel\.randomize_va_space\s*=\s*([0-1]|[3-9]|[1-9][0-9]+)\" /etc/sysctl.conf /etc/sysctl.d/*.conf /usr/lib/sysctl.d/*.conf /usr/local/lib/sysctl.d/*.conf /run/sysctl.d/*.conf"
    [ "$status" -ne 0 ]
    [[ "$output" == "" ]]
}

@test "1.5.3 Ensure prelink is disabled  " {
    run bash -c "dpkg -s prelink | grep -E '(Status:|not installed)'"
    [ "$status" -eq 1 ]
    [[ "$output" == *"dpkg-query: package 'prelink' is not installed and no information is available"* ]]
}


@test "1.6.1.1 Ensure AppArmor is installed  " {
    run bash -c "dpkg -s apparmor | grep -E '(Status:|not installed)'"
    [ "$status" -eq 0 ]
    [[ "$output" == *"Status: install ok installed"* ]]
}



