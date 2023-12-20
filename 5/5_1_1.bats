@test "5.1.1 Ensure cron daemon is enabled and running" {
    run bash -c "systemctl is-enabled cron"
    [ "$status" -eq 0 ]
    [[ "$output" == "enabled" ]]
    run bash -c "systemctl status cron | grep 'Active: active (running) '"
    [ "$status" -eq 0 ]
    [[ "$output" == *"Active: active (running) since"* ]]
}