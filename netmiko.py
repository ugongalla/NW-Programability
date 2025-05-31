from netmiko import ConnectHandler
#ssh script to connect to device
# Define the device parameters
cisco_device = {
    'device_type': 'cisco_ios',      # Device platform
    'host': '192.168.1.1',           # Replace with the actual IP address
    'username': 'admin',             # Replace with actual username
    'password': 'admin123',          # Replace with actual password
    'secret': 'enablepassword',      # Enable password, if required
}

try:
    print(f"Connecting to {cisco_device['host']}...")

    # Establish SSH connection
    net_connect = ConnectHandler(**cisco_device)

    # Enter enable mode
    net_connect.enable()

    # Run a command
    output = net_connect.send_command("show version")

    # Print the output
    print("\n--- Command Output ---\n")
    print(output)

    # Disconnect
    net_connect.disconnect()
    print("\nConnection closed.")

except Exception as e:
    print(f"Connection failed: {e}")
