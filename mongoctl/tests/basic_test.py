# The MIT License

# Copyright (c) 2012 ObjectLabs Corporation

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


import unittest
import commands
import json
import inspect
import os
import shutil

from mongoctl.tests.test_base import MongoctlTestBase

class BasicMongoctlTest(MongoctlTestBase):

    def test_start_stop_server(self):
        self.assert_server_stopped("simple_test_server")
        self.assert_start_server("simple_test_server")
        self.assert_server_running("simple_test_server")
        self.assert_stop_server("simple_test_server")
        self.assert_server_stopped("simple_test_server")

    ###########################################################################
    def test_restart_server(self):
        self.assert_server_stopped("simple_test_server")
        self.assert_restart_server("simple_test_server")
        self.assert_restart_server("simple_test_server")
        self.assert_restart_server("simple_test_server")
        self.assert_server_running("simple_test_server")
        self.assert_stop_server("simple_test_server")
        self.assert_server_stopped("simple_test_server")

    ###########################################################################
    def get_my_test_servers(self):
        return ["simple_test_server"]
# booty
if __name__ == '__main__':
    unittest.main()

