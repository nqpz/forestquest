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


class UpAndDown:
    def __init__(self, world):
        self.world = world

    def __call__(self, pos):
        s = self.world.size[1] - pos[1]
        if s < 100:
            return pos
        elif 100 <= s < 200:
            return pos[0], self.world.size[1] - (200 - s)
        else:
            return pos[0], pos[1] + 200
