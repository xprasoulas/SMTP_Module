import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
print(now)

date_of_birth = dt.datetime(year=2000,month=12,day=11, hour=22)
print(date_of_birth)