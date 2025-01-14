import sys  # Import the sys module

# Print sys.argv to see the list of command-line arguments
print("Command-line arguments:", sys.argv)

# Access arguments
a = int(sys.argv[1])  # Convert first argument to integer
b = int(sys.argv[2])  # Convert second argument to integer

# Perform calculation
c = a + b

# Print result
print(f"{a} + {b} = {c}")
