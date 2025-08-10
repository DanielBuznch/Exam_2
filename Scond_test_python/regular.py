from order import Order



class RegularOrder(Order):

    def __init__(self,name,delivery_address,list_item,customer,payment_type):
        super().__init__(name, delivery_address, list_item, customer, payment_type)


    def calculate_total_price(self):
        return super().calculate_total_price()
