import uuid
import datetime
import random
import json
from azure.servicebus.control_client import ServiceBusService
# event hub sanajit creds

az_service_namespace = 'twittereventhubsg'
az_shared_access_key_name = ''
az_shared_access_key_value = ''


sbs = ServiceBusService(service_namespace=az_service_namespace, shared_access_key_name=az_shared_access_key_name, shared_access_key_value=az_shared_access_key_value)
devices = []
for x in range(0, 10):
    devices.append(str(uuid.uuid4()))

for y in range(0,100000):
    for dev in devices:
        reading = {'source': 'wind-turbine-geo-sensor', 
                   'id': 'tst_sensor', 
                   'timestamp': str(datetime.datetime.utcnow()),
                   'Export_Unit': random.random(),
                   'battery_current': random.randint(10, 20), 
                   'solar_KWH': random.randint(10, 20),
                   'Grid_VOLTAGE': random.randint(250, 800),
                   'turbine_RPM': random.randint(400, 500)}
        s = json.dumps(reading)
        sbs.send_event('twittereventhubsg', s)
    print (y)
    print (s)
