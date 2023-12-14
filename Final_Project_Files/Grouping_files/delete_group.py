import subprocess

def delete_group(group_name):
    try:
        subprocess.run(['sudo', 'delgroup', group_name], check=True)
        print(f"Group '{group_name}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error deleting group: {e}")

def main():
    group_name = input("Enter the name of the group to delete: ")

    delete_group(group_name)

if __name__ == "__main__":
    main()
