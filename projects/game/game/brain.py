import numpy as np


class Neuron(object):

    def __init__(self):
        self.theta = []
        self.inputs = []
        self.x = []
    def give_input(self,array):
        """takes data like: array([[0,0,1,1],[0,1,0,1]])"""
        self.inputs = array
        #print array.shape
        self.x = np.concatenate((np.ones((1,array.shape[1])),array),axis=0)
    def set_theta(self,matrix):
        self.theta = matrix
    def get_output(self):
        g = lambda x: 1/(1+np.exp(-x))
        return g(np.dot(self.theta,self.x))
    def grad_desc(self,y,alpha = 1,descend = 10):
        """assumes y in the form myAnd=array([0,0,0,1])"""            
        for i in range(descend):
            self.theta = self.theta- alpha*((1/(1+exp(-self.theta.np.dot(self.x)))-y)*self.x).sum(axis=1)
        return self.theta
    
class Network(object):
    def __init__(self,shape,matrix=[]):
        """shape should be like (2,2,1), where the first 2 is the input dimension, 
        the second 2 is the hidden layer, and the final 1 is the output.
        
        Notice then that (2,1) would only be a single neuron, with two inputs:
        i.e., it'd be great for calculating things like OR, or AND
        
        Matrix, is an optional theta array (i.e., something like array([[[1,1,-1]]]) for initialization.
        Otherwise, an array with normal random numbers will be generated.
        """
        self.shape = shape
        if len(matrix) == 0:
            theta = []     
            for i in range(len(self.shape)-1):
                input_size = self.shape[i]+1
                theta.append([np.random.randn(input_size).tolist() for j in range(self.shape[i+1])])
            self.theta = np.asarray(theta)
            #print self.theta
            #print self.theta.shape
        else:    
            self.theta = np.asarray(matrix)
            #print self.theta.shape
        self.neurons = [0 for i in range(len(self.shape)-1)]
        for i in range(len(self.shape)-1):
            self.neurons[i] = [0 for j in range(self.shape[i+1])]
            for j in range(self.shape[i+1]):
                self.neurons[i][j] = Neuron()
                self.neurons[i][j].set_theta(np.array(self.theta[i][j]))
    
    def give_input(self,matrix):
        """takes data like: array([[0,0,1,1],[0,1,0,1]])"""
        self.matrix = matrix
        self.output_matrix = [matrix]
        for i in range(len(self.shape)-1):
            out = []
            for j in range(self.shape[i+1]):
                self.neurons[i][j].give_input(matrix)
                out.append([self.neurons[i][j].get_output()])
            matrix = np.concatenate(out,axis =0)
            self.output_matrix.append(matrix)

    def get_output(self):
        self.give_input(self.matrix)
        return self.neurons[len(self.shape)-2][0].get_output()
    
    def get_theta(self):
        """this isn't working right now..."""
        theta_temp = []
        for i in range(len(self.shape)-1):
            for j in range(self.shape[i+1]):
                theta_temp.append(self.neurons[i][j].theta)
        return np.asarray(theta_temp)            
    
    def regress(self,y,alpha =1, epochs =1):
        """assumes y in the form myAnd=array([0,0,0,1])
           alpha is the learning rate
           epochs is the amount of times it's going to recur
           notice, for now, that we can't have data like array([[0,0,0,1][1,1,0,0]])
           but this will be added soon
        """ 
        for epoch in range(epochs):
            #It doesn't look like it, but this is forward propagation

            out_error =  self.get_output()-y
                                            
            if epoch%500 == 0:
                print 'For epoch %d error: %s' %(epoch, out_error)    
                
            #as the professor said, we do it over each input seperately
            for inputs in range(len(self.output_matrix[0][0])):
    
                #first we go get delta
                delta = [None for i in range(len(self.shape)-1)]
                delta[len(self.shape)-2] = [np.array([out_error[inputs]])]
                for i in reversed(range(len(self.shape)-2)):
                    delta[i] = [None for j in range(self.shape[i+1])] 
                    for j in range(self.shape[i+1]):
                        for k in range(self.shape[i+2]):
                            activation =  self.output_matrix[i+1][j][inputs]
                            delta[i][j] =  activation*(1-activation)*delta[i+1][k]*self.neurons[i+1][k].theta[j+1]
    
                #and now we update our weights
                for i in range(len(self.shape)-1):
                    for j in range(self.shape[i+1]):
                        self.neurons[i][j].theta -= alpha*delta[i][j]*\
                        np.concatenate((np.array([1]),self.output_matrix[i][:,inputs]),axis=1)
 
