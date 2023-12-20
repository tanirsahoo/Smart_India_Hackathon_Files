@test "1.8.4 Ensure XDCMP is not enabled " {
    run bash -c "grep -Eis '^\s*Enable\s*=\s*true' /etc/gdm3/custom.conf"
    [ "$status" -ne 0 ]
    [[ "$output" = "" ]]
}