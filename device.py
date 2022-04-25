#class_module_inheritance



class Router:
    def __init__ (self,model,swversion,ip_add):
        self.model=model
        self.swversion=swversion
        self.ip_add=ip_add

    def getdesc(self):
        desc=(f'Router Model         :{self.model}\n'\
              f'Software Version     :{self.swversion}\n'\
              f'Management Address   :{self.ip_add}')
        return desc 

class Switch(Router):
    def getdesc(self):
        desc=(f'Switch Model          :{self.model}\n'\
             f'Software Version       :{self.swversion}\n'\
             f'Management Address     :{self.ip_add}')
        return desc

