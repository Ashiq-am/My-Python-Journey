from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)












from datetime import datetime

now = datetime.now().time() # time object

print("now =", now)
print("type(now) =", type(now))