collections:
	cd data/collections/SentiRuEval-2015/ && ./init.sh
	cd data/collections/SentiRuEval-2016/ && ./init.sh
	cd tools/balancer/2015 && ./init.sh
balancedCollections:
	cd tools/balancer/2015/volume/3k && psql -U postgres -h localhost -W -d romipdata -f produce.sql
