from sklearn.neighbors import KNeighborsClassifier
from information_theory import information_distance

string2digits = lambda text,max_length:list(map( 
  ord,
  text + " "*(max(0,max_length-len(text))) 
))[:max_length]

digits2string = lambda digits:''.join(map( 
  chr,
  map(int,digits)
)).strip()


classifier = KNeighborsClassifier( 
  metric=lambda x,y:information_distance(
    x=digits2string(x),
    y=digits2string(y) 
  )
)


train = lambda X,y: classifier.fit( 
  X=list(map(
    lambda text:string2digits( 
      text=text,
      max_length=N 
    ),
    X
  )),
  y=y 
)

classify = lambda text: intents[ 
  classifier.predict(
    X=[ 
      string2digits(
        text=text,
        max_length=N 
      )
    ] 
  )[0]
]


