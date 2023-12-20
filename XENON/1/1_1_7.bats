@test "1.8.2 Ensure GDM login banner is configured " {
    if dpkg -s gdm3; then
        run bash -c "cat /etc/gdm3/greeter.dconf-defaults"
        [ "$status" -eq 0 ]
        [[ "$output" = *"[org/gnome/login-screen]"* ]]
        [[ "$output" = *"banner-message-enable=true"* ]]
        [[ "$output" = *"banner-message-text="* ]]
    fi
}