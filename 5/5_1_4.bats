@test "5.5.3 Ensure default group for the root account is GID 0" {
    run bash -c "grep \"^root:\" /etc/passwd | cut -f4 -d:"
    [ "$status" -eq 0 ]
    [[ "$output" == "0" ]]
}