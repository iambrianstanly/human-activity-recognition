

from zipfile import ZipFile

with ZipFile("data/mobile_health/mobile_health.zip", 'r') as z:
    z.extractall("data/mobile_health")