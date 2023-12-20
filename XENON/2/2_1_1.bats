@test "2.1.6 Ensure LDAP server is not installed  " {
    run bash -c "dpkg -s slapd | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'slapd' is not installed and no information is available"* ]]
}

@test "2.1.7 Ensure NFS is not installed  " {
    run bash -c "dpkg -s nfs-kernel-server | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'nfs-kernel-server' is not installed and no information is available"* ]]
}

@test "2.1.8 Ensure DNS Server is not installed  " {
    run bash -c "dpkg -s bind9 | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'bind9' is not installed and no information is available"* ]]
}

@test "2.1.9 Ensure FTP Server is not installed  " {
    run bash -c "dpkg -s vsftpd | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'vsftpd' is not installed and no information is available"* ]]
}

@test "2.1.10 Ensure HTTP server is not installed  " {
    run bash -c "dpkg -s apache2 | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'apache2' is not installed and no information is available"* ]]
}

@test "2.1.11 Ensure IMAP and POP3 server are not installed  " {
    run bash -c "dpkg -s dovecot-imapd dovecot-pop3d | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'dovecot-imapd' is not installed and no information is available"* ]]
    [[ "$output" == *"dpkg-query: package 'dovecot-pop3d' is not installed and no information is available"* ]]
}

@test "2.1.12 Ensure Samba is not installed  " {
    run bash -c "dpkg -s samba | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'samba' is not installed and no information is available"* ]]
}

@test "2.1.13 Ensure HTTP Proxy Server is not installed  " {
    run bash -c "dpkg -s squid | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'squid' is not installed and no information is available"* ]]
}

@test "2.1.14 Ensure SNMP Server is not installed  " {
    run bash -c "dpkg -s snmpd | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'snmpd' is not installed and no information is available"* ]]
}
