import csv
import os

output_dir = "routers/vars"
os.makedirs(output_dir, exist_ok=True)

with open("vars.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        router_name = row["router"]
        file_path = os.path.join(output_dir, f"{router_name}.yml")

        with open(file_path, "w") as f:
            for key, value in row.items():
                if key != "router":
                    if value == "":
                        f.write(f"{key}: \n")
                    elif key in ["ospf_process", "ospf_area"]:
                        f.write(f"{key}: {value}\n")
                    else:
                        f.write(f'{key}: "{value}"\n')