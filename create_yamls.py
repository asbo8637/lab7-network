import csv
import os

output_dir = "roles/routers/vars"
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



# Create main.yml
main_yml_content = '''---
- name: Load router variables
  include_vars: "vars/{{ inventory_hostname }}.yml"

- name: Generate configuration file
  template:
    src: "lab_jinja2_template.j2"
    dest: "files/{{ inventory_hostname }}.conf"
'''

main_yml_path = os.path.join("roles", "routers", "tasks", "main.yml")
os.makedirs(os.path.dirname(main_yml_path), exist_ok=True)
with open(main_yml_path, "w") as main_yml_file:
    main_yml_file.write(main_yml_content)