def add_time(start, duration, days = False):
  [start_time , meridiem] = start.split(" ")
  [start_hour , sM] = start_time.split(":")
  [duration_hour , duration_minute] = duration.split(":")
  
  week_index = {"monday" : 0 ,"tuesday": 1 , "wednesday" : 2, "thursday" : 3, "friday" : 4 , "saturday" : 5 , "sunday" : 6}
  
  week_day =  ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]
  meridiem_dict = {"AM" : "PM" , "PM" : "AM"}

  total_minutes = int(sM) + int(duration_minute)
  total_hours = int(start_hour) + int(duration_hour)

  if total_minutes > 60:
    total_minutes = total_minutes - 60
    total_hours += 1

  if total_minutes < 10:
    total_minutes = f"{total_minutes}".zfill(2)
  
  total_days = int(duration_hour) // 24

  if (meridiem == "PM"):
    if total_hours >= 12:
      total_days += 1
  
  result_minutes = total_minutes
  meridiem_change = int(total_hours / 12)
  result_hour = total_hours % 12
  result_hour = 12 if result_hour == 0 else result_hour
  
  meridiem = meridiem_dict[meridiem] if (meridiem_change % 2) == 1 else meridiem
  
  new_time = str(result_hour) + ":" + str(result_minutes) +" "+ meridiem
  
  if days:
    days = days.lower()
    index = round((week_index[days] + total_days) % 7)
    result_days = week_day[index]
    new_time += ", " + result_days

  if total_days == 1:
    new_time += " (next day)"
  elif total_days >= 2:
    new_time += " ("+str(total_days) + " days later)"
  
  return new_time
