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

##[ Name        ]## places
##[ Maintainer  ]## Niels Serup <ns@metanohi.org>
##[ Description ]## Contains classes for places with special structures


class PlaceChanger:
    def __init__(self, world, *args):
        self.world = world
        self.init(*args)

    def init(self, *args):
        pass

class UpAndDown(PlaceChanger):
    def __call__(self, pos):
        s = self.world.size[1] - pos[1]
        if s < 100:
            return pos
        elif 100 <= s < 200:
            return pos[0], self.world.size[1] - (200 - s)
        else:
            return pos[0], pos[1] + 200

class AdvancedPower(PlaceChanger):
    def init(self, power, minus = 0):
        self.power = power
        self.minus = minus

    def __call__(self, pos):
        return (float(pos[1]) / self.world.size[1]) ** self.power - self.minus

class PlaceDetails:
    def c(self, clas, *args):
        return clas(self.world, *args)

    def improve_places(self):
        self.sys.emit_signal('beforeplacesimprove', self)
        places = self.world.places
        places[0].power = 1.6
        places[1].power = 1.6
        places[2].power = 1.8
        places[3].set_char_size(self.c(AdvancedPower, 1.5, .2))
        places[4].set_char_size(self.c(AdvancedPower, 1.5, .2))
        places[5].power = 1.3
        places[6].power = 1.4
        places[7].set_char_size(self.c(AdvancedPower, 1.4, .15))
        places[8].power = 1.7
        places[9].set_char_size(self.c(AdvancedPower, 1.7, .2))
        places[10].set_char_size(self.c(AdvancedPower, 1.8, .05))
        places[11].set_char_size(self.c(AdvancedPower, 1.3, -.2))
        places[12].set_char_size(self.c(AdvancedPower, 2.5, .05))
        places[13].set_char_size(self.c(AdvancedPower, 1.7, .05))
        places[14].power = 1.5
        places[15].set_char_size(self.c(AdvancedPower, 1.65, .07))
        self.sys.emit_signal('afterplacesimprove', self)
