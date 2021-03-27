#!/usr/bin/env python3
"""Usage:
  saorga.py music [options] [encode]
  saorga.py -h | --help

Options:
  --to_play <to_play>           Song to play
  --add <new_song>              New song to add to the music library
"""

from docopt import docopt
from features import music_player

def main(args):
  print(args)
  if args['music']:
    if args['--add'] == True:
      music_player.add_song(args['<new_song'])
    elif args['--to_play']:
      music_player.play_song(args['<to_play>'])
    elif args['encode']:
      music_player.encode_songs()

if __name__ == "__main__":
  args = docopt(__doc__)
  main(args)
