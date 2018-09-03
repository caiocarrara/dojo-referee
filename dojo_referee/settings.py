# Copyright (C) 2018 Caio Carrara <eu@caiocarrara.com.br>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# LICENSE for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import os


APPLICATION_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(APPLICATION_BASE_DIR, 'assets')

APPLICATION_TITLE = 'Coding Dojo Referee'
APPLICATION_WIDTH = 400
APPLICATION_HEIGHT = 200
APPLICATION_GEOMETRY = '%sx%s' % (APPLICATION_WIDTH, APPLICATION_HEIGHT)
APPLICATION_DEFAULT_FONT = (None, 16)
APPLICATION_HERO_FONT = (None, 30, 'bold')
APPLICATION_SECONDARY_FONT = (None, 18)

LOG_CONFIG_FILE = os.path.join(APPLICATION_BASE_DIR, 'logging.conf')

INITIAL_TIME = '05:00'

SOUND_EXEC = 'aplay'
SOUND_BEGIN_FILE = os.path.join(ASSETS_DIR, 'begin.wav')
SOUND_FINISH_FILE = os.path.join(ASSETS_DIR, 'finish.wav')
