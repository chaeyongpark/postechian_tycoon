all:
	./manage.py loaddata initial_data/initial_item.json
	./manage.py loaddata initial_data/initial_combination_1.json
	./manage.py loaddata initial_data/initial_combination_2.json
	./manage.py loaddata initial_data/codeToItem_1_to_240.json
	./manage.py loaddata initial_data/codeToItem_241_to_480.json
	./manage.py loaddata initial_data/codeToItem_481_to_690.json
	./manage.py loaddata initial_data/codeToItem_691_to_900.json
	./manage.py loaddata initial_data/codeToItem_901_to_1070.json
	./manage.py loaddata initial_data/mission.json
	./manage.py loaddata initial_data/ice_breaking.json
	./manage.py loaddata initial_data/initial_etc.json
	./manage.py loaddata initial_data/mission.json

codeToItem:
	./manage.py loaddata initial_data/codeToItem_1_to_240.json
	./manage.py loaddata initial_data/codeToItem_241_to_480.json
	./manage.py loaddata initial_data/codeToItem_481_to_690.json
	./manage.py loaddata initial_data/codeToItem_691_to_900.json
	./manage.py loaddata initial_data/codeToItem_901_to_1070.json

item:
	./manage.py loaddata initial_data/initial_item.json

ice_breaking:
	./manage.py loaddata initial_data/ice_breaking.json
