#!/usr/bin/env python
from distutils.core import setup
import os
ginfo_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                          'forestquest', 'generalinformation.py')
execfile(ginfo_file) # Gives us a version variable

setup(
    name='ForestQuest',
    version=version,
    author='Niels Serup',
    author_email='ns@metanohi.org',
    packages=['forestquest'],
    url='http://metanohi.org/projects/forestquest/',
    license='LICENSING.txt',
    description='An exiting RPG',
    long_description=open('README.txt').read(),
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: End Users/Desktop",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: GNU General Public License (GPL)",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python",
                 "Topic :: Games/Entertainment :: Role-Playing",
                 ],
    requires=['dililatum']
)
