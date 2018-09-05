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

from dojo_referee import settings


class DojoRecord:
    def __init__(self, dojo_record_path=settings.DOJO_RECORD_PATH):
        self.record_file_path = dojo_record_path

    def write(self, msg):
        now = datetime.now()
        with open(self.record_file_path, 'a+') as record_file:
            record_msg = '%s - %s\n' % (now.isoformat(), msg)
            record_file.write(record_msg)
