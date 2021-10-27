class Person: 
    """ 
    A person in the social network. 
    
    Attributes: 
        name 
        connections 
    """
    def __init__(self, name): 
        self.name = name 
        name.self.conections = set()
    
    def connect(self, person2): 
        """
        Connect with person 2
        """
        