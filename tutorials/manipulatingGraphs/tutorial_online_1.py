
############
#tutorial-1#
############
#%%
from networkx.classes.function import edges, nodes
import pandas as pd

#read data remotely - making sure click on the raw 
df= pd.read_csv('https://raw.githubusercontent.com/stefanoacode/net-analysis-smm638/master/data/musae_ENGB_edges.csv')

df.info()

# there is a space in the original file "to"
df.rename({'#from':'source','to ':'target'}, inplace=True)

#alternative df.rename(dict(zip(df.columns)))
#alternative: df.rename(dict(zip([""]'#':'source','to':'target'}, inplace=True)
# %%
df.info
#%%
import networkx as nx

#only apply when you have file stored locally: g = nx.read_edgelist()

g = nx.from_pandas_edgelist(df, source='#from', target='to')


# %%

# manipulate data on pandas

# and read the data 


#%%

# write data in the locale file directly in nx 
nx.write_graphml(g, path='my_data.graphml')

# write data to pandas dataframe
df.to_csv('my_data.csv')

# %%
# another way to get rid of rename colunm
my_data='https://raw.githubusercontent.com/stefanoacode/net-analysis-smm638/master/data/musae_ENGB_edges.csv'

# check the quality of lable 
df = pd.read_csv(my_data, header=0, names=['v0','v1'])
df.head()
# %%
import numpy as np

# add new ingridients 
df.loc[:, 'weight'] = np.random.poisson(lam=10, size=len(df))
df.head()
# %%
g = nx.from_pandas_edgelist(df.source='v0', target='v1', edge_attr='weight')
# %%
# create nunpy data 
import networkx as nx
a_np = nx.to_numpy_matrix(g)
out_file = os.path.join(wd, 'data', 'from_numpy.npy')
# %%
nodes = g.nodes()

edges = g.edges()

nodes
g = nx.DiGraph()


# %%
import numpy as np

x = np.random.poisson(lam=3, size=1)
x
# %%
