import json
import os

class Setting:
    def __init__(self, filename):
        # settingfilepath = "../config/" + filename + ".json"
        print os.listdir('.')
        print "hello>>>>>>>>>>"
        settingfilepath = 'config/' + filename + ".json"
        self.setting = json.loads(open(settingfilepath, 'r').read())

    def get(self, settingname):
        return self.setting[settingname]
