## Copyright 2005 Baiju M <baiju.m.mail@gmail.com>

## This file is part of BookMarker.

## BookMarker is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## BookMarker is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with BookMarker; if not, write to the Free Software
## Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""Web views."""

from boom.interfaces import IMark

class BookMarks:

    def __init__(self, context, request, base_url=''):
        self.context = context
        self.request = request
        self.base_url = base_url

    def listMarks(self):
        marks = []
        for name, child in self.context.items():
            if IMark.providedBy(child):
                info = {}
                info['url'] = child.url
                info['description'] = child.description
                marks.append(info)
        return marks
