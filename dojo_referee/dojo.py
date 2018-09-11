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
from datetime import datetime, timedelta
import logging

from dojo_referee.record import Record
from dojo_referee import settings

logger = logging.getLogger('dojo_referee')


class DojoParticipant:
    def __init__(self, email):
        self.email = email

    def __eq__(self, other):
        return self.email == other.email

    def __str__(self):
        return self.email


class DojoIteration:
    def __init__(self, pilot, copilot):
        self.pilot = pilot
        self.copilot = copilot
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(minutes=settings.ITERATION_TIME_MIN)


class Dojo:
    WAITING_START = 'WAITING_START'
    STARTED = 'STARTED'
    FINISHED = 'FINISHED'

    def __init__(self):
        self.status = Dojo.WAITING_START
        self.participants = list()
        self.iterations = list()
        self.dojo_record = Record(record_path=settings.DOJO_RECORD_PATH)
        self.participants_record = Record(record_path=settings.PARTICIPANTS_RECORD_PATH, timestamp=False)

    def start(self):
        self.status = Dojo.STARTED
        logger.info('message=dojo session started')
        self.dojo_record.write('message=dojo session started')

    def finish(self):
        self.status = Dojo.FINISHED
        logger.info('message=dojo session finished')
        self.dojo_record.write('message=dojo session finished')

    def add_participant(self, participant):
        if not self.is_participant(participant):
            self.participants.append(participant)
            self.participants_record.write(str(participant))

    def is_participant(self, participant):
        return participant in self.participants

    def add_iteration(self, pilot, copilot):
        self.add_participant(pilot)
        self.add_participant(copilot)

        self.iterations.append(
            DojoIteration(pilot, copilot)
        )
        logger.info('message=iteration started, pilot=%s, copilot=%s' % (pilot, copilot))
        self.dojo_record.write('message=iteration started, pilot=%s, copilot=%s' % (pilot, copilot))
