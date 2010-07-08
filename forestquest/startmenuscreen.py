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

##[ Name        ]## startmenuscreen
##[ Maintainer  ]## Niels Serup <ns@metanohi.org>
##[ Description ]## Controls the screen content in the first menu of
                  # the game

import time
import pygame
from dililatum.various import thread

class StartMenu:
    def animate_startmenubg(self):
        clock = pygame.time.Clock()
        m = len(self.startbgobjs)
        i = [0, 1]
        k = 0
        rectsurf = pygame.Surface((620, 460)).convert_alpha()
        rectsurf.fill((255, 155, 55, 100))
        while not self.animating_startmenubg_done:
            self.world.blit(self.startbg)
            self.world.blit(*self.startbgobjs[i[0]])
            self.world.blit(*self.startbgobjs[i[1] + 2])
            self.world.blit(rectsurf, (10, 10))
            self.world.flip()
            k += 1
            if k == 6:
                k = 0
                for j in range(len(i)):
                    if i[j] == 0:
                        i[j] = 1
                    else:
                        i[j] = 0
            clock.tick(30)

    def start_startmenuscreen(self):
        # Loading screen must have been created for this to work
        self.animating_startmenubg_done = False
        self.animate_startmenubg()

    def end_startmenuscreen(self):
        self.animating_startmenubg_done = True
