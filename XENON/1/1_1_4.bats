@test "1.1.18 Ensure /home partition includes the nodev option" {
    run bash -c "findmnt -n /home | grep -v nodev"
    [ "$status" -eq 1 ]
    [ "$output" = "" ]
}