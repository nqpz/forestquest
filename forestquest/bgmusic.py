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

##[ Name        ]## bgmusic
##[ Maintainer  ]## Niels Serup <ns@metanohi.org>
##[ Description ]## Adds bacground music to places

class BackgroundMusicGroup(list):
    def __init__(self, world, val):
        self.world = world
        list.__init__(self, val)

    def add(self, *snd):
        for x in self:
            for y in snd:
                self.world.places[x].bgsounds.append(y)

    def remove(self, *snd):
        for x in self:
            for y in snd:
                self.world.places[x].bgsounds.remove(y)

class BackgroundMusicGroups(dict):
    def __init__(self, world):
        self.world = world
        dict.__init__(self)

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, BackgroundMusicGroup(self.world, val))

class BackgroundMusic:
    def append_bg_sounds(self):
        self.sys.emit_signal('beforebgsoundsappend', self)
        s = self.sounds
        m = self.music
        b = BackgroundMusicGroups(self.world)

        b['forest0'] = 62, 65, 64, 63, 66, 68, 61, 60, 59
        b['forest0'].add(s['birds0'], m['To be happy'])
        b['threeways0'] = 25,
        b['threeways0'].add(s['birds1'])
        b['forest1'] = 88, 8, 5, 6, 18, 114, 17, 3, 2, 1, 11
        b['forest1'].add(s['birds0'], m['Fadeout'])
        b['forest2'] = 14, 16, 9, 10
        b['forest2'].add(m['hermano'])
        b['oddstone'] = 52, 56, 57, 53, 54, 55
        b['oddstone'].add(m['unicorns'])
        b['forest3'] = 0, 22, 13, 12, 72, 69, 71, 75, 76
        b['forest3'].add(m['Fjord'])
        b['forest4'] = 4, 23, 24, 7, 15
        b['forest4'].add(m['Our journey'])
        b['noforest'] = 21, 19, 20
        b['noforest'].add(s['birds0'])
        b['toruin'] = 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, \
            37, 48, 49, 50, 51, 58
        b['toruin'].add(s['birds0'], m['gallinas'])
        b['ruin'] = 38, 39, 46, 40, 47, 45, 44, 41, 42, 43
        b['ruin'].add(m['Pianos'])
        b['threeways1'] = 67,
        b['threeways1'].add(s['birds1'])
        b['tobeach0'] = 77, 78, 79, 81, 70, 73, 74, 87, 109, 108, 85, 82
        b['tobeach0'].add(s['birds0'], m['Noctavia'])
        b['tobeach1'] = 92, 89, 90, 91, 112, 94, 95, 80, 86, 107, \
            111, 106, 110, 113, 115, 93, 83
        b['tobeach1'].add(s['birds0'], m['Echoes of the Universe'])
        b['beach'] = 96, 100, 98, 99, 104, 101, 103, 105, 102, 97, 84, 116
        b['beach'].add(s['waves'], m['Winter princess'])

        self.bgmgroups = b
        self.sys.emit_signal('afterbgsoundsappend', self)

