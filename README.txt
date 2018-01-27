Background
---------------

Author: Sean Eaton

This purpose of this script is to quickly install a chess engine to use for analysis(Stockfish by default) on a Linux cloud instance such as Amazon's EC2 service. It will automatically grab the necessary packages and install them, with authentication and install confirmation all that is needed from the user.


How to use
---------------

1. Run installscript.sh and confirm package installation as requested.

2. Open engineconfig.cnf with your preferred text editor and replace the FEN with one of your choice. Stockfish is the default engine to use but you may change the path to an engine of your choice.

3. Run sfanalysis.py to show engine details, a textual display of the board position, and the engine's best move followed by best response(ponder).


Requirements
---------------

- Must be running a Red Hat derived distro using yum package manager. One could edit installscript.sh to use apt-get once they find the names for the packages installed.

- If you want to an engine other than Stockfish, this python script only supports UCI protocol engines.


Changelog
---------------

1/27/2018 - Initial version is released!
