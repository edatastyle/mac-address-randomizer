#!/bin/bash

# Install dependencies
sudo apt-get install -y python3 iproute2

# Copy the Python script and wrapper to the appropriate locations
sudo cp change_mac.py /usr/local/bin/change_mac.py
sudo chmod +x /usr/local/bin/change_mac.py

# Create a wrapper script for easy execution
echo '#!/bin/bash' | sudo tee /usr/local/bin/change_mac > /dev/null
echo '/usr/bin/python3 /usr/local/bin/change_mac.py "$@"' | sudo tee -a /usr/local/bin/change_mac > /dev/null
sudo chmod +x /usr/local/bin/change_mac

echo "Installation complete. You can now run 'change_mac -i <interface>'"
