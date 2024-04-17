import songs
import networkx as nx 
import matplotlib.pyplot as plt 
   

artist_songs, number_of_artist_appearance = songs.get_songs("test/data/artist-list.txt")

G = nx.Graph()

print(number_of_artist_appearance.keys())

for song in artist_songs:
    number_of_artists_featured = len(artist_songs[song])
    for i in range(number_of_artists_featured - 1):
        for j in range(i + 1, number_of_artists_featured):
            if G.has_edge(artist_songs[song][i], artist_songs[song][j]):
                G[artist_songs[song][i]][artist_songs[song][j]]['weight'] += 1
            else:
                G.add_edge(artist_songs[song][i], artist_songs[song][j], weight = 1)



edges = G.edges()
weights = [G[u][v]['weight'] for u,v in edges]

nx.draw_networkx(G, nodelist = number_of_artist_appearance.keys(), node_size = [v * 100 for v in number_of_artist_appearance.values()],
                    width = weights) 
plt.show() 
