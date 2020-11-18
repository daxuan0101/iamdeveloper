import tensorflow as tf
print(tf.__version__)

hello = tf.constant('Hello World')
sess = tf.compat.v1.Session()
print(sess.run(hello))
