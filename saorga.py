#!/usr/bin/env python3
"""Usage:
  saorga.py [music <to_play>]
  saorga.py -h | --help
"""

from docopt import docopt
from features import music_player

def main(args):
  print(args)
  if args['music']:
    music_player.play_song(args['<to_play>'])

if __name__ == "__main__":
  args = docopt(__doc__)
  main(args)
