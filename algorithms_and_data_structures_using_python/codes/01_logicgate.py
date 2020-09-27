class LogicGate:
    """逻辑门基类"""
    
    def __init__(self, name):
        self.name = name
        self.output = None
        
    def get_label(self):
        return self.name
        
    def get_output(self):
        """获取逻辑门的输出"""
        self.output = self.perform_logic_gate()
        return self.output
        


class BinaryGate(LogicGate):
    """两个逻辑输入的基类"""
    
    def __init__(self, name):
        super().__init__(name)
        self.pin_a = None
        self.pin_b = None
    
    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        elif self.pin_b == None:
            self.pin_b = source
        else:
            raise RuntimeError('No empty pins')
    
        
    def get_pin_a(self):
        if self.pin_a == None:            
            return int(input('Enter pin A input for gate' + self.get_label() + '-->'))
        else:
            return self.pin_a.get_from().get_output()
    
    def get_pin_b(self):
        if self.pin_b == None:     
            return int(input('Enter pin B input for gate' + self.get_label() + '-->'))   
        else:
            return self.pin_b.get_from().get_output()
            

class UnaryGate(LogicGate):
    """一个逻辑输入的基类"""    
    def __init__(self, name):
        super().__init__(name)
        self.pin = None
        
    def get_pin(self):
        return int(input('Enter pin input for gate' + self.get_label() + '-->'))
    

class AndGate(BinaryGate):
    def __init__(self, name):
        super().__init__(name)
    
    def perform_logic_gate(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        
        return 1 if a == 1 and b == 1 else 0



class OrGate(BinaryGate):
    def __init__(self, name):
        super().__init__(name)
    
    def perform_logic_gate(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        
        return 0 if a == 0 and b == 0 else 1
        
class NotGate(UnaryGate):
    def __init__(self, name):
        super().__init__(name)
    
    def perform_logic_gate(self):
        pin = self.get_pin()
        
        return 0 if pin == 1 else 1


class Connector:
    """
    连接类
    把from门连接到to门
    但是本类对象好像没什么用
    """
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate
        tgate.set_next_pin(self)
        
    def get_from(self):
        return self.from_gate
        
    def get_to(self):
        return self.to_gate


if __name__ == "__main__":
    g1 = AndGate('G1')
    g2 = OrGate('G2')
    g3 = NotGate('G3')
    # print(g1.get_output())
    # print(g2.get_output())
    # print(g3.get_output())
        
    c1 = Connector(g1, g2)
    c2 = Connector(g3,g2)
    print(g2.get_output())
    
