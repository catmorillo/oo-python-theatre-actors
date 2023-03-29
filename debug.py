import ipdb
from lib import *

# Test your code below...
r1 =Role("Arnold")
r2 =Role("Little bear")
r3 =Role("Little Mermaid")
r4 =Role("Lionking")




a1 =Audition("Mark", "Atlanta, Georgia", r1, False)
a2 =Audition("Hector laVoe", "Los Angeles", r2, True)
a3 =Audition("Marie Sheep", "Orlando Florida", r4, True)
a4 =Audition("Tom Holland", "Orlando Florida", r4, True)


# the below line allows us to stop & try stuff!
ipdb.set_trace()