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

from questylib.game import GenericGame
from questylib.world import World
import forestquest.places as plc

class Game(GenericGame):
    name = 'ForestQuest'
    shortname = 'fquest'

    def start_game(self):
        self.status('''\
Welcome to ForestQuest. This is version 0.1 of the game. ForestQuest
-- both code and media -- is free software/content under the terms of
the GNU GPLv3+. Media is also available under the terms of the
Creative Commons Attribution-ShareAlike 3.0 Unported license. Read
more about this on <http://metanohi.org/projects/forestquest/>.''')

        self.status('Loading data...')
        self.world = World(self.sys, self.size)
        self.world.start()

        # Character creation
        self.protagonist = self.world.create_character(
            'protagonist', self.get_data('protagonist'))
        self.world.add_character(self.protagonist)
        self.world.set_leading_character(self.protagonist)

        # Loading of places
        self.load_places('places/images', 'places/okpositions')

        self.use_data_from_map('places/map-details')
        places = self.world.places
        places[0].power = 1.55
        places[1].power = 1.6
        places[2].power = 1.55

        self.world.set_place(places[0])

    def run_game(self):
        self.status('Full speed!')
        self.world.run()


if __name__ == '__main__':
    print '''\
This is ForestQuest, an RPG game meant to be run using the Questy RPG
engine. If you have Questy installed, it is advised that you run
it like this if you want to play ForestQuest:

    $ questy forestquest

Both Questy and ForestQuest must be properly installed for this to
work. Downloads and installation instructions are available at
<http://metanohi.org/projects/questy/> and at
<http://metanohi.org/projects/forestquest/>.'''
