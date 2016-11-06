from sklearn.neighbors import NearestNeighbors
import scipy.spatial.distance as scidi 

class LOF:
    def __init__(self, train_data, k):
        self.train_data = train_data
        self.nearest_neighbors = NearestNeighbors(n_neighbors = k, metric = "euclidean")
        
        # Fit the training data to find neighbors:
        self.nearest_neighbors.fit(train_data)
    
    # Calculates the KNN of a row "a"
    def __neighbors(self, a):
        return_value = self.nearest_neighbors.kneighbors([a])
        return(return_value)
    
    # Calculates the number of neighbors of a row "a"
    def __number_of_neighbors(self, a):
        return(len(self.__neighbors(a)[0][0]))
    
    # Calculates the k-distance of a row "a"
    def __k_distance(self, a):
        distances, indexes = self.__neighbors(a)
        return(max(distances[0]))
    
    # Calculates the reachability distance between rows "a" and "b"
    def __reachability_distance(self, a, b):
        return(max([self.__k_distance(b), scidi.euclidean(a, b)]))
    
    # Calculates the local reachability function for row "a"
    def __lrd(self, a):
        neighbors_distances, neighbors_indexes = self.__neighbors(a)
        
        numerator = sum([self.__reachability_distance(a, b) for b in self.train_data.iloc[neighbors_indexes[0],:].values])
        denominator =  self.__number_of_neighbors(a)
        
        return(1/(numerator/denominator))
    
    # Calculates the LOF for a row "a"
    def __lof(self, a):
        neighbors_distances, neighbors_indexes = self.__neighbors(a)
        
        numerator = sum([(self.__lrd(b) / self.__lrd(a)) for b in self.train_data.iloc[neighbors_indexes[0], :].values])
        denominator = self.__number_of_neighbors(a)
        
        return(numerator/denominator)
    
    # Predicts the LOFs for the rows in "test_data"
    def predict(self, test_data):
        lofs = [self.__lof(x) for _, x in test_data.iterrows()]
        return(lofs)