import tensorflow as tf
tf.config.list_physical_devices('GPU')
with tf.compat.v1.Session() as sess:
    hello = tf.constant('helloWorld')
    print(sess.run(hello))
