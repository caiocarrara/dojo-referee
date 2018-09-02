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
import logging
import os
import subprocess

logger = logging.getLogger('dojo_referee')

APPLICATION_BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(APPLICATION_BASE_DIR, 'assets')
SOUND_EXEC = 'aplay'
SOUND_BEGIN_FILE = os.path.join(ASSETS_DIR, 'begin.wav')
SOUND_FINISH_FILE = os.path.join(ASSETS_DIR, 'finish.wav')


def play(audio_file_path):
    try:
        sound_playing = subprocess.Popen(
            [SOUND_EXEC, audio_file_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
        )
        return sound_playing
    except OSError as exc:
        logger.error('The following error happened trying to play finish sound', exc)


def play_begin():
    return play(SOUND_BEGIN_FILE)


def play_finish():
    return play(SOUND_FINISH_FILE)
