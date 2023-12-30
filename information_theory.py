from gzip import compress


K = lambda text: len(compress(text.encode('utf-8')))

information_distance = lambda x,y: K(x+y) - min(K(x), K(y))
