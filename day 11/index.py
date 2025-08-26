import re
from datetime import datetime
import pytz


print("=== Regex: Pattern Matching and Extraction ===")


text = "My phone number is 987-654-3210 and email is john.doe@example.com."


phone_pattern = r'\d{3}-\d{3}-\d{4}'
phone_match = re.search(phone_pattern, text)
if phone_match:
    print("Phone number found:", phone_match.group())


email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
email_match = re.search(email_pattern, text)
if email_match:
    print("Email found:", email_match.group())



print("\n=== datetime: Working with Dates and Times ===")
now = datetime.now()
print("Local current datetime:", now.strftime("%Y-%m-%d %H:%M:%S"))

date_str = "2025-08-26 15:30:00"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime object:", parsed_date)



print("\n=== pytz: Timezone Conversion ===")
utc = pytz.utc
local = pytz.timezone("Asia/Kolkata")
eastern = pytz.timezone("US/Eastern")

utc_now = datetime.now(utc)
print("UTC Time:", utc_now.strftime("%Y-%m-%d %H:%M:%S"))

local_time = utc_now.astimezone(local)
print("India Time (Asia/Kolkata):", local_time.strftime("%Y-%m-%d %H:%M:%S"))

eastern_time = utc_now.astimezone(eastern)
print("US Eastern Time:", eastern_time.strftime("%Y-%m-%d %H:%M:%S"))



print("\n=== Hands-on: Regex Validation & Date/Time Conversion ===")

def validate_phone(phone):
    return re.fullmatch(r'\d{3}-\d{3}-\d{4}', phone) is not None

def convert_timezone(date_str, from_tz_str, to_tz_str):
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)
    dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    dt = from_tz.localize(dt)
    return dt.astimezone(to_tz)

converted = convert_timezone("2025-08-26 10:00:00", "UTC", "Asia/Tokyo")
print("Converted time (UTC → Tokyo):", converted.strftime("%Y-%m-%d %H:%M:%S"))



print("\n=== Exercise: Email Validation & Multi-Timezone Clock ===")

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern, email) is not None

def show_current_times():
    zones = ["UTC", "Asia/Kolkata", "Europe/London", "US/Pacific"]
    now_utc = datetime.now(pytz.utc)
    for zone in zones:
        tz = pytz.timezone(zone)
        local_time = now_utc.astimezone(tz)
        print(f"{zone}: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")

emails = ["user@example.com", "not-an-email@", "test.user@domain.co"]
for email in emails:
    print(f"Email '{email}' is valid? {is_valid_email(email)}")

print("\nCurrent times in different timezones:")
show_current_times()
