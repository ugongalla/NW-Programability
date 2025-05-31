from netmiko import ConnectHandler
# create device object using dictonary
Device = {'device_type: cisco_IOS', 'IP:192.168.1.2', 'username:admin', ' password:cisco123'}

# connect to device using ssh

ssh_connect = ConnectHandler(**Device)

#send the command to device and print output

output = ssh_connect.command_send('show ip int br')
print(output)

# Finally close the connection
ssh_connect.disconnect()

