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
from datetime import datetime


class Record:
    def __init__(self, record_path, timestamp=True):
        self.record_file_path = record_path
        self.with_timestamp = timestamp

    def write(self, msg):
        if self.with_timestamp:
            now = datetime.now()
            record_msg = '%s - %s\n' % (now.isoformat(), msg)
        else:
            record_msg = '%s\n' % msg

        with open(self.record_file_path, 'a+') as record_file:
            record_file.write(record_msg)
