# VENDOR_ID extraction - issue
# have to remove the rule folder

import subprocess
import sys

def disable_usb_for_user(username):
    try:
        # Create a udev rule to disable USB for the specified user
        rule_content = 'ACTION=="add", SUBSYSTEM=="usb", ENV{ID_VENDOR_ID}!="", RUN+="/bin/sh -c \'/bin/echo {username} > /sys%p/authorized_users\'"'.format(username=username)

        # Write the rule to a temporary file
        rule_file_path = '/etc/udev/rules.d/99-disable-usb-for-{username}.rules'.format(username=username)
        with open(rule_file_path, 'w') as rule_file:
            rule_file.write(rule_content)

        # Reload udev rules
        subprocess.run(['sudo', 'udevadm', 'control', '--reload-rules'])
        subprocess.run(['sudo', 'udevadm', 'trigger'])

        print(f"USB access disabled for user: {username}")
    except Exception as e:
        print(f"Error: {e}")
  #  finally:
   #      Cleanup: Remove the temporary rule file
    #    subprocess.run(['sudo', 'rm', rule_file_path])

if __name__ == "__main__":
    username = input('Enter the username : ').strip()
    disable_usb_for_user(username)
