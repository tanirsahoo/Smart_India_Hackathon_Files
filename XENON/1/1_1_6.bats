@test "1.7.4 Ensure permissions on /etc/motd are configured " {
    if [ -f /etc/motd ]; then
        run bash -c "stat -L /etc/motd | grep -E \"Uid: \([[:space:]]+0/[[:space:]]+root\)\""
        [ "$status" -eq 0 ]
        run bash -c "stat -L /etc/motd | grep -E \"Gid: \([[:space:]]+0/[[:space:]]+root\)\""
        [ "$status" -eq 0 ]
        run bash -c "stat -L /etc/motd | grep \"Access: (0644/\""
        [ "$status" -eq 0 ]
    fi
}

@test "1.7.5 Ensure permissions on /etc/issue are configured" {
    if [ -f /etc/issue ]; then
        run bash -c "stat /etc/issue | grep -E \"Uid: \([[:space:]]+0/[[:space:]]+root\)\""
        [ "$status" -eq 0 ]
        run bash -c "stat /etc/issue | grep -E \"Gid: \([[:space:]]+0/[[:space:]]+root\)\""
        [ "$status" -eq 0 ]
        run bash -c "stat /etc/issue | grep \"Access: (0644/\""
        [ "$status" -eq 0 ]
    fi
}

@test "1.7.6 Ensure permissions on /etc/issue.net are configured " {
    if [ -f /etc/issue.net ]; then
        run bash -c "stat /etc/issue.net | grep -E \"Uid: \([[:space:]]+0/[[:space:]]+root\)\""
        [ "$status" -eq 0 ]
        run bash -c "stat /etc/issue.net | grep -E \"Gid: \([[:space:]]+0/[[:space:]]+root\)\""
        [ "$status" -eq 0 ]
        run bash -c "stat /etc/issue.net | grep \"Access: (0644/\""
        [ "$status" -eq 0 ]
    fi
}
