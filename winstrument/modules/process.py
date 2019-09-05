# Copyright (C) 2019  NCC Group
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import frida
import win32con
from winstrument.base_module import BaseInstrumentation
class Process(BaseInstrumentation):
    modulename = "process"
    def __init__(self,*args, **kwargs):
        self._output = []
        super().__init__(*args,**kwargs)

    def on_message(self, message, data):
        if message["type"] == "error":
            print(f"Error: {message}")
            return
        elif message["type"] == "send":
            payload = message["payload"]
            self.write_message(payload)