import subprocess

def delete_group(group_name):
    # Delete the group
    delete_group_cmd = ['sudo', 'delgroup', group_name]
    subprocess.run(delete_group_cmd, check=True)

if __name__ == "__main__":
    # Input the group name
    group_name = input("Enter the name of the group to delete: ")

    # Delete the group
    delete_group(group_name)
    print(f"Group '{group_name}' deleted successfully.")

