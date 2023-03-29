from .audition import Audition

class Actor:
    def __init__(self, name):
        self.name = name

 #auditions` returns a list of auditions this actor attended.
    @property
    def auditions(self):
        return [a.audition for a in self.auditions]

 #roles` returns a list of roles the actor auditioned for.
    @property
    def roles(self):
        return [r.role for r in self.auditions]       

#characters` returns a list of strings with all the different 
#character names this actor auditioned for.
    @property
    def characters(self):
    actor_names= []
    for actor in actors:
        if actor.auditioned:
            actor_names.append.(actor.name)

#paychecks` returns a list of strings with all the 
#different character names that this actor has been **hired** for.
    @property
    def paychecks
    character_names =[]
    for actor in actors
        if actor.hired:
            character_name.append(actor.name)
            