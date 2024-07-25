from fabric.api import *

# Set the name of the user login to the remote host
env.user = 'yzabala'
env.port = '2222'  # <-- please replace with the actual value of your VM's port number
env.hosts = ['localhost']

# Define the task to get the hostname of remote machines
def getHostname():
    name = run("hostname")
    print("The host name is:", name)

def installPackage(pkg='dummy'):
    cmd = 'yum install ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def removePackage(pkg=''):
    if pkg == '':
        cmd = 'yum remove dummy -y'
    else:
        cmd = 'yum remove ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def updatePackage(pkg=''):
    cmd = 'yum update ' + pkg + ' -y'
    status = sudo(cmd)
    print(status)

def makeUser():
    # Create a new user called "ops445p" with home directory "/home/ops445p"
    sudo("useradd -m -d /home/ops445p ops445p")
    
    # Add the new user to the sudo group called "wheel"
    sudo("usermod -aG wheel ops445p")
    
    # Get the SSH public key from the instructor (assumed to be in instructor_key.pub)
    local("scp -P {0} instructor_key.pub {1}@{2}:/tmp/instructor_key.pub".format(env.port, env.user, env.hosts[0]))
    
    # Create .ssh directory for the new user and set permissions
    sudo("mkdir -p /home/ops445p/.ssh")
    sudo("chown ops445p:ops445p /home/ops445p/.ssh")
    sudo("chmod 700 /home/ops445p/.ssh")
    
    # Move the public key to the authorized_keys file and set permissions
    sudo("mv /tmp/instructor_key.pub /home/ops445p/.ssh/authorized_keys")
    sudo("chown ops445p:ops445p /home/ops445p/.ssh/authorized_keys")
    sudo("chmod 600 /home/ops445p/.ssh/authorized_keys")

    # Clean up by removing the temporary key file
    sudo("rm -f /tmp/instructor_key.pub")
