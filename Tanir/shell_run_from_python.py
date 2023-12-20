import subprocess

# Replace 'your_password' with the actual root password
root_password = '#Tanir2002'

# Replace 'command_to_run_as_root' with the command you want to execute as root
command_to_run_as_root = 'ls /root/home/tanir'

# Create the command to echo the root password and execute the desired command
full_command = f'echo {root_password} | sudo -S {command_to_run_as_root}'

# Run the command
result = subprocess.run(full_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

#script_path = './Hard_Script_1.7.4.sh'
#subprocess.run(['bash', script_path])

# Print the result
print(result.stdout)
print(result.stderr)
