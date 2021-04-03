"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

from threading import Thread
import time


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, name=kwargs['name'])
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.kwargs = kwargs

    def run(self):

        for consumer_carts in self.carts:
            cart_id = self.marketplace.new_cart()

            for consumer_cart in consumer_carts:
                if consumer_cart['type'] == 'add':
                    quantity = consumer_cart['quantity']
                    while quantity != 0:
                        while not self.marketplace.add_to_cart(cart_id, consumer_cart['product']):
                            time.sleep(self.retry_wait_time)
                        quantity -= 1
                if consumer_cart['type'] == 'remove':
                    quantity = consumer_cart['quantity']
                    while quantity != 0:
                        self.marketplace.remove_from_cart(
                            cart_id, consumer_cart['product'])
                        quantity -= 1

            final_list = self.marketplace.place_order(cart_id)
            for product_bought in final_list:
                print("{} bought {}".format(
                    self.kwargs['name'], product_bought))
