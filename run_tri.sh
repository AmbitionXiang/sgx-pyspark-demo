#SGX-PySpark with SCONE
/spark/bin/spark-submit --master local[1] encrypted-files/enc-triangle_counting.py  input/enc-tc_opaque_7.txt &> output_tri.txt
# /spark/bin/spark-submit --master local[1] input/enc-triangle_counting.py input/enc-tc_opaque_7.txt &> output_tri.txt