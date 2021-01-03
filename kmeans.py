import numpy as np
import cv2
import utils
from scipy.spatial.distance import cdist
def kmeans_init_centers(X,n_clusters):
    return X[np.random.choice(X.shape[0],n_clusters,replace=False)]
def kmeans_predict_labels(X,centers):
    D=cdist(X,centers)
    return np.argmin(D,axis=1)
def kmeans_update_center(X,labels,n_clusters):
    centers=np.zeros((n_clusters,X.shape[1]))
    for k in range(n_clusters):
        Xk=X[labels==k,:]
        centers[k,:]=np.mean(Xk,axis=0)
    return centers
def kmeans_has_convergred(centers,new_centers):
    return (set([tuple(a) for a in centers]) == 
      set([tuple(a) for a in new_centers]))
def kmeans(init_centers,init_labels,X,n_clusters):
    centers=init_centers
    labels=init_labels
    while True:
        labels=kmeans_predict_labels(X,centers)
        new_centers=kmeans_update_center(X,labels,n_clusters)
        if kmeans_has_convergred(centers,new_centers):
            break
        centers=new_centers
    return(centers,labels)
