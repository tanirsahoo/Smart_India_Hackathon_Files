import grp

def list_all_groups():
    try:
        groups = grp.getgrall()
        print("All groups on the system:")
        for group in groups:
            print(group.gr_name)
    except Exception as e:
        print(f"Error listing groups: {e}")

def main():
    list_all_groups()

if __name__ == "__main__":
    main()
