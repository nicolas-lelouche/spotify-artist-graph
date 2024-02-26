import songs
import networkx as nx 
import matplotlib.pyplot as plt 
   

artist_songs, number_of_artist_appearance = songs.get_songs("test/data/artist-list.txt")

G = nx.Graph()

for song in artist_songs:
    if len(artist_songs[song]) > 1:
        G.add_edge(artist_songs[song][0], artist_songs[song][1])

d = nx.degree(G)


nx.draw(G, nodelist=d.keys(), node_size=[v * 100 for v in d.values()])
plt.show() 
