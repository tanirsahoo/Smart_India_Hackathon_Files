@test "6.2.1 Ensure accounts in /etc/passwd use shadowed passwords" {
  run bash -c 'awk -F: '\''($2 != "x" ) { print $1 " is not set to shadowed passwords "}'\'' /etc/passwd'
  [ "$status" -eq 0 ] # returns nothing
  [[ "$output" == "" ]]
}

@test "6.2.3 Ensure all groups in /etc/passwd exist in /etc/group" {
  run sudo "$BATS_TEST_DIRNAME"/6.2.3.sh
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]
}