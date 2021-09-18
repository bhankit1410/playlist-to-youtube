import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


def get_creds_for_spotify(path):
    edge_list = pd.read_csv(path)
    return edge_list

