# python

# https://www.python.org/downloads/
# Gzipped source tarball
# https://www.python.org/ftp/python/3.9.18/Python-3.9.18.tgz

wget https://www.python.org/ftp/python/3.9.18/Python-3.9.18.tgz
tar -xzf Python-3.9.18.tgz 
cd Python-3.9.18
./configure --enable-optimizations --with-ensurepip=install --prefix=/path/to/your/filesystem
make
make install
# or altinstall if you already have a python on that path and don't want to overwrite the symlinks

[user@host python]$ /path/to/your/filesystem/python/bin/python3.9 --version
Python 3.9.18

# wrong path?
make clean
./configure --enable-optimizations --with-ensurepip=install --prefix=/new/path
make
make install
# or altinstall if you already have a python on that path and don't want to overwrite the symlinks
make altinstall

# extra packages needed?
python-gofer.noarch
python-gofer-proton.noarch
python-isodate.noarch
python-pulp-common.noarch
python-qpid-proton.x86_64
qpid-proton-c.x86_64

yum groupinstall "Development Tools"
yum install bison byacc cscope ctags cvs diffstat doxygen flex gcc gcc-c++ gcc-gfortran gettext git indent intltool libtool patch patchutils rcs redhat-rpm-config rpm-build subversion swig systemtap

########################### python install
yum -y update --skip-broken
yum -y groupinstall "Development Tools"
yum -y install gcc openssl-devel bzip2-devel libffi-devel sqlite-devel sqlite-libs.i686 


https://realpython.com/installing-python/#how-to-build-python-from-source-code

wget https://www.python.org/ftp/python/3.11.1/Python-3.11.1.tgz
tar -xzvf Python-3.11.1.tgz
cd Python*
./configure --enable-optimizations --with-ensurepip=install --prefix=$HOME/python-3.9.7
make -j 8
# to install on /usr/bin, makeinstall would replace currenlty installed!!!
# --prefix should replace /usr/bin with whatever you choose
sudo make altinstall
