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
    from pygame.locals import *
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
        self.protagonist = self.load_character('protagonist', name='Guy')
        self.world.set_leading_character(self.protagonist)
        self.protagonist.show()
        self.mantis0 = self.load_character('mantis0', name='Mantis')

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
            self.load_msgbox(path='messageboxes/simplegradient0normal',
                             font=self.std_font)
        self.world.set_default_msgbox(self.msgbox)

        # Distribute background sounds and music to all places
        self.append_bg_sounds()

        # End startup screen
        self.end_startupscreen()

        #### LOAD DATA END ####

        #self.start_startmenuscreen()


        def howfeel():
            self.mantis0.ask('Here I am again. How are you feeling?',
                             ['Good.', self.mantis0.say, 'That\'s nice.'],
                             ['Bad.', self.mantis0.say, 'That\'s too bad.'],
                             ['1 of 10.', self.mantis0.say, 'Go for 2.'],
                             ['It depends on how you look at it. Maybe I\'m not even here right now. Maybe this digital representation of my very being is just an illusion of something that is not meant to exist.', self.mantis0.say, 'Sure.'],
                             ['3 of 11.', self.mantis0.say, 'Go for 4.'],
                             ['Nil.', self.mantis0.say, 'Lin.'],
                             ['Yo.', self.mantis0.say, 'No.']
                             )
        def welcome():
            self.mantis0.say('''\
Hi there! I'm a mantis! I don't really have a name yet, but you can \
call me Mantis. I am your guide. You don't have name, but you do have \
a mission. I don't know what it is, but I know it exists. This \
forest must be investigated by you for further information. That is \
all I know. But anyway, I must be going now. I have something \
todo. Good-ely-bye!\nYou should try touching the small box.''', endaction=[self.mantis0.hide])

        def begin(event):
            self.world.set_place(62, (300, 300))
            self.mantis0.set_position((300, 400))
            self.mantis0.show()
            welcome()

        self.sys.signalactions.add('beforeworldrun', begin)
        box = self.load_object(imgfile='objects/box0.png', pos=(250, 320),
                               areaadd=(0, 30), action=[howfeel],
                               walkonact=False, require=[KEYDOWN, K_SPACE])
        self.world.places[62].add_object(box)

    def run_game(self):
        self.status('Full speed!')
        self.world.run()

if __name__ == '__main__':
    print forestquest_help
