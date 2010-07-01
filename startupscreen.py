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

##[ Name        ]## startupscreen
##[ Maintainer  ]## Niels Serup <ns@metanohi.org>
##[ Description ]## Controls the loading screen of the startup process

import os.path
import time
import pygame
from questylib.various import thread

class StartupScreen:
    def loading_data(self, event):
        if event.name == 'beforecharactercreate':
            s = 'Creating character %s...' % event.args[0]
        elif event.name == 'beforeplacesload':
            self.startup_places_num = event.args[1]
            s = 'Loading places...'
        elif event.name == 'beforeplaceload':
            s = 'Loading place %s of %s...' % (event.args[1],
                                               self.startup_places_num)
        elif event.name == 'afterplacesload':
            del self.startup_places_num
            s = 'Finished loading places'
        self.current_startup_string = s

    def animate_startbg(self):
        i = 0
        w = 1
        m = len(self.startbgobjs)
        rectsurf = pygame.Surface((620, 50)).convert_alpha()
        rectsurf.fill((255, 255, 255, 200))
        while not self.animating_startbg_done:
            self.world.blit(self.startbg)
            self.world.blit(*self.startbgobjs[i])
            self.world.blit(rectsurf, (10, 410))
            self.world.blit(self.std_font.write(self.current_startup_string),
                            (20, 420))
            self.world.flip()
            i += w
            if i == m or i == -1:
                w *= -1
                i += w * 2
            time.sleep(0.15)

    def start_startupscreen(self, infopath):
        pinfo = self.get_path_data(infopath)[1]['.'][1]
        self.startbgobjs = range(len(pinfo) - 1)
        for x in pinfo:
            path = os.path.join(infopath, x)
            if x.find('-obj') != -1:
                imp = x.split('-obj')[1].split('.')[0].split('-')
                num = int(imp[0])
                pos = [int(y) for y in imp[1].split(',')]
                self.startbgobjs[num] = (self.world.load_image(path), pos)
            else:
                self.startbg = self.world.load_image(path, False)

        self.current_startup_string = 'Loading...'
        self.sys.signalactions.add('beforecharactercreate',
                                   self.loading_data)
        self.sys.signalactions.add('beforeplacesload', self.loading_data)
        self.sys.signalactions.add('beforeplaceload', self.loading_data)
        self.sys.signalactions.add('afterplacesload', self.loading_data)

        self.animating_startbg_done = False
        thread(self.animate_startbg)

    def end_startupscreen(self):
        self.animating_startbg_done = True
        self.sys.signalactions.remove('beforecharactercreate',
                                   self.loading_data)
        self.sys.signalactions.remove('beforeplacesload', self.loading_data)
        self.sys.signalactions.remove('beforeplaceload', self.loading_data)
        self.sys.signalactions.remove('afterplacesload', self.loading_data)
