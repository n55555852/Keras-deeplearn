# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:52:19 2019

@author: Administrator
"""

"""tensorflow_test
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
"""

"""获取数据"""
import numpy as np
path='./mnist.npz'
f = np.load(path)
x_train, y_train = f['x_train'], f['y_train']
x_test, y_test = f['x_test'], f['y_test']
f.close()




