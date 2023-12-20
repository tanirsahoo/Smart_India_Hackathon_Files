#@test "5.3.2 Ensure permissions on SSH private host key files are configured" {
#    local SSH_CONFIG=$(find /etc/ssh -xdev -type f -name 'ssh_host_*_key' -exec stat {} \; | grep "Access" | grep "Uid")
#    while IFS= read -r line; do
#        [[ "$line" = *"Uid:"*"("*"0/"*"root"* ]]
#        [[ "$line" = *"Gid:"*"("*"0/"*"root"* ]]
#        [[ "$line" = "Access:"*"(0"[0-6]"00"* ]]
#    done <<< "$SSH_CONFIG"
#}

#@test "5.3.3 Ensure permissions on SSH public host key files are configured" {
#    local SSH_CONFIG=$(find /etc/ssh -xdev -type f -name 'ssh_host_*_key.pub' -exec stat {} \; | grep "Access" | grep "Uid")
#    while IFS= read -r line; do
#        [[ "$line" = "Access:"*"(0"[0-7][0\|4][0\|4]* ]]
#    done <<< "$SSH_CONFIG"
#}

@test "5.3.22 Ensure SSH MaxSessions is limited" {
    local MAXSESSIONS=$(sshd -T -C user=root -C host="$(hostname)" -C addr="$(grep $(hostname) /etc/hosts | awk '{print $1}')" | grep -i maxsessions)
    MAXSESSIONS=(${MAXSESSIONS// / }) # get number from string
    [[ "${MAXSESSIONS[1]}" -lt 11 ]]
    run bash -c "grep -Eis '^\s*MaxSessions\s+(1[1-9]|[2-9][0-9]|[1-9][0-9][0-9]+)' /etc/ssh/sshd_config /etc/ssh/sshd_config.d/*.conf"
    [ "$status" -ne 0 ]
    [[ "$output" == "" ]]
}