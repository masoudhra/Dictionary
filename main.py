# key : value
# key bayad unique bashad

week_days = {
    "sat": "Saturday",
    "sun": "Sunday",
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday"
}

print(week_days["sat"])
print(week_days["fri"])
# age bba get begim mitoonim agge eshteah vareddd kardan ye chize default gharar bedim
print(week_days.get("sun", "Not a valid key!"))
print(week_days.get("san", "Not a valid key!"))
