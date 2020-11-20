import requests
nomor = input("Masukan Nomor HP : ")
password = input("Masukan Password : ")
print('Sedang Login >>>')
headers = {'accept':'text/htmlapplication/xhtml+xml,application/xml;q=0.9,image/Androidp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3','origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','content-type':'application/json','User-Agent':'AppleAndroidKit/537.36 Mozilla'}
r = requests.post('https://id-api.spooncast.net/signin/?version=2',headers=headers,json={"sns_type":"phone","sns_id":nomor,"password":password})
respon_data = r.json()
for i in respon_data['results']:
	taguser = i['id']
	tokennyaa = i['token']
	tagged = i['tag']
	print('')
	print(i['nickname'])
	print(tagged)
	print('')
	idbaru = input('Masukan ID yang baru : ')
	inputidbaru = {'username':idbaru}
	paramex = {'cv':'heimdallr'}
	headers = {'User-Agent':'Mozilla/5.0','Authorization':'Token '+tokennyaa,'origin':'https://www.spooncast.net','referer':'https://www.spooncast.net/','content-type':'application/json'}
	jrii = requests.post('https://id-api.spooncast.net/users/username/',headers=headers,params=paramex,json=inputidbaru)
	if jrii.status_code==200:
		print('Success ! ID Telah di ganti ke ' + str(idbaru))
		print('Silahkan Cek ID Spoon kamu..')
	else:
		print('Gagal')