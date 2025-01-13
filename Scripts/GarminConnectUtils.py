import os
import pytz
import datetime
from garminconnect import Garmin
from StravaRunWidgetApp.models import RunningModel

class GarminUtils:
    def __init__(self):
        self.api = self.setUpGarmin()
        self.today_c_date = datetime.date.today().strftime("%Y-%m-%d")
        
    def setUpGarmin(self):
        api = Garmin(os.environ["MyEmailAddress"], os.environ["MyGarminPassword"])
        api.login()
        return api
    
    def getRunId(self):
        try:
            result = RunningModel.objects.filter(run_date=self.today_c_date)
            output = result.values_list('run_id', flat=True)
        except RunningModel.DoesNotExist:
            print("No record found for today's date.")
            activities_by_date = self.api.get_activities_by_date(self.today_c_date)
            for activity in activities_by_date:
                if activity['activityType']['typeKey'] == "running":
                    new_record = RunningModel.objects.create(run_date=self.today_c_date, run_id=activity['activityId'])
                    print(f"Record inserted with Run ID: {new_record.run_id} for Date: {new_record.run_date}")
                    output.append(activity['activityId'])
                else:
                    output = []
        print(f"Found {len(output)} ids")                  
        return output
                