class TechStack:
    def __init__(self, tech_names):
        self._tech_names=tech_names

    @property
    def tech_names(self):
        return self._tech_names
    
    @tech_names.setter
    def tech_names(self, value):
        self._tech_names=value

    @tech_names.deleter
    def tech_names(self):
        del self._tech_names

tech_stack=TechStack('python,jave,sql')
print(tech_stack.tech_names)


tech_stack.tech_names='python,sql'
print(tech_stack.tech_names)

del tech_stack.tech_names
print(tech_stack.__dict__)

"""
python,jave,sql
python,sql
{}
"""