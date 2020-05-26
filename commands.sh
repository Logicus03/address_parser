# Needed packages
apt-get install curl autoconf automake libtool pkg-config -y
apt-get install python3-dev -y
apt-get install libevent-dev -y

# Update pip
pip install --upgrade pip

# Install postal from conda
conda install -c conda-forge postal --y