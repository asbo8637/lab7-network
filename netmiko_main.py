from netmiko import ConnectHandler

routers = [
    {
        "name": "R1",
        "device_type": "cisco_ios",
        "host": "198.51.100.11",
        "username": "root",
        "password": "cisco"
    },
    {
        "name": "R2",
        "device_type": "cisco_ios",
        "host": "198.51.100.12",
        "username": "root",
        "password": "root"
    },
    {
        "name": "R3",
        "device_type": "cisco_ios",
        "host": "198.51.100.13",
        "username": "root",
        "password": "root"
    }
]

for router in routers:

    print(f"\nConnecting to {router['name']}")

    connection = ConnectHandler(**router)

    config_file = f"roles/routers/files/{router['name']}.conf"

    with open(config_file) as f:
        commands = f.read().splitlines()

    output = connection.send_config_set(commands)

    print(output)

    connection.save_config()

    connection.disconnect()

print("Oh yeah:")
print("All routers configured.")