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
import time
import threading
import tkinter as tk


APPLICATION_TITLE = 'Coding Dojo Referee'
APPLICATION_WIDTH = 400
APPLICATION_HEIGHT = 200
APPLICATION_GEOMETRY = '%sx%s' % (APPLICATION_WIDTH, APPLICATION_HEIGHT)
APPLICATION_DEFAULT_FONT = (None, 26)
APPLICATION_SECONDARY_FONT = (None, 22)
INITIAL_TIME = '05:00'


class CountdownThread(threading.Thread):
    def __init__(self, master, duration_time, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master = master
        self.duration_time = time.strptime(duration_time, '%M:%S')
        self.remaining_sec = self.duration_time.tm_min * 60 + self.duration_time.tm_sec

        self.should_stop = False

    def run(self):
        print('Countdown started...')
        while self.remaining_sec >= 0 and not self.should_stop:
            remaining_min, remaining_sec = divmod(self.remaining_sec, 60)
            remaining = '{:02d}:{:02d}'.format(remaining_min, remaining_sec)
            self.master.update_remaining_time(remaining)
            time.sleep(1)
            self.remaining_sec -= 1
        print('Countdown finished...')
        return

    def stop(self):
        self.should_stop = True


class DojoReferee(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(APPLICATION_TITLE)
        self.geometry(APPLICATION_GEOMETRY)
        self.standard_font = APPLICATION_DEFAULT_FONT
        self.secondary_font = APPLICATION_SECONDARY_FONT
        self.resizable(False, False)

        self.setup_widgets()

        self.protocol('WM_DELETE_WINDOW', self.safe_exit)

    def setup_widgets(self):
        self.main_frame = tk.Frame(
            self,
            width=APPLICATION_WIDTH,
            height=APPLICATION_HEIGHT,
            bg='white',
            padx=10,
            pady=5,
        )
        self.start_button = tk.Button(
            self.main_frame,
            text='Start',
            bg='green',
            activebackground='lightgreen',
            fg='white',
            activeforeground='white',
            command=self.start,
            font=self.secondary_font,
        )

        self.stop_button = tk.Button(
            self.main_frame,
            text='Stop',
            bg='red',
            activebackground='red',
            fg='white',
            activeforeground='white',
            command=self.stop,
            font=self.secondary_font,
        )

        self.remaining_time = tk.StringVar(self.main_frame)
        self.remaining_time.set(INITIAL_TIME)
        self.countdown_label = tk.Label(
            self.main_frame,
            textvar=self.remaining_time,
            bg='white',
            fg='black',
            font=self.standard_font,
        )

        self.main_frame.pack(fill=tk.BOTH, expand=1)
        self.countdown_label.pack(fill=tk.X, pady=10)
        self.start_button.pack(fill=tk.X, pady=10)
        self.stop_button.pack(fill=tk.X, pady=10)

    def start(self):
        self.update_remaining_time(INITIAL_TIME)
        self.countdown = CountdownThread(self, INITIAL_TIME)
        self.countdown.start()

    def stop(self):
        if hasattr(self, 'countdown'):
            self.countdown.stop()
            self.update_remaining_time(INITIAL_TIME)

    def safe_exit(self):
        self.stop()
        self.after(200, self.destroy)

    def update_remaining_time(self, time):
        self.remaining_time.set(time)


def main():
    referee = DojoReferee()
    referee.mainloop()


if __name__ == '__main__':
    main()
