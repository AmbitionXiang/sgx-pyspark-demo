#SGX-PySpark with SCONE
/spark/bin/spark-submit --master local[1] encrypted-files/enc-transitive_closure.py  input/enc-tc_opaque_2.txt &> output_tc.txt
# /spark/bin/spark-submit --master local[1] input/enc-transitive_closure.py input/enc-tc_opaque_2.txt &> output_tc_tmp.txt