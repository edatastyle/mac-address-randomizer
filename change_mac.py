#!/usr/bin/python3
import random, subprocess, argparse, sys

def generate_random_mac():
    """Generate a valid random MAC address."""
    random_mac = [
        random.randint(0x00, 0xFF),  # First byte
        random.randint(0x00, 0xFF),
        0x00,  # Organizationally Unique Identifier (can vary)
        0x99,  # Custom value
        random.randint(0x00, 0xFF),
        random.randint(0x00, 0xBB)
    ]
    # Ensure the locally administered address bit is set
    random_mac[0] = random_mac[0] & 0xFE | 0x02
    return ":".join(map(lambda x: "%02x" % x, random_mac))

def change_mac_address(interface):
    """Change the MAC address of a given network interface."""
    mac_addr = generate_random_mac()
    print(f"Generated MAC Address: {mac_addr}")

    try:
        # Show current interface status
        subprocess.run(["ip", "link", "show", "dev", interface], check=True)
        
        # Bring the interface down
        subprocess.run(["ip", "link", "set", "dev", interface, "down"], check=True)
        
        # Set the new MAC address
        subprocess.run(["ip", "link", "set", "dev", interface, "addr", mac_addr], check=True)
        
        # Bring the interface back up
        subprocess.run(["ip", "link", "set", "dev", interface, "up"], check=True)
        
        # Show updated interface status
        subprocess.run(["ip", "link", "show", "dev", interface], check=True)
        
        print(f"MAC Address for {interface} changed successfully to {mac_addr}")
    except subprocess.CalledProcessError as e:
        print(f"Error while executing command: {e}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Changes the MAC address of the specified network interface to a randomly generated one.")
    parser.add_argument("-i", "--interface", help="Enter your interface or device ID")
    
    args = parser.parse_args()
    interface = args.interface

    change_mac_address(interface=interface)
    sys.exit()