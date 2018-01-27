#!/bin/bash

sudo yum install git gcc-c++ python python-devel xz xz-devel
sudo pip install backports.lzma
sudo pip install python-chess[engine,gaviota]
git clone https://github.com/official-stockfish/Stockfish.git
cd Stockfish/src

make profile-build ARCH=x86-64
cd ../..
chmod 777 sfanalysis.py
