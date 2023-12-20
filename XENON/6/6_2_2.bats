@test "6.2.8 Ensure no users have .netrc files" {
  run "$BATS_TEST_DIRNAME"/6.2.8.sh
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]
}

@test "6.2.9 Ensure no users have .forward files" {
  run "$BATS_TEST_DIRNAME"/6.2.9.sh
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]
}

@test "6.2.10 Ensure no users have .rhosts files" {
  run "$BATS_TEST_DIRNAME"/6.2.10.sh
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]
}

@test "6.2.11 Ensure root is the only UID 0 account " {
  run bash -c "awk -F: '(\$3 == 0) { print \$1 }' /etc/passwd"
  [[ "$output" == "root" ]]
  [ "$status" -eq 0 ]
}

@test "6.2.12 Ensure root PATH Integrity " {
  run "$BATS_TEST_DIRNAME"/6.2.12.sh
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]
}

@test "6.2.13 Ensure no duplicate UIDs exist " {
  run "$BATS_TEST_DIRNAME"/6.2.13.sh
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]
}

@test "6.2.14 Ensure no duplicate GIDs exist " {
  run "$BATS_TEST_DIRNAME"/6.2.14.sh
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]
}

@test "6.2.15 Ensure no duplicate user names exist " {
  run "$BATS_TEST_DIRNAME"/6.2.15.sh
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]
}

@test "6.2.16 Ensure no duplicate group names exist " {
  run "$BATS_TEST_DIRNAME"/6.2.16.sh
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]
}

@test "6.2.17 Ensure shadow group is empty " {
  run bash -c 'awk -F: '\''($1=="shadow") {print $NF}'\'' /etc/group'
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]

  run bash -c 'awk -F: -v GID="$(awk -F: '\''($1=="shadow") {print $3}'\'' /etc/group)" '\''($4==GID) {print $1}'\'' /etc/passwd'
  [ "$status" -eq 0 ]
  [[ "$output" == "" ]]
}