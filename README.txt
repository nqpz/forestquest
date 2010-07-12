===========
ForestQuest
===========

Welcome to the realm of::
    ┏━┛┏━┃┏━┃┏━┛┏━┛━┏┛┏━┃ ┃ ┃┏━┛┏━┛━┏┛
    ┏━┛┃ ┃┏┏┛┏━┛━━┃ ┃ ┃ ┃ ┃ ┃┏━┛━━┃ ┃ 
    ┛  ━━┛┛ ┛━━┛━━┛ ┛ ━━━┛━━┛━━┛━━┛ ┛ 

ForestQuest is an RPG. You have a role. You play a game. And in this
case, "a game" is this game.

ForestQuest consists of two parts: Code and data. Code is written in
Python and released under the GNU GPLv3+, while data is generally
available under the terms of the Creative Commons BY-SA 3.0+
license. More about this in the file LICENSING.txt includeded with
this distribution.

ForestQuest uses the Dililatum library to run itself. At
http://metanohi.org/projects/dililatum/ you can get a copy of
Dililatum. This version of ForestQuest works with Dililatum v0.1 (and
maybe even future versions).

You do not have to install ForestQuest to run it, but it is possible.
To install ForestQuest, write this in a terminal::

    $ ./setup.py install

To run it, make sure Dililatum is installed, and then run this in a
terminal::

    $ dililatum path/to/forestquest

If you chose to install ForestQuest, there's an even quicker way::

    $ dililatum forestquest

A graphical Dililatum frontend might be added in a future Dililatum
release. Read more about this on the Dililatum website.

New versions of ForestQuest can be downloaded from
http://metanohi.org/projects/forestquest/. Because of ForestQuest's
status as a game, there's really not much to document. The size of the
code of ForestQuest is limited, and it's not like it creates a whole
new set of APIs. Dililatum is documented.

ForestQuest is a work in progress, and part of its purpose is to be
a way to more easily develop Dililatum (which, like ForestQuest, is not
exactly complete right now). Developers are very welcome.

The current version of ForestQuest is v0.1. The original author is
Niels Serup <ns@metanohi.org>.
