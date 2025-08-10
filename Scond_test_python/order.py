from datetime import datetime
from abc import ABC, abstractmethod
from payment_type import PaymentType
from customer import Customer
from order_item import OrderItem



class Order(ABC):
    id_counter = 1

    @abstractmethod
    def __init__(self,name,delivery_address,list_item:list[OrderItem],customer:Customer,payment_type:PaymentType):
        self.order_id = Order.id_counter
        Order.id_counter += 1

        self.name = name
        self.delivery_address =delivery_address
        self.list_item = item_ids = [item.item_id for item in list_item]
        if len(item_ids) != len(set(item_ids)):
            raise ValueError("Duplicate item_id found in order items!")
        self.customer = customer
        self.total_price = self.calculate_total_price()
        self.payment_type = payment_type
        self.order_date = datetime.now()


        for item in list_item:
            self.customer.auto_favorit_item(item)


    @abstractmethod
    def calculate_total_price(self):
        return sum(item.price for item in self.list_item)

