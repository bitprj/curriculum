$sys_deps = <<-SCRIPT
# Update the image
apt-get update
apt-get upgrade -y

# Install packages
apt-get install -y inxi
apt-get install -y git
apt-get install -y curl
apt-get install -y build-essential

# Update Message of the Day
cd /etc/update-motd.d
chmod -x *
touch 00-custom-header
cat >> 00-custom-header <<EOL
#!/bin/sh
echo ""
echo "########################################################"
echo "#                                                      #"
echo "#  Blockchain at Davis - DApp Development Environment  #"
echo "#               (BaD - DDE) now active                 #"
echo "#                                                      #"
echo "########################################################"
echo ""
echo "SYSTEM STATUS:"
inxi -I -c 0
echo "DISK STATUS:"
inxi -D -c 0
EOL

chmod +x 00-custom-header
cd ~

# Get node and npm installed
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
apt-get install -y nodejs
SCRIPT

$dev_deps = <<-SCRIPT
# Complete npm setup
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
touch .profile
echo "export PATH=~/.npm-global/bin:$PATH" >> .profile
source ~/.profile

# npm related packages
npm install -g truffle
npm install -g ganache-cli 
npm install -g web3
npm install -g ethers

# set node to recognize global package location
echo "export NODE_PATH=$(npm root -g)" >> .profile
source ~/.profile

# Setup complete
echo ""
echo "||| SETUP COMPLETE |||"
echo ""
echo ""
echo " Welcome to: "
echo ""
echo "██████╗  █████╗ ██████╗       ██████╗ ██████╗ ███████╗"
echo "██╔══██╗██╔══██╗██╔══██╗      ██╔══██╗██╔══██╗██╔════╝"
echo "██████╔╝███████║██║  ██║█████╗██║  ██║██║  ██║█████╗  "
echo "██╔══██╗██╔══██║██║  ██║╚════╝██║  ██║██║  ██║██╔══╝  "
echo "██████╔╝██║  ██║██████╔╝      ██████╔╝██████╔╝███████╗"
echo "╚═════╝ ╚═╝  ╚═╝╚═════╝       ╚═════╝ ╚═════╝ ╚══════╝"
echo ""
echo "Blockchain At Davis - DApp Development Environment"
SCRIPT
# Make sure the vagrant-disksize plugin is installed
required_plugins = %w(vagrant-disksize)

plugins_to_install = required_plugins.select { |plugin| not Vagrant.has_plugin? plugin }
if not plugins_to_install.empty?
  puts "Installing plugins: #{plugins_to_install.join(' ')}"
  if system "vagrant plugin install #{plugins_to_install.join(' ')}"
    exec "vagrant #{ARGV.join(' ')}"
  else
    abort "Installation of one or more plugins has failed. Aborting."
  end
end

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/xenial64"
  config.vm.provider "virtualbox" do |v|
    v.name = "BaD-DDE VM"
    v.customize ["modifyvm", :id, "--uartmode1", "disconnected"]
  end
  config.disksize.size = '15GB'

  # Setup environment name
  config.vm.define "BaD-DDE"
  config.vm.hostname = "BaD-DDE"

  # Execute Provisioning Scripts
  config.vm.provision "shell", inline: $sys_deps
  config.vm.provision "shell", inline: $dev_deps, privileged: false
  
  # Establish + Synchronize Folders
  config.vm.synced_folder "workbench/", "/home/vagrant/workbench", create: true
end
