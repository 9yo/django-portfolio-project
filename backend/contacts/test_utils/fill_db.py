import requests

headers = {
    'Content-Type': 'application/json'
}

response = requests.post('http://localhost:8000/register/', headers=headers, json={
    'email': 'test@gmail.com',
    'username': 'test',
    'password': 'test'
})

# print(response.json())
# with open('h.html', 'w') as f:
#     f.write(results)

response = requests.post('http://localhost:8000/auth/login/', json={
    'username': 'test',
    'password': 'test'
})

access_token = response.json().get('access')

print('Access token -', access_token)

names = ['VanessaWest', 'Emily Foster', 'Todd Meyer', 'Sarah Wilson', 'Emily Norman', 'Ryan Beck III', 'Angela Ramsey', 'Robert Smith', 'Andrea Gibson', 'Alexis Davis', 'Allen Smith', 'Kristy Underwood', 'Ricardo Smith', 'Anthony Small', 'Sabrina Anderson', 'Emily Davis', 'Bryan King', 'Perry Arnold', 'Matthew Martin', 'Kevin Murphy', 'Tabitha Miller', 'Tom Williams', 'Claudia Clark', 'Martha Hawkins', 'Jeremy Hughes', 'Michelle Randolph', 'Karen Mcdonald', 'Cheryl Rivera', 'Laura Hanson', 'Lisa Silva', 'Melvin Jones', 'Lori Petersen', 'Steven Brown', 'Jason Conley', 'Pamela Stephens', 'Tracey Meyer', 'Kenneth Williams', 'Michelle Monroe', 'Melanie Sanchez', 'Brian Brown', 'Kimberly Sanchez', 'Leslie Mullins', 'Christopher Leonard', 'Rebecca Chase', 'Joshua Walker', 'Anthony Gray', 'Jason Rodgers', 'Kelsey Miller', 'Tracy Kelly', 'Charles Goodman']
numbers = ['+1 582-262-3777','+1 582-262-8009','+1 417-754-9346','+1 309-814-3863','+1 582-465-5606','+1 609-939-4510','+1 202-328-8639','+1 210-824-8477','+1 505-665-3278','+1 201-528-8399','+1 582-333-9169','+1 201-399-4641','+1 202-449-9627','+1 582-302-2820','+1 302-584-7728','+1 352-825-8624','+1 209-376-6698','+1 385-937-0050','+1 239-698-2185','+1 202-212-9086','+1 215-617-2942','+1 513-682-3089','+1 201-258-1316','+1 331-943-6509', '+1 229-582-2488', '+1 223-281-1773','+1 505-830-1126','+1 582-300-2938','+1 336-991-6970','+1 582-201-7875','+1 505-633-5031','+1 505-504-6716','+1 228-533-4708','+1 582-302-8727','+1 505-644-3201','+1 582-322-1365','+1 254-703-1554','+1 505-644-5096','+1 582-322-6161','+1 325-258-9608','+1 582-201-7784','+1 508-628-3453','+1 208-521-8622','+1 582-222-8849','+1 361-818-2047','+1 364-504-7383','+1 707-583-4879','+1 606-472-1087','+1 323-551-1775','+1 582-322-0687']
comments = ['job', 'family', 'friends', 'medical assistant', '']


headers['Authorization'] = f'Bearer {access_token}'
# for i in range(len(names) - 1):
#     response = requests.post('http://localhost:8000/contacts/', headers=headers, json={
#         'name': names[i],
#         'number': numbers[i],
#         'comment': comments[i//10]
#     })
#     print('created id -', response.json().get('id'))

for i in range(len(comments) - 2):
    response = requests.post('http://localhost:8000/contact_books/', headers=headers, json={
        'name': comments[i],
        'desc': '',
        'contacts': []
    })
    print('created id -', response.json().get('id'))
