# balancer root folder
BALANCER_SCRIPTS=./tools/balancer
DATABASE=romipdata
DATABASE_USER=postgres

collections:
	# Initialize sentiRuEval collections
	cd data/collections/SentiRuEval-2015/ && ./init.sh
	cd data/collections/SentiRuEval-2016/ && ./init.sh
	# Initialize data for balancing
	cd ${BALANCER_SCRIPTS}/2015 && ./init.sh

balanced_sentiRuEval_2015_3k:
	cd ${BALANCER_SCRIPTS}/2015/volume/3k && psql -U $(DATABASE_USER) -h localhost -W -d $(DATABASE) -f produce.sql

balanced_sentiRuEval_2016_6k:
	cd ${BALANCER_SCRIPTS}/2016/volume/6k && psql -U $(DATABASE_USER) -h localhost -W -d $(DATABASE) -f produce_bank_2016.sql
	cd ${BALANCER_SCRIPTS}/2016/volume/6k && psql -U $(DATABASE_USER) -h localhost -W -d $(DATABASE) -f produce_ttk_2016.sql

balanced_sentiRuEval_2016_8k:
	cd ${BALANCER_SCRIPTS}/2016/volume/8k && psql -U $(DATABASE_USER) -h localhost -W -d $(DATABASE) -f produce_bank_2016.sql
	cd ${BALANCER_SCRIPTS}/2016/volume/8k && psql -U $(DATABASE_USER) -h localhost -W -d $(DATABASE) -f produce_ttk_2016.sql

install:
	# Install all dependecies.
	sudo apt-get install python-libxml2 python-psycopg2 python-pip postgresql g++ unzip
	sudo pip install setuptools
	sudo pip install pymystem3

	# Downloading classifier libraries.

	mkdir -p models/classifiers

	cd models/classifiers/ && git clone https://github.com/cjlin1/libsvm
	make -C models/classifiers/libsvm
	make -C models/classifiers/libsvm/python
	cd models/classifiers/ && git clone https://github.com/cjlin1/liblinear
	make -C models/classifiers/liblinear
	make -C models/classifiers/liblinear/python
