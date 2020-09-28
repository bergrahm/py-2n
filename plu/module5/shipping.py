class ShippingContainer:

    next_serial = 1337

    #@staticmethod
    #def _get_next_serial():
    #    result = ShippingContainer.next_serial
    #    ShippingContainer.next_serial += 1
    #    return result
    
    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32


    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if (value > 5):
            raise ValueError("too hot")
        self._celsius = value
    

    def __init__(self, owner_code, contents, celsius):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._get_next_serial()