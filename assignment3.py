# 1. Create 100 random json files with the following information:
#     a. id: random string or hex
#     b. start and end datetime: between 01-06-2021 and 01-07-2021 inclusive
#     c. club_id: 10 constant value
#     d. activity_id: among 1,2,3 {1:'bball', 2:'fball', 3:'sball'}
#     c. staff_member_id: among 100, 200, 300
#     d. participants: contains at least 2 members but not more than 5 with the following info
#         i. member_id
#         ii. has_paid
#         iii. present
#     e. guest: contains at least 2 members but not more than 5 with the following info
#         i. first_name
#         ii. last_name
#         iii. has_paid
#         iv. present
#     f. deleted: either true or false

#     Example of sample json:
#     {
#         "id": "8a060891ff4641669abdca3863c2d54b",
#         "datetime_start": "2021-06-01T00:00:00+02:00",
#         "datetime_end": "2021-06-26T10:19:19+02:00",
#         "club_id": 10,
#         "activity_id": 3,
#         "staff_member_id": 100,
#         "participants": [
#             {
#                 "memeber_id": 44,
#                 "has_paid": false,
#                 "present": false
#             },
#             {
#                 "memeber_id": 37,
#                 "has_paid": true,
#                 "present": false
#             }
#         ],
#         "guests": [ 
#             {
#                 "first_name": "ewsyo",
#                 "last_name": "xevkm",
#                 "email": "ewsyo.xevkm@gmail.com",
#                 "has_paid": false,
#                 "present": true
#             },
#             {
#                 "first_name": "xblci",
#                 "last_name": "bvtpa",
#                 "email": "xblci.bvtpa@gmail.com",
#                 "has_paid": true,
#                 "present": false
#             }
#         ],
#         "deleted": false
#     }

# 2. Convert the generated json files to csvs:
#     i. events.csv:
#         a.activity_name,
#         b. number_of_participants,
#         c. number_of_guests

#     ii. participants.csv:
#         a. create primary_key,
#         b. present,
#         c. memeber_id,
#         d. has_paid,
#         e. event_id

from datetime import date, timedelta
import random
import uuid
import string
import json
import csv

def generate_obj(n):
    obj = {}
    obj['id'] = str(uuid.uuid4())
    obj['club_id'] = 10
    obj['activity_id'] = random.randint(1, 3)
    obj['staff_member_id'] = random.randint(100, 300)
    obj['participants'] = generate_participants(random.randint(2, 5))
    obj['guests'] = generate_guest(random.randint(2, 5))        
    obj['deleted'] = True if n % 2 == 0 else False
    obj['datetime_start'] = (date(2021, 6, 1) + timedelta(days=random.randint(0, 15))).strftime("%m/%d/%Y, %H:%M:%S")
    obj['datetime_end'] = (date(2021, 7, 1) - timedelta(days=random.randint(0, 15))).strftime("%m/%d/%Y, %H:%M:%S")
    return obj

def generate_participants(number):
    participants = []
    for n in range(number):
        obj = {}
        obj['member_id'] = n
        obj['has_paid'] = True if n % 2 == 0 else False
        obj['present'] = True if n % 3 == 0 else False
        participants.append(obj)
    return participants

def generate_guest(number):
    guests = []
    for n in range(number):
        obj = {}
        obj['first_name'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        obj['last_name'] = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        obj['email'] = f"{obj['first_name']}@gmail.com"
        obj['has_paid'] = True if n % 2 == 0 else False
        obj['present'] = True if n % 3 == 0 else False
        guests.append(obj)
    return guests

count = 100

for x in range(count):
    obj = generate_obj(x)
    obj_json = json.dumps(obj, indent=2)
    file_name = f"file_{x}"
    with open(f"{file_name}.json", 'w') as ouput:
        ouput.write(obj_json)
    with open(f"{file_name}.json") as input:
        data = json.load(input)
    event_data = [data['activity_id'], len(data['participants']), len(data['guests'])]
    with open(f"events_{x}.csv", 'w') as e :
        wr = csv.writer(e)
        wr.writerow(event_data)
    pcdata = []
    for pc in data['participants']:
        pcdata.append([pc['member_id'], pc['has_paid'], pc['present']])
    with open(f"participants_{x}.csv", 'w') as p :
        wr = csv.writer(p)
        wr.writerows(pcdata)