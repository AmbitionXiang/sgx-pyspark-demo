#SGX-PySpark with SCONE
/spark/bin/spark-submit --master local[1] encrypted-files/enc-dijkstra.py  input/enc-dij_opaque_1.txt &> output_dij.txt
# /spark/bin/spark-submit --master local[1] input/enc-dijkstra.py input/enc-dij_opaque_1.txt &> output_dij.txt