#SGX-PySpark with SCONE
/spark/bin/spark-submit --master local[1] encrypted-files/enc-pearson_correlation.py  input/enc-pe_opaque_a_105.txt input/enc-pe_opaque_b_105.txt &> output_pc.txt
# /spark/bin/spark-submit --master local[1] input/enc-pearson_correlation.py  input/enc-pe_opaque_a_105.txt input/enc-pe_opaque_b_105.txt &> output_pc.txt