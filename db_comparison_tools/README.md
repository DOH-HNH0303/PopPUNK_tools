# Tool instructions
## List of Tools 
### #<a name="compare_cluster_numbers.py"></a> compare_cluster_numbers.py

## [#compare_cluster_numbers.py]

This script takes in two POPPUNK DBs' cluster assigments to see if they differ. POPPUNK clusters need to be visualized to confirm the cluster pattern matches the data, but similar database builds may yield identical cluster assigments such that the scores in DB builds should carry more influence in picking the final organism DB build to use.

Example Use:
```
python compare_clusters.py --db1 Corynebacterium_diphtheriae_bac_D5_dec5 --db2 Corynebacterium_diphtheriae_bac_D4
```

Example Output:
```
NaN count per column:
Cluster     0
Cluster2    0
dtype: int64
0 cluster calls differ between DB cluster assignments
```
Example Interpretation:
Having NaN counts of 0 indicates that the sequences used in the DB builds are identical. The assigned cluster numbers are identical between the two given databases, just other metrics should be given more weight in the decision of which DB to use.