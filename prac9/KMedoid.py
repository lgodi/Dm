#!/usr/bin/env python
# coding: utf-8

# In[12]:


from pyclustering.cluster.kmedoids import kmedoids
from pyclustering.cluster import cluster_visualizer
from pyclustering.utils import read_sample
from pyclustering.samples.definitions import FCPS_SAMPLES

# Load list of points for cluster analysis.
sample = read_sample(FCPS_SAMPLES.SAMPLE_TWO_DIAMONDS)

# Set random initial medoids.
initial_medoids = [100,200,300,500,600,700,750]

# Create instance of K-Medoids algorithm. 
kmedoids_instance = kmedoids(sample, initial_medoids)

# Run cluster analysis and obtain results.
kmedoids_instance.process()
clusters = kmedoids_instance.get_clusters()

# Show allocated clusters.
print(clusters)

# Display clusters.
visualizer = cluster_visualizer()
visualizer.append_clusters(clusters, sample)
visualizer.show()


# In[ ]:




