# vm_lab.py
# Starter script for PythonLabs VM exercises

# Optional: ask your name for personalization
name = input("Enter your name: ")

print(f"Hello, {name}! Welcome to your PythonLabs VM lab.\n")

# List of VM commands you practiced
commands = [
    "pwd",
    "ls -la",
    "whoami",
    "tree"
]

# Log commands to the screen
print("Logging commands:")
for cmd in commands:
    print(f"Command: {cmd}")

# Save commands to a file
with open("command_log.txt", "w") as file:
    for cmd in commands:
        file.write(cmd + "\n")

print("\nCommands saved to command_log.txt")
print("Lab complete! ✅")