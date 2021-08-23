import requests
from operator import itemgetter


def calc_age(uid):
    token = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
    version = 5.71
    fields = 'bdate'
    payload_user = {'access_token': token, 'v': version, 'user_ids': uid, 'fields': fields}
    response_user = requests.get('https://api.vk.com/method/users.get', params=payload_user)
    data = response_user.json()
    id = data['response'][0]['id']
    payload_friends = {'access_token': token, 'v': version, 'user_id': id, 'fields': fields}
    response_friends = requests.get('https://api.vk.com/method/friends.get', params=payload_friends)
    data_bdate = response_friends.json()
    list_bdate = data_bdate['response']['items']

    bdate = []
    for i in list_bdate:
        user_data = {2021 - int(v[-4:]) for k, v in i.items() if k == 'bdate' and v.count('.') == 2}
        bdate.extend(user_data)

    age_list = []
    age_test_list = []
    for i in bdate:
        if i not in age_test_list:
            age_test_list.append(i)
            age_list.append((i, bdate.count(i)))
    age_list = sorted(age_list, key = itemgetter(0))
    age_list = sorted(age_list,key = itemgetter(1),reverse=True)
    return age_list

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
