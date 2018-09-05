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
import pytest

from dojo_referee.dojo import Dojo, DojoIteration, DojoParticipant
from dojo_referee import settings


@pytest.fixture
def dojo_participant():
    return DojoParticipant('test@test.com')


@pytest.fixture
def pilot():
    return DojoParticipant('pilot@dojo-referee.com')


@pytest.fixture
def copilot():
    return DojoParticipant('copilot@test.com')


@pytest.fixture
def dojo_iteration(pilot, copilot):
    return DojoIteration(pilot, copilot)


@pytest.fixture
def dojo():
    return Dojo()


def test_dojo_participant_eq(dojo_participant):
    other_participant = DojoParticipant(dojo_participant.email)
    assert dojo_participant == other_participant


def test_dojo_participant_str(dojo_participant):
    assert dojo_participant.email == str(dojo_participant)


def dojo_iteration_end_time(dojo_iteration):
    start_time = dojo_iteration.start_time
    end_time = dojo_iteration.end_time
    assert end_time.minutes - start_time.minutes == settings.ITERATION_TIME_MIN


def test_dojo_waiting_start(dojo):
    assert dojo.status == Dojo.WAITING_START


def test_dojo_start(dojo):
    dojo.start()
    assert dojo.status == Dojo.STARTED


def test_dojo_finish(dojo):
    dojo.finish()
    assert dojo.status == Dojo.FINISHED


def test_dojo_add_participant(dojo):
    dojo_participant = DojoParticipant('test@test.com')
    dojo.add_participant(dojo_participant)
    assert dojo.participants[0] == dojo_participant


def test_dojo_add_participant_do_not_duplicate(dojo):
    dojo_participant = DojoParticipant('test@test.com')
    dojo.add_participant(dojo_participant)
    dojo.add_participant(dojo_participant)
    assert len(dojo.participants) == 1


def test_dojo_is_participant(dojo):
    dojo_participant = DojoParticipant('test@test.com')
    dojo.add_participant(dojo_participant)
    assert dojo.is_participant(dojo_participant)


def test_dojo_add_iteration(dojo, pilot, copilot):
    dojo.add_iteration(pilot, copilot)
    assert len(dojo.iterations) == 1
    iteration = dojo.iterations[0]
    assert iteration.pilot == pilot
    assert iteration.copilot == copilot


def test_dojo_add_iteration_adds_participants(dojo, pilot, copilot):
    dojo.add_iteration(pilot, copilot)
    assert pilot in dojo.participants
    assert copilot in dojo.participants


def test_dojo_add_iteration_dont_duplicates_participants(dojo, pilot, copilot):
    dojo.add_participant(pilot)
    dojo.add_participant(copilot)
    dojo.add_iteration(pilot, copilot)
    assert len(dojo.participants) == 2
