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

class SimplePerspective(PlaceChanger):
    def init(self, power, minus=0):
        self.power = power
        self.minus = minus

    def __call__(self, pos):
        a = self.world.size[1] / self.power
        a = (pos[1] - self.world.size[1] + a) / float(a) - self.minus
        return a

class XZigZagWithYPerspective(PlaceChanger):
    def init(self, ziglen, ypower, yminus=0):
        self.ziglen = ziglen
        self.y = SimplePerspective(self.world, ypower, yminus)

    def __call__(self, pos):
        z = self.ziglen
        z2 = z / 2
        x = float(pos[0])
        t = x % z
        if t > z2:
            t = -t + z2
        t = t / 5
        s = t / z2
        r = (s + self.y(pos)) / 2
        return r

class PlaceDetails:
    def c(self, clas, *args):
        return clas(self.world, *args)

    def g(self, num, clas, *args):
        self.world.places[num].char_size = self.c(clas, *args)

    def p(self, num, power, minus=0):
        self.g(num, SimplePerspective, power, minus)

    def improve_places(self):
        self.sys.emit_signal('beforeplacesimprove', self)
        self.p(0, 1.36)
        self.p(1, 1.36)
        self.p(2, 1.36)
        self.p(3, 1.36, .2)
        self.p(4, 1.36, .15)
        self.p(5, 1.2)
        self.p(6, 1.36)
        self.p(7, 1.36, .13)
        self.p(8, 1.36)
        self.p(9, 1.26, .26)
        self.p(10, 1.4)
        self.p(11, 1.06, -.2)
        self.p(12, 1.46, .12)
        self.p(13, 1.36)
        self.p(14, 1.36)
        self.p(15, 1.36)
        self.p(16, 1.36)
        self.p(17, 1.43, .17)
        self.p(18, 1.46)
        self.p(19, 1.4, .25)
        self.p(20, 1.5, .3)
        self.p(21, 1.46, .27)
        self.p(22, 1.42, .07)
        self.p(23, 1.46)
        self.p(24, 1.42, .2)
        self.p(25, 1.5)
        self.p(26, 1.44)
        self.p(27, 1.36)
        self.p(28, 1.42, .05)
        self.p(29, 1.36)
        self.p(30, 1.52, .05)
        self.p(31, 1.46, .05)
        self.p(32, 1.36)
        self.p(33, 1.28)
        self.p(34, 1.4)
        self.p(35, 1.46)
        self.p(36, 1.36)
        self.p(37, 1.36)
        self.p(38, 1.03, .04)
        self.p(39, 1.6, -.75)
        self.p(40, 1.1, .4)
        self.p(41, 1.26)
        self.p(42, 1.1, -.15)
        self.p(43, 1.16)
        self.p(44, 1.06, .3)
        self.p(45, 1.25)
        self.p(46, 1.005, .3)
        self.p(47, 1.1, .2)
        self.p(48, 1.2, .15)
        self.p(49, 1.65, .1)
        self.p(50, 1.63, .2)
        self.p(51, 1.65, .05)
        self.p(52, 1.66, .05)
        self.g(53, XZigZagWithYPerspective, 100, 1.03, .05)
        self.g(54, XZigZagWithYPerspective, 100, 1.03, .05)
        self.g(55, XZigZagWithYPerspective, 100, 1.03, .05)
        self.g(56, XZigZagWithYPerspective, 100, 1.03, .05)
        self.g(57, XZigZagWithYPerspective, 100, 1.03, .05)
        self.p(58, 1.36, .2)
        self.p(59, 1.46)
        self.p(60, 1.6)
        self.p(61, 1.16)
        self.p(62, 1.36)
        self.p(63, 1.36)
        self.p(64, 1.56)
        self.p(65, 1.5)
        self.p(66, 1.36)
        self.p(67, 1.46)
        self.p(68, 1.41, .15)
        self.p(69, 1.65)
        self.p(70, 1.5, .15)
        self.p(71, 1.36)
        self.p(72, 1.43)
        self.p(73, 1.46)
        self.p(74, 1.36)
        self.p(75, 1.36, .15)
        self.p(76, 1.42, .32)
        self.p(77, 1.47, .07)
        self.p(78, 1.49, .07)
        self.p(79, 1.36, .2)
        self.p(80, 1.36, .2)
        self.p(81, 1.36, .35)
        self.p(82, 1.36)
        self.p(83, 1.56, .15)
        self.p(84, 1.4, .1)
        self.p(85, 1.4, .25)
        self.p(86, 1.36)
        self.p(87, 1.36)
        self.p(88, 1.43)
        self.p(89, 1.2)
        self.p(90, 1.16, .2)
        self.p(91, 1.25)
        self.p(92, 1.3, .15)
        self.p(93, 1.53)
        self.p(94, 1.36, .3)
        self.p(95, 1.36)
        self.p(96, .7, .5)
        self.p(97, 1.2, .3)
        self.p(98, 1.1)
        self.p(99, 1.36)
        self.p(100, 1.0)
        self.p(101, 1.55, .15)
        self.p(102, 1.36)
        self.p(103, 1.56)
        self.p(104, 1.5)
        self.p(105, 1.36, .14)
        self.p(106, 1.44)
        self.p(107, 1.26)
        self.p(108, 1.46)
        self.p(109, 1.36)
        self.p(110, 1.16)
        self.p(111, 1.5)
        self.p(112, 1.35, .15)
        self.p(113, 1.5, -.05)
        self.p(114, 1.1, -.1)
        self.p(115, 1.4, .2)
        self.p(116, 1.1, .1)
        self.sys.emit_signal('afterplacesimprove', self)
