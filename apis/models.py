import os
import yaml

# Load your Machine learning libraries here ex: Keras or Tensorflow ... etc
import tensorflow as tf


def init():
    # create global variables, so that you can load this variable inside api/module file
    global test_var
    global graph

    # Load models here into global variables
    test_var = "Load model here"

    graph = tf.get_default_graph()


def _get_cwd():
    return os.getcwd()
