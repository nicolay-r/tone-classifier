install:
	# Install all dependecies.
	sudo pip install -r requirements.txt

	# Downloading classifier libraries.
	mkdir -p models/classifiers
	cd models/classifiers/ && git clone https://github.com/cjlin1/libsvm
	make -C models/classifiers/libsvm
	make -C models/classifiers/libsvm/python
	cd models/classifiers/ && git clone https://github.com/cjlin1/liblinear
	make -C models/classifiers/liblinear
	make -C models/classifiers/liblinear/python
