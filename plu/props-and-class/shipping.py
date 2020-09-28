class ShippingContainer:
    import iso6346 as iso6346
    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        import iso6346 as iso6346
        return iso6346.create(owner_code=owner_code, serial=str(serial).zfill(6))

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=None)

    @classmethod
    def _get_next_serial2(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result
    
    @property
    def test(self):
        return self._test

    @test.setter
    def test(self, value): 
        self._p = value

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))

    @staticmethod
    def _get_next_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self._test = 2
        self.bic = ShippingContainer._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._get_next_serial2())

if __name__ == "__main__":
    

    s6 = ShippingContainer.create_empty("001337")
    print(s6.bic, s6.contents, s6.owner_code)
    #s1 = ShippingContainer("lol", "lewl")
    #print(s1.bic, s1.contents, s1.owner_code)

    ##s2 = ShippingContainer("lonk", "bonk")
    #print(s2.bic, s2.contents, s2.owner_code)

    #s3 = ShippingContainer.create_empty("Dear-boy")
    #print(s3.bic, s3.contents, s3.owner_code)

    #s4 = ShippingContainer.create_with_items("FEW213", ["sweat", "blood", "tears"])
    #print(s4.bic, s4.contents, s4.owner_code)