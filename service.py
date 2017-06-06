import sys
from time import sleep
from resources.lib import control, packages, config

conf = config.config()
current_version = conf.getVersion()

packages_instance = packages.packages()
package_latest_version = packages_instance.getVersion()

if current_version == package_latest_version:
    sys.exit(1)

sleep(10)
if control.yesnoDialog(control.lang(30040).format(package_latest_version), "", "", control.addonInfo('name'), control.lang(30032), control.lang(30031)):
    control.execute('RunScript({0}, 0, action=update)'.format(control.addonInfo('id')))
else:
    pass
