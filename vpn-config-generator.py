import os
from jinja2 import Environment, FileSystemLoader

# Load templates
env = Environment(loader=FileSystemLoader(''))  # Assumes templates are in current directory

def ask_variables(variables):
    data = {}
    for var in variables:
        data[var] = input(f"Enter value for '{var}': ")
    return data


def render_template(template_file, context, output_file):
    template = env.get_template(template_file)
    config = template.render(context)
    with open(output_file, 'w') as f:
        f.write(config)
    print(f"✅ Generated config file: {output_file}")

# Step 1: Ask which VPNs to configure
q1 = input("Do you want to configure Dial-up VPN? (yes/no): ").lower()
q2 = input("Do you want to configure Hub & Spoke VPN? (yes/no): ").lower()
q3 = input("Do you want to configure Site-to-Site VPN? (yes/no): ").lower()

# Step 2: Handle each template based on user choice

if q1 == 'yes':
    print("\n--- Dial-up VPN ---")
    print("First, Server Configuration:")
    server_vars = ["vdom_name", "site_name", "outgoing_interface", "client_name", "client_url",
                   "psksecret", "local_vpn_ip", "remote_vpn_ip"]
    server_data = ask_variables(server_vars)
    render_template("templates/dialup-server.jinja", server_data,
                    "outconf/output_dialup_server.conf")

    print("Now, Client Configuration:")
    client_vars = ["vdom_name", "site_name", "outgoing_interface", "client_name", "remote_gateway_static_IP",
                   "psksecret", "client_url", "local_vpn_ip", "remote_vpn_ip"]
    client_data = ask_variables(client_vars)
    render_template("templates/dialup-client.jinja", client_data,
                    "outconf/output_dialup_client.conf")

if q2 == 'yes':
    print("\n--- Hub & Spoke VPN ---")
    print("Hub Configuration:")
    hub_vars = ["vdom_name", "site_name", "outgoing_interface", "remote_gateway", "psksecret"]
    hub_data = ask_variables(hub_vars)
    render_template("templates/hub-spoke-hub.jinja", hub_data,
                    "outconf/output_hub.conf")

    print("Spoke Configuration:")
    spoke_vars = ["vdom_name", "site_name", "outgoing_interface", "psksecret", "hub_id"]
    spoke_data = ask_variables(spoke_vars)
    render_template("templates/hub-spoke-spoke.jinja", spoke_data,
                    "outconf/output_spoke.conf")

if q3 == 'yes':
    print("\n--- Site-to-Site VPN ---")
    s2s_vars = ["vdom_name", "site_name", "outgoing_interface", "remote_gateway", "psksecret"]
    s2s_data = ask_variables(s2s_vars)
    render_template("templates/site2site.jinja", s2s_data,
                    "outconf/output_s2s.conf")
