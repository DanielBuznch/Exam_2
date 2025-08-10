from order import Order
from customer import Customer
from order_item import OrderItem
from payment_type import PaymentType
from typing import override


class VipOrder(Order):
    def __init__(self, name, delivery_address, list_item, customer,payment_type):
        super().__init__( name, delivery_address, list_item, customer, payment_type)


        if not self.customer.is_vip:
            raise ValueError(f"{self.customer.name} Your account is not on the list of VIP please check and then try again ")
        self.total_price = self.calculate_total_price()


    @override
    def calculate_total_price(self):
       bace_price = super().calculate_total_price()
       discount = Customer.discount if Customer.discount <= 1 else 0
       discount_price =  bace_price * (1-discount)
       return discount_price