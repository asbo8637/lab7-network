from netmiko import ConnectHandler

routers = [
    {
        "name": "R1",
        "device_type": "cisco_ios",
        "host": "R1",
        "username": "root",
        "password": "cisco"
    },
    {
        "name": "R2",
        "device_type": "cisco_ios",
        "host": "R2",
        "username": "root",
        "password": "root"
    },
    {
        "name": "R3",
        "device_type": "cisco_ios",
        "host": "R3",
        "username": "root",
        "password": "root"
    }
]


for router in routers:
    print(f"\nConnecting to {router['name']}")

    # Remove the extra 'name' key for connect handler. It will not accept it.
    router_conn = dict(router)
    router_conn.pop('name', None)
    connection = ConnectHandler(**router_conn)

    config_file = f"roles/routers/files/{router['name']}.conf"
    with open(config_file) as f:
        commands = f.read().splitlines()

    output = connection.send_config_set(commands)
    print(output)
    connection.save_config()
    connection.disconnect()

print("Oh yeah:")
print("All routers configured.")