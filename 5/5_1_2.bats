@test "5.2.1 Ensure sudo is installed" {
    run bash -c "dpkg -s sudo"
    if [ "$status" -ne 0 ]; then
        run bash -c "dpkg -s sudo-ldap"
        [ "$status" -eq 0 ]
    fi
}