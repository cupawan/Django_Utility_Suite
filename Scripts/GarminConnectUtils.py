import os
import pytz
import datetime
from garminconnect import Garmin
from garminconnect import Garmin

class GarminUtils:
    def __init__(self):
        self.api = self.setUpGarmin()
        self.today_c_date = datetime.date.today().strftime("%Y-%m-%d")
        
    def setUpGarmin(self):
        api = Garmin(os.environ["MyEmailAddress"], os.environ["MyGarminPassword"])
        api.login()
        return api
    
    def getRunId(self):
        output = []
        activities_by_date = self.api.get_activities_by_date(self.today_c_date)
        for activity in activities_by_date:
            if activity['activityType']['typeKey'] == "running":
                output.append(activity['activityId'])
        return output
                