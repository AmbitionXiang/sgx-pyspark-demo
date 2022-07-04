#SGX-PySpark with SCONE
/spark/bin/spark-submit --master local[1] encrypted-files/enc-matrix_multiplication.py  input/enc-mm_opaque_a_100.txt input/enc-mm_opaque_b_100.txt &> output_mm.txt
# /spark/bin/spark-submit --master local[1] input/enc-matrix_multiplication.py  input/enc-mm_opaque_a_100.txt input/enc-mm_opaque_b_100.txt &> output_mm.txt