#!/bin/bash
curl -o DemoData.tar.gz https://weilab.math.msu.edu/Downloads/TopFit/Data.tar.gz
tar -zxvf Data.tar.gz
rsync -a Data/* .
rm -r Data/ 
