# from datetime import datetime, timedelta
# datetime.today().strftime('%Y/%m/%d')-timedelta(days = 1)

//strftime is use to format days and change it to string
from datetime import datetime, timedelta
# today=datetime.today() //today 
for i in range(0,3):
  print((datetime.today()-timedelta(days = i)).strftime('%Y/%m/%d'))
