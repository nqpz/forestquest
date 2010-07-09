#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ForestQuest: an exiting RPG to be run using the Dililatum engine
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
This is ForestQuest, an RPG game meant to be run using the Dililatum RPG
engine. If you have Dililatum installed, it is advised that you run
it like this if you want to play ForestQuest:

    $ dililatum forestquest

Both Dililatum and ForestQuest must be properly installed for this to
work. Downloads and installation instructions are available at
<http://metanohi.org/projects/dililatum/> and at
<http://metanohi.org/projects/forestquest/>.'''

try:
    from dililatum.game import GenericGame
    from forestquest.startupscreen import StartupScreen
    from forestquest.startmenuscreen import StartMenu
    from forestquest.places import PlaceDetails
    from forestquest.bgmusic import BackgroundMusic
    import forestquest.generalinformation as ginfo
except ImportError:
    import sys
    print forestquest_help
    sys.exit()

class Game(GenericGame, StartupScreen, StartMenu, PlaceDetails, BackgroundMusic):
    name = 'ForestQuest'
    shortname = 'fquest'

    def start_game(self):
        self.status('''\
Welcome to ForestQuest. This is version %s of the game. ForestQuest's
program part is free software under the terms of the GNU GPLv3+. Its
data part is free content, mostly released under the Creative Commons
Attribution-Share Alike 3.0+ Unported license. Read more about this on
<http://metanohi.org/projects/forestquest/>.''' % ginfo.version)

        self.create_world()
        self.world.start()

        #### LOAD DATA BEGIN ####
        self.status('Loading data...')

        # Load icon
        self.world.load_icon('icons/icon-32x32.png')

        # Create font
        self.std_font = self.world.create_font(path='fonts/chumbly.ttf')

        # Start startup screen
        self.start_startupscreen('startbg')

        # Load characters
        self.protagonist = self.load_character('protagonist')
        self.mantis0 = self.load_character('mantis0')

        # Load sounds and music
        self.sounds = self.load_sounds('sounds')
        self.music = self.load_sounds('music')

        # Load places
        self.load_places('places/images', 'places/okpositions',
                         'places/overlays')
        self.improve_places()

        # Load map linking the places together
        self.use_data_from_map('places/map')

        # Load message boxes
        self.msgbox = \
            self.load_msgbox(bgimg='messageboxes/simplegradient0.png',
                             font=self.std_font)

        # Distribute background sounds and music to all places
        self.append_bg_sounds()

        # End startup screen
        self.end_startupscreen()

        #### LOAD DATA END ####

        #self.start_startmenuscreen()

        self.world.set_default_msgbox(self.msgbox)
        self.world.set_leading_character(self.protagonist)
        self.protagonist.say('Hello')
        self.world.set_place(62, (300, 300))

    def run_game(self):
        self.status('Full speed!')
        self.world.run()


if __name__ == '__main__':
    print forestquest_help
