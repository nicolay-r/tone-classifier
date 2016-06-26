#!/bin/bash
mkdir data
wget --output-document=data/positive.csv "https://www.dropbox.com/s/vqul3qh3d0o1qyo/positive.csv?dl=1"
wget --output-document=data/negative.csv "https://www.dropbox.com/s/944dfta73i6s95z/negative.csv?dl=1"
