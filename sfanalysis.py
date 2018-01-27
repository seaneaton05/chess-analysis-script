#Importing chess.uci package which is part of the python-chess library that allows us to communicate with the engine. ConfigParser lets us define engine parameters from a config file.
import chess.uci
import ConfigParser

#Reading and defining config file items..
config = ConfigParser.ConfigParser()
config.read('engineconfig.cnf')
engineDir = config.get('engine_parameters', 'chessengine')
boardPos = config.get('engine_parameters', 'fen')
engine  = chess.uci.popen_engine(engineDir)
board = chess.Board(boardPos)

#Running the engine and displaying results
engine.uci()
engine.position(board)
print "Engine: ", engine.name
print "Author(s): ", engine.author
print ""
print board
print ""
print engine.go(depth=20)
print ""
engine.quit()
