@test "3.5.2.1 Ensure nftables is installed" {
    run bash -c "dpkg-query -s nftables | grep 'Status: install ok installed'"
    [[ "$output" == "Status: install ok installed" ]]
}