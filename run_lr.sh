#SGX-PySpark with SCONE
/spark/bin/spark-submit --master local[1] encrypted-files/enc-logistic_regression.py  input/enc-lr_small.txt &> output_lr.txt
# /spark/bin/spark-submit --master local[1] input/enc-logistic_regression.py  input/enc-lr_small.txt &> output_lr.txt