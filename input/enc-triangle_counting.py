from __future__ import print_function

import sys, time
import os, pyaes, binascii
from operator import add

from pyspark.sql import SparkSession
import time

key = "Scontain-Germany"
aes = pyaes.AESModeOfOperationCTR(key)

def decrypt_m(e_mess):
    b_mess = binascii.unhexlify(e_mess)
    decrypted = aes.decrypt(b_mess)
    return decrypted

def parseEdge(line):
    parts = line.split(' ')
    l = max(int(parts[0]), int(parts[1]))
    s = min(int(parts[0]), int(parts[1]))
    return (s, l)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: triangle counting <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonTri")\
        .getOrCreate()

    print("begin to time")
    tic = time.time()
    graph = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])\
        .map(lambda x: decrypt_m(x))\
        .map(parseEdge)\
        .filter(lambda x: x[0] != x[1])\
        .distinct()\
        .cache()

    c = graph.join(graph)\
        .keyBy(lambda x: x[1])\
        .join(graph\
            .map(lambda x: (x, 1)))\
        .count()
    print("count: "+str(c))

    # need to time
    toc = time.time()
    print("triangle counting in %s seconds" % (toc - tic))

    spark.stop()
