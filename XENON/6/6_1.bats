@test "6.1.2 Ensure permissions on /etc/passwd are configured" {
  run bash -c "stat /etc/passwd"
  [[ "$output" = *"Uid:"*"("*"0/"*"root"* ]]
  [[ "$output" = *"Gid:"*"("*"0/"*"root"* ]]
  [[ "$output" = *"Access:"*"(0644"* ]]
}

@test "6.1.3 Ensure permissions on /etc/passwd- are configured" {
  run bash -c "stat /etc/passwd-"
  [[ "$output" = *"Uid:"*"("*"0/"*"root"* ]]
  [[ "$output" = *"Gid:"*"("*"0/"*"root"* ]]
  [[ "$output" = *"Access:"*"(0"[0246][04][04]* ]]
}

@test "6.1.4 Ensure permissions on /etc/group are configured" {
  run bash -c "stat /etc/group"
  [[ "$output" = *"Uid:"*"("*"0/"*"root"* ]]
  [[ "$output" = *"Gid:"*"("*"0/"*"root"* ]]
  [[ "$output" = *"Access:"*"(0644"* ]]
}

@test "6.1.5 Ensure permissions on /etc/group- are configured" {
  run bash -c "stat /etc/group-"
  [[ "$output" = *"Uid:"*"("*"0/"*"root"* ]]
  [[ "$output" = *"Gid:"*"("*"0/"*"root"* ]]
  [[ "$output" = *"Access:"*"(0"[0246][04][04]* ]]
}

@test "6.1.6 Ensure permissions on /etc/shadow are configured" {
  run bash -c "stat /etc/shadow"
  [[ "$output" = *"Access:"*"(0"[0246][04][0]* ]]
  [[ "$output" = *"Uid:"*"("*"0/"*"root"* ]]
  # both root and shadow are regarded as safe
  # gid>0 for shadow and gid=0 for root
  ROOT_SHADOW_EXPR=".*Gid:[[:space:]]*(\([[:space:]]*[1-9][0-9]*\/[[:space:]]*shadow\)|\([[:space:]]*0\/[[:space:]]*root\)).*"
  [[ "$output" =~ $ROOT_SHADOW_EXPR ]]
}

@test "6.1.7 Ensure permissions on /etc/shadow- are configured" {
  run bash -c "stat /etc/shadow-"
  [[ "$output" = *"Access:"*"(0"[0246][04][0]* ]]
  [[ "$output" = *"Uid:"*"("*"0/"*"root"* ]]
  # both root and shadow are regarded as safe
  # gid>0 for shadow and gid=0 for root
  ROOT_SHADOW_EXPR=".*Gid:[[:space:]]*(\([[:space:]]*[1-9][0-9]*\/[[:space:]]*shadow\)|\([[:space:]]*0\/[[:space:]]*root\)).*"
  [[ "$output" =~ $ROOT_SHADOW_EXPR ]]
}

@test "6.1.8 Ensure permissions on /etc/gshadow are configured" {
  run bash -c "stat /etc/gshadow"
  [[ "$output" = *"Access:"*"(0"[0246][04][0]* ]]
  [[ "$output" = *"Uid:"*"("*"0/"*"root"* ]]
  # both root and shadow are regarded as safe
  # gid>0 for shadow and gid=0 for root
  ROOT_SHADOW_EXPR=".*Gid:[[:space:]]*(\([[:space:]]*[1-9][0-9]*\/[[:space:]]*shadow\)|\([[:space:]]*0\/[[:space:]]*root\)).*"
  [[ "$output" =~ $ROOT_SHADOW_EXPR ]]
}

@test "6.1.9 Ensure permissions on /etc/gshadow- are configured" {
  run bash -c "stat /etc/gshadow-"
  [[ "$output" = *"Access:"*"(0"[0246][04][0]* ]]
  [[ "$output" = *"Uid:"*"("*"0/"*"root"* ]]
  # both root and shadow are regarded as safe
  # gid>0 for shadow and gid=0 for root
  ROOT_SHADOW_EXPR=".*Gid:[[:space:]]*(\([[:space:]]*[1-9][0-9]*\/[[:space:]]*shadow\)|\([[:space:]]*0\/[[:space:]]*root\)).*"
  [[ "$output" =~ $ROOT_SHADOW_EXPR ]]
}
