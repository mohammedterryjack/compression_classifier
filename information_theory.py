from gzip import compress


K = lambda text: len(compress(text.encode('utf-8')))

information_distance = lambda x,y: K(x+y) - min(K(x), K(y))

rank = lambda target,candidates,top_n: sorted( 
  candidates,
  key=lambda candidate:information_distance(
    x=target,
    y=candidate
  ) 
)[:top_n]
