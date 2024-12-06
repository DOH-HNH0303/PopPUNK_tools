import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.sparse import csr_matrix
import argparse
#import matplotlib.style as mplstyle
 
 
def get_options():

    parser = argparse.ArgumentParser(description='determine distance "centers" with kmeans', prog='extract_centers')
    # input options
    parser.add_argument('--prefix', help='prefix of distance tsv and poppunk database',
                                    required=True)


    return parser.parse_args()
args = get_options() 
prefix = args.prefix
distances = prefix + ".distances.tsv"

#mplstyle.use('fast')

distances = pd.read_csv(distances, sep='\t', index_col=0)
distances = distances.drop('Accessory', axis=1)

# Create a sparse matrix from your distance matrix
distances_sparse = csr_matrix(distances["Core"])

# Extract the upper triangle indices for a sparse matrix
row, col = distances_sparse.nonzero()
upper_tri_indices = (row < col)
distances_flat = distances_sparse[row[upper_tri_indices], col[upper_tri_indices]]
distances_flat = np.array(distances_flat)

# Reshape data for K-Means clustering
distances_reshaped = distances_flat.reshape(-1, 1)

# Perform K-Means clustering (2 clusters: within and between clusters)
distances_reshaped = np.asarray(distances_reshaped)
kmeans = KMeans(n_clusters=2, random_state=42, algorithm="elkan").fit(distances_reshaped)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Prepare kmeans centers for plotting
flat_list = []
for sublist in centers:
    for item in sublist:
        flat_list.append(item)
flat_list.sort() 
print(flat_list)
threshold = np.mean(centers)

counts, bin_edges = np.histogram(distances_flat, bins=100, density=True)
plt.hist(bin_edges[:-1], bin_edges, weights=counts, density=True, alpha=0.7)
plt.axvline(x=flat_list[0], color='r', linestyle='--', linewidth=2, label='min')
plt.axvline(x=flat_list[1], color='b', linestyle='--', linewidth=2, label='max')
plt.axvline(x=threshold, color='cyan', linestyle='--', linewidth=2, label='kmeans average')
# plt.axvline(x=0.0048838854, color='yellow', linestyle='--', linewidth=2, label='Max intra-cluster')
# plt.axvline(x=0.0045250654, color='orange', linestyle='--', linewidth=2, label='Min inter-cluster')
# plt.axvline(x=0.0047044754, color='green', linestyle='--', linewidth=2, label='Suggested core genome distance threshold')
# plt.axvline(x=0.003277, color='pink', linestyle='--', linewidth=2, label='combined')
plt.title("Pairwise Distance Distribution")
plt.xlabel("Core Genome Distance")
plt.ylabel("Density")
plt.legend()
title = prefix + "_distances.png"
plt.savefig(title)
##########################




with open('thresholds.txt', 'a') as file: # Write new content 
    file.write(prefix + "\t"+ str(flat_list[0]) + "\t" + str(flat_list[1]) + "\t" +str(threshold) + "\n")

print(f"Determined core genome distance threshold: {threshold}")


# Compute the inertia for a range of cluster numbers
distances_flat=np.asarray(distances_flat)
inertia = []
K = range(1, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(distances_flat.reshape(-1, 1))
    inertia.append(kmeans.inertia_)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(K, inertia, 'bx-')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal Number of Clusters')
title = prefix + "_elbow.png"
plt.savefig(title)