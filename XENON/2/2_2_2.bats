@test "2.1.17 Ensure NIS Server is not installed (Automated)" {
    run bash -c "dpkg -s nis | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'nis' is not installed and no information is available"* ]]
}

@test "2.2.1 Ensure NIS Client is not installed (Automated)" {
    run bash -c "dpkg -s nis | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'nis' is not installed and no information is available"* ]]
}

@test "2.2.2 Ensure rsh client is not installed (Automated)" {
    run bash -c "dpkg -s rsh-client | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'rsh-client' is not installed and no information is available"* ]]
}

@test "2.2.3 Ensure talk client is not installed (Automated)" {
    run bash -c "dpkg -s talk | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'talk' is not installed and no information is available"* ]]
}

@test "2.2.5 Ensure LDAP client is not installed (Automated)" {
    run bash -c "dpkg -s ldap-utils | grep -E '(Status:|not installed)'"
    [[ "$output" == *"dpkg-query: package 'ldap-utils' is not installed and no information is available"* ]]
}
