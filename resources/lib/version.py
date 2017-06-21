# -*- coding: utf-8 -*-

"""
    TheDabur Add-on
    Copyright (C) 2017 TheDabur
"""

from time import sleep, time
from resources.lib import control, packages, config


class version:
    def __init__(self):
        self.conf = config.config()
        self.conf_json = self.conf.get()
        self.packages = []

    def check(self):
        return bool(self.get_current_version() != self.get_latest_version())

    def is_time_to_check(self):
        return bool(self.conf.getUpdateNextCheck() < int(time()))

    def get_current_version(self):
        return self.conf.getVersion()

    def get_latest_version(self):
        self.packages = packages.packages()
        return self.packages.getVersion()

    def check_and_update(self):
        if self.check():
            if control.yesnoDialog(control.lang(30040).format(self.get_latest_version()), "", "",
                                   control.addonInfo('name'),
                                   control.lang(30032), control.lang(30031)):

                if "skip_version" in self.conf_json:
                    del self.conf_json['skip_version']

                self.conf_json['updated_at'] = int(time())
                self.conf.save()
                control.execute('RunScript({0}, 0, action=update)'.format(control.addonInfo('id')))

                pass
            else:
                pass
        else:
            control.dialog.ok(control.addonInfo('name'), control.lang(30041).format(self.get_current_version()))
