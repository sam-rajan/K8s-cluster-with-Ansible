from __future__ import (absolute_import, division, print_function)
from ansible.plugins.callback import CallbackBase

__metaclass__ = type

import sys
import os

DOCUMENTATION = '''
    callback: output
'''

class CallbackModule(CallbackBase):
    CALLBACK_VERSION = 2.0
    CALLBACK_NAME = 'output'
    CALLBACK_NEEDS_WHITELIST = False

    def __init__(self):
        super(CallbackModule, self).__init__()

    def v2_runner_on_failed(self, result, ignore_errors=False):
        host = result._host.get_name()
        self.runner_on_failed(host, result._result, ignore_errors)

    def v2_runner_on_ok(self, result):
        host = result._host.get_name()
        if 'print_id' in result._task.tags or self._display.verbosity > 1:
            print(result._result["ansible_facts"]["productId"])
            print(result._result["ansible_facts"]["macAddress"])
        self.runner_on_ok(host, result._result)
                                               