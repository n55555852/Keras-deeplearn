# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 10:02:36 2019

@author: 10200994
"""
import tensorflow as tf 
from tensorflow.examples.tutorials.mnist import input_data

#数据加载，onehot转换。
mnist = input_data.read_data_sets("./",one_hot = True)
print ("Training data size:",mnist.train.num_examples)
print ("Validating data size:",mnist.validation.num_examples)
print ("Testing data size:",mnist.test.num_examples)
print ("Example training data len:",len(mnist.train.images[0]))
#print ("Example training data:",mnist.train.images[0])
print ("Example training data labels:",mnist.train.labels[0])


#设置mini_batch
batch_size = 100 
xs,ys = mnist.train.next_batch(batch_size)
print ("X shape:", xs.shape)
print ("Y shape:", ys.shape)



#
Learning_rate_base = 0.8
Learning_rate_decay= 0.99
regulirizationg_sate =0.0001
training_step = 30000
moving_average_decay = 0.99

def inference(input_tensor,avg_class,weights1,biases1,weights2,biases2):
    if avg_class ==None:
        layer1 = tf.nn.relu(tf.matmul(input_tensor, weights1)+biases1)
        layer2 = tg.nn.relu(tf.matmul(layer1, weights2)+biases2)
        

def train(mnist):
    x =tf.placeholder(tf.float32,[None, 28*28],name= 'x-input')
    y_ =tf.placeholder(tf.float32,[None, 10],name = 'y-output')
    
