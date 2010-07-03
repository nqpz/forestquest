#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ForestQuest: An exiting RPG to be run using the Questy engine
# Copyright (C) 2010  Niels Serup

# This file is part of ForestQuest.
#
# ForestQuest is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ForestQuest is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ForestQuest.  If not, see <http://www.gnu.org/licenses/>.

##[ Name        ]## game
##[ Maintainer  ]## Niels Serup <ns@metanohi.org>
##[ Description ]## Controls the ForestQuest game

forestquest_help = '''\
This is ForestQuest, an RPG game meant to be run using the Questy RPG
engine. If you have Questy installed, it is advised that you run
it like this if you want to play ForestQuest:

    $ questy forestquest

Both Questy and ForestQuest must be properly installed for this to
work. Downloads and installation instructions are available at
<http://metanohi.org/projects/questy/> and at
<http://metanohi.org/projects/forestquest/>.'''

try:
    from questylib.game import GenericGame
    from forestquest.startupscreen import StartupScreen
    from forestquest.places import PlaceDetails
except ImportError:
    import sys
    print forestquest_help
    sys.exit()

class Game(GenericGame, StartupScreen, PlaceDetails):
    name = 'ForestQuest'
    shortname = 'fquest'

    def start_game(self):
        self.status('''\
Welcome to ForestQuest. This is version 0.1 of the game. ForestQuest's
program part is free software under the terms of the GNU GPLv3+. Its
data part is free content under the Creative Commons
Attribution-Share Alike 3.0+ Unported license. Read more about this on
<http://metanohi.org/projects/forestquest/>.''')

        self.create_world()
        self.world.start()

        self.status('Loading data...')

        # Load icon
        self.world.load_icon('icons/icon-32x32.png')

        self.std_font = self.world.create_font(path='fonts/chumbly.ttf')

        # Start startup screen
        self.start_startupscreen('startbg')

        # Character creation
        self.protagonist = self.world.create_character(
            'protagonist', self.get_path_data('protagonist'))
        self.world.add_character(self.protagonist)
        self.world.set_leading_character(self.protagonist)

        # Load places
        self.load_places('places/images', 'places/okpositions',
                         'places/overlays')
        self.improve_places()

        # Load map linking the places together
        self.use_data_from_map('places/map')

        # End startup screen
        self.end_startupscreen()

        self.world.set_place(62, (300, 300))

    def run_game(self):
        self.status('Full speed!')
        self.world.run()


if __name__ == '__main__':
    print forestquest_help
