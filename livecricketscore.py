#pip install pycricbuzz
from pycricbuzz import Cricbuzz
a=Cricbuzz()
match=a.matches()
for x in match:
    print(x)
    if(x['mchstate'] != 'nextlive'):
        print(a.livescore(x['id']))
        print(a.commentary(x['id']))
        print(a.scorecard(x['id']))
