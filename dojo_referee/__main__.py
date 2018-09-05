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
import logging.config
import tkinter as tk

from dojo_referee.dojo import Dojo
from dojo_referee.sound import play_begin, play_finish
from dojo_referee.workers import BlinkingLabelThread, CountdownThread
from dojo_referee import settings

logger = logging.getLogger('dojo_referee')


class DojoReferee(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(settings.APPLICATION_TITLE)
        self.geometry(settings.APPLICATION_GEOMETRY)
        self.resizable(False, False)
        self.clock_str = '{:02}:00'.format(settings.ITERATION_TIME_MIN)

        self.setup_widgets()
        self.protocol('WM_DELETE_WINDOW', self.safe_exit)

        self.dojo = Dojo()
        self.iteration_active = False

    def setup_widgets(self):
        self.main_frame = tk.Frame(
            self,
            width=settings.APPLICATION_WIDTH,
            height=settings.APPLICATION_HEIGHT,
            bg='white',
            padx=10,
            pady=5,
        )
        self.btn_toggle_session = tk.Button(
            self.main_frame,
            text='Start Dojo Session',
            bg='royalblue',
            activebackground='dodgerblue',
            fg='white',
            activeforeground='white',
            command=self.toggle_session,
            font=settings.APPLICATION_DEFAULT_FONT,
        )

        self.btn_toggle_iteration = tk.Button(
            self.main_frame,
            text='Start',
            bg='forestgreen',
            activebackground='green3',
            fg='white',
            activeforeground='white',
            command=self.toggle_iteration,
            font=settings.APPLICATION_SECONDARY_FONT,
            state=tk.DISABLED,
        )

        self.remaining_time = tk.StringVar(self.main_frame)
        self.remaining_time.set(self.clock_str)
        self.countdown_label = tk.Label(
            self.main_frame,
            textvar=self.remaining_time,
            bg='white',
            fg='black',
            font=settings.APPLICATION_HERO_FONT,
        )

        self.main_frame.pack(fill=tk.BOTH, expand=1)
        self.btn_toggle_session.pack(fill=tk.X, pady=10)
        self.countdown_label.pack(fill=tk.X, pady=10)
        self.btn_toggle_iteration.pack(fill=tk.BOTH, pady=10)

    def toggle_session(self):
        if self.dojo.status == Dojo.STARTED:
            self.dojo.finish()
            self.btn_toggle_iteration['state'] = tk.DISABLED
            self.btn_toggle_session['text'] = 'Start Dojo Session'
        else:
            self.dojo.start()
            self.btn_toggle_iteration['state'] = tk.NORMAL
            self.btn_toggle_session['text'] = 'Finish Dojo Session'

    def toggle_iteration(self):
        if self.iteration_active:
            self.finish_iteration()
        else:
            self.start_iteration()
        self.iteration_active = not self.iteration_active

    def start_iteration(self):
        self.update_remaining_time(self.clock_str)
        self.btn_toggle_iteration['text'] = 'Resume'
        self.btn_toggle_iteration['bg'] = 'orange3'
        self.btn_toggle_iteration['activebackground'] = 'orange2'
        self.countdown = CountdownThread(self, self.clock_str)
        self.countdown.start()
        self.sound_playing = play_begin()

    def finish_iteration(self):
        self.btn_toggle_iteration['text'] = 'Start'
        self.btn_toggle_iteration['bg'] = 'forestgreen'
        self.btn_toggle_iteration['activebackground'] = 'green3'
        self.countdown_label['fg'] = 'black'
        if hasattr(self, 'countdown'):
            self.countdown.stop()
            self.update_remaining_time(self.clock_str)
        if hasattr(self, 'blinking'):
            self.blinking.stop()
        if hasattr(self, 'sound_playing'):
            self.sound_playing.terminate()

    def safe_exit(self):
        self.finish_iteration()
        self.after(200, self.destroy)

    def update_remaining_time(self, time):
        if time == '00:00':
            self.btn_toggle_iteration['text'] = 'Stop'
            self.countdown_label['fg'] = 'red'
            self.blinking = BlinkingLabelThread(self, time)
            self.blinking.start()
            self.sound_playing = play_finish()
        self.remaining_time.set(time)


def main():
    logging.config.fileConfig(settings.LOG_CONFIG_FILE)
    referee = DojoReferee()
    referee.mainloop()


if __name__ == '__main__':
    main()
