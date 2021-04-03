"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2020
"""


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    producer_id = -1
    producer_ids = []
    producers_products = []

    cart_id = -1
    cart_products_ids = []
    consumers_carts = []

    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_producer = queue_size_per_producer

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        self.producer_id += 1
        self.producer_ids.append(self.producer_id)
        self.producers_products.append([])
        return self.producer_id

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        if len(self.producers_products[int(producer_id)]) > self.queue_size_per_producer:
            return False

        self.producers_products[int(producer_id)].append(product)
        return True

    def new_cart(self):
        """ [[carts] [carts]]
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        self.cart_id += 1
        self.consumers_carts.append([])
        self.cart_products_ids.append([])
        return self.cart_id

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        # cautam pe la producatori
        found = 0
        producer_no = -1
        for producer_products in self.producers_products:
            producer_no += 1
            product_no = -1
            for producer_product in producer_products:
                product_no += 1
                if producer_product[0] == product:
                    found = 1
                    producer_product_found = producer_product
                    break
            if found == 1:
                break
        # stergem produsul de la producatori& adaugam la cart
        if found == 1:
            self.producers_products[producer_no].remove(producer_product_found)
            new_added = (producer_no, producer_product_found)
            self.consumers_carts[cart_id].append(product)
            self.cart_products_ids[cart_id].append(new_added)
            return True

        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        self.consumers_carts[cart_id].remove(product)
        # adaug inapoi la producer-ul respectiv
        for all_products in self.cart_products_ids[cart_id]:
            product_detailed = all_products[1]
            if all_products[1] == product_detailed[0]:
                # am gasit produsul de returnat
                producer_author = all_products[0]
                self.producers_products[producer_author].append(
                    product_detailed)
                break

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        return self.consumers_carts[cart_id]
