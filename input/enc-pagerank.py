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

def computeContribs(urls, rank):
    """Calculates URL contributions to the rank of other URLs."""
    num_urls = len(urls)
    for url in urls:
        yield (url, rank / num_urls)


def parseNeighbors(urls):
    """Parses a urls pair string into urls pair."""
    parts = urls.split(' ')
    return (parts[0], parts[1])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: page rank <file> <iter>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("PythonPR")\
        .getOrCreate()

    print("begin to time")
    tic = time.time()
    
    # Loads in input file. It should be in format of:
    #     URL         neighbor URL
    #     URL         neighbor URL
    #     URL         neighbor URL
    #     ...
    lines = spark.read.text(sys.argv[1]).rdd.map(lambda r: r[0])\
        .map(lambda x: decrypt_m(x))

    # Loads all URLs from input file and initialize their neighbors.
    links = lines.map(parseNeighbors).distinct().groupByKey().cache()

    # Loads all URLs with other URL(s) link to from input file and initialize ranks of them to one.
    ranks = links.map(lambda url_neighbors: (url_neighbors[0], 1.0))

    # Calculates and updates URL ranks continuously using PageRank algorithm.
    for iteration in range(int(sys.argv[2])):
        # Calculates URL contributions to the rank of other URLs.
        contribs = links.join(ranks).flatMap(
            lambda url_urls_rank: computeContribs(url_urls_rank[1][0], url_urls_rank[1][1]))
        
        # Re-calculates URL ranks based on neighbor contributions.
        ranks = contribs.reduceByKey(add).mapValues(lambda rank: rank * 0.85 + 0.15)

    # Collects all URL ranks and dump them to console.
    res = ranks.collect()
    toc = time.time()
    print("page rank in %s seconds" % (toc - tic))
    (link, rank) = res[0]
    print("%s has rank: %s." % (link, rank))

    # need to time
    spark.stop()
