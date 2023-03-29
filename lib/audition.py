
class Audition:
    def __init__(self, actor, location, role, hired =False):
        self.location = location
        self.hired = hired
        self.role = role
        self.actor = actor

#role` returns an instance of role associated with this audition.
    @property 
    def role(self): 
        return [ r for r in self.audition] 
    
#actor` returns an instance of actor associated with this audition.
    @property 
    def actor(self):
        return [ a for a in self.audition] 

#call_back()` will change the the hired attribute to `True`. 

    @property
    def call_back(self):
        self.hired == True
        

        