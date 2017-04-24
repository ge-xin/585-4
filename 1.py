import tensorflow as tf

a = tf.to_float(tf.constant([3,5,10]))
b = tf.to_float(tf.constant([4,12,24]))
c = tf.sqrt(tf.add(tf.square(a), tf.square(b)))

session = tf.InteractiveSession()
result = session.run(c)
print result