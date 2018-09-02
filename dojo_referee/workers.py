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
import time
import threading

logger = logging.getLogger('dojo_referee')


class CountdownThread(threading.Thread):
    def __init__(self, master, duration, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = master
        self.duration = time.strptime(duration, '%M:%S')
        self.remaining_sec = self.duration.tm_min * 60 + self.duration.tm_sec

        self.should_stop = False

    def run(self):
        logger.info('Countdown started...')
        while self.remaining_sec >= 0 and not self.should_stop:
            remaining_min, remaining_sec = divmod(self.remaining_sec, 60)
            remaining = '{:02d}:{:02d}'.format(remaining_min, remaining_sec)
            self.master.update_remaining_time(remaining)
            time.sleep(1)
            self.remaining_sec -= 1
        logger.info('Countdown finished...')
        return

    def stop(self):
        self.should_stop = True


class BlinkingLabelThread(threading.Thread):
    def __init__(self, master, text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = master
        self.text = text
        self.should_stop = False

    def run(self):
        while True and not self.should_stop:
            current_value = self.master.remaining_time.get()
            if current_value:
                self.master.remaining_time.set('')
            else:
                self.master.remaining_time.set(self.text)
            time.sleep(0.5)
        return

    def stop(self):
        self.should_stop = True
