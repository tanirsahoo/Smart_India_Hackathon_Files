import grp
import pwd

def is_system_group(group):
    # Check if the group GID is in the common range for system groups
    return 0 < group.gr_gid < 1000

def is_admin_user(user):
    # Customize this list with usernames you consider as admin users
    admin_usernames = ["admin", "root"]
    return user.pw_name in admin_usernames

def display_user_created_groups():
    # Get all groups and their information
    groups = grp.getgrall()

    # Get all users and their information
    users = pwd.getpwall()

    # Display user-created group names along with associated usernames
    for group in groups:
        # Check if the group is not a system group and has members
        if not is_system_group(group) and group.gr_mem:
            group_name = group.gr_name
            group_members = [user.pw_name for user in users if user.pw_name in group.gr_mem and not is_admin_user(user)]
            
            # Check if the group has non-admin members
            if group_members:
                group_members_str = ",".join(group_members)
                print(f"Group: {group_name}, Members: {group_members_str}")

if __name__ == "__main__":
    display_user_created_groups()

