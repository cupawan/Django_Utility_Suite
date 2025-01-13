import os
import pytz
import datetime
import requests
from StravaRunWidgetApp.models import RunningModel
from garminconnect import (Garmin, GarminConnectAuthenticationError, GarminConnectConnectionError, GarminConnectTooManyRequestsError)

class GarminUtils:
    def __init__(self):
        self.today_c_date = datetime.date.today().strftime("%Y-%m-%d")
        
    def setUpGarmin(self):
        api = Garmin(os.environ["MyEmailAddress"], os.environ["MyGarminPassword"])
        api.login()
        return api
    
    def getRunId(self):
        output = []
        try:
            result = RunningModel.objects.filter(run_date=self.today_c_date)
            output = result.values_list('run_id', flat=True)
        except RunningModel.DoesNotExist:
            print("No record found for today's date.")
            try:
                self.api = self.setUpGarmin()
                activities_by_date = self.api.get_activities_by_date(self.today_c_date)
                for activity in activities_by_date:
                    if activity['activityType']['typeKey'] == "running":
                        new_record = RunningModel.objects.create(run_date=self.today_c_date, run_id=activity['activityId'])
                        print(f"Record inserted with Run ID: {new_record.run_id} for Date: {new_record.run_date}")
                        output.append(activity['activityId'])
            except (GarminConnectConnectionError, GarminConnectAuthenticationError, GarminConnectTooManyRequestsError, requests.exceptions.HTTPError) as err:
                print("Error occurred during Garmin Connect communication: %s", err)
        print(f"Found {len(output)} ids")                  
        return output
                