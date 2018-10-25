import requests

donors = ['Imelda','Roxy','Nidia','Bennett','Roxanne','Kirstin','Markus','Jona','Kylie','Austin','Tiana','Demetra',
          'Edris','Jacquetta','Ilana','Eugene','Brunilda','Andreas','Milton','Thora', 'Anirudh']

for donor in donors:
    req = requests.get("http://127.0.0.1:5000/get_donated_refugees?user="+donor)
    print(req.text)
