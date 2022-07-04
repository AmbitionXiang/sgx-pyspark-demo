#SGX-PySpark with SCONE
/spark/bin/spark-submit --master local[1] encrypted-files/enc-kmeans.py  input/enc-km_opaque_50000_5.txt 10 0.3 &> output_km.txt
# /spark/bin/spark-submit --master local[1] input/enc-kmeans.py  input/enc-km_opaque_50000_5.txt 10 0.3 &> output_km.txt