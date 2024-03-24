import os
import datetime
import pytz

print(os.listdir())


# comprehesion for list to append
L1 = [10, 20, 30, 40]
L2 = ["one", "two", "three", "four"]
L3 = [y for x in [L1, L2] for y in x]
print("Joined list:", L3)

# time zone with pytz
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)