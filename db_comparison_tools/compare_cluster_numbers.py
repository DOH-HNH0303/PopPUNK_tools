import pandas as pd
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument("--db1", dest="db1",  default="db1", help="/path/to/input/poppunkdb1")
parser.add_argument("--db2", dest="db2",  default="db2", help="/path/to/input/poppunkdb2")
args = parser.parse_args()

db1 = args.db1 + "/" + args.db1 + "_clusters.csv"
clusters1 = pd.read_csv(db1)
clusters1.set_index('Taxon', inplace=True)

db2 = args.db2 + "/" + args.db2 + "_clusters.csv"
clusters2 = pd.read_csv(db2)
clusters2.set_index('Taxon', inplace=True)
clusters2.rename(columns={'Cluster': 'Cluster2'}, inplace=True)

# Join cluster tables of db1 and db2 on taxon (seq name) as index
result = clusters1.join(clusters2)

# Detect if any seqs got dropped between DBs
column_nan_count = result.isnull().sum()
print("NaN count per column:")
print(column_nan_count)

# Return list of cluster assignment of seqs that are not identical between DBs
identity = result.loc[~(result['Cluster'] == result['Cluster2'])]
print(f"{len(identity)} cluster calls differ between DB cluster assignments")