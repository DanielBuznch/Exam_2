from datetime import datetime
from abc import ABC, abstractmethod
from payment_type import PaymentType
from order_item import OrderItem
from enum import Enum
from order import Order
from customer_type import CustomerType
from gift import GiftAble

class Customer:
    id_counter = 1

    def __init__(self,first_name,last_name,email,delivery_address,customer_type:CustomerType,discount):
        self.customer_id = Customer.id_counter
        Customer.id_counter += 1

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.delivery_address = delivery_address
        self.customer_type = customer_type
        self.discount = discount
        self.favorite_items = []
        self.gift = None

    def auto_favorit_item(self,item):
        if not item in self.favorite_items:
            self.favorite_items.append(item)

    def add_favorit_item(self,item):
        if isinstance(item,OrderItem):
           self.favorite_items.append(item)

    def del_favorit_item(self,item):
        if isinstance(item,OrderItem):
           self.favorite_items.remove(item)


    def open_gift(self):
        if self.gift:
            self.gift.open_gift()
        else:
            print("No gift to open.")

    def give_gift(self, giftable: GiftAble):
        self.gift = giftable
        print("Congratulations! you got a new gift! Enjoy!")