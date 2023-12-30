from information_theory import information_distance

rank = lambda target,candidates,top_n: sorted( 
  candidates,
  key=lambda candidate:information_distance(
    x=target,
    y=candidate
  ) 
)[:top_n]
