#SGX-PySpark with SCONE
/spark/bin/spark-submit --master local[1] encrypted-files/enc-pagerank.py  input/enc-pr_opaque.txt 1 &> output_pr.txt
# /spark/bin/spark-submit --master local[1] input/enc-pagerank.py input/enc-pr_opaque.txt 1 &> output_pr.txt