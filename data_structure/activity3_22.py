#get the country code
cntr_cd={'India' : '0091', 'Nepal' : '00977', 'Australia' : '0025', 'Canada' : '+1', 'Mexico' : '+52'}
#search dictionary for country code of india
print("Country code for India:")
print(cntr_cd.get('India', 'not found :/'))
print("Country code for Japan:")
print(cntr_cd.get('Japan', 'not found :/'))