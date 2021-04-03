"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2020
"""


class Marketplace:
    id_prod = -1
    id_cart = -1
    ids_producers = []
    producers_products = []
    consumers_carts = [] 
    queue_size_per_producer = 0
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """

    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        # pass
        self.queue_size_per_producer = queue_size_per_producer

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        # fiecare producator va avea lista lui pt id-ul sau
        self.id_prod += 1
        self.ids_producers.append(id)
        self.producers_products.append([]) 
        return id

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        prod_queue = producers_products[int(producer_id)]

        if (len(prod_queue) < queue_size_per_producer):
            # don't let producer wait
            producers_products[int(producer_id)].append(product)
            return True
        return False
        # pass

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        # presupun ca fiecare consumer va avea ids-urile salvate
        self.id_cart += 1 
        self.consumers_carts.append([])
        return id_cart
        # pass

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        i = -1
        producer_found = -1 
        put_back = []
        for producer_products in self.producers_products:
            i += 1
            for producer_product in producer_products:
                if producer_product == product:
                    # l-am gasit
                    producer_found = i
                    # take_from = producer_products
                    break
            if producer_found != -1:
                break           

        if producer_found != -1:
            # si acum dam update la produsele ramase
            # already_took = 0 
            # for prod in take_from:
            #     if prod == product and already_took == 0:
            #         already_took = 1
            #     if prod == product and already_took == 1:
            #         put_back.append(prod)
            #     if prod != product:
            #         put_back.append(prod)
            # self.producers_products[producer_found].update(put_back)
            self.producers_products[producer_found].remove(product)

            # punem in cart-ul consumerului
            self.consumers_carts[cart_id].append(product)
            #returnam success
            return True
        else:
            return False
        # pass

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        self.consumers_carts(cart_id).remove(product)
        # cart = self.consumers_carts(cart_id)
        # renewed_cart = []
        # already_taken =0
        # for prod in cart:
        #     if prod == product and already_taken == 0:
        #         already_taken = 1
        #     if prod == product and already_taken == 1:
        #         renewed_cart.append(prod)
        #     if prod != product:
        #         renewed_cart.append(prod)
        # pass

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        final_cart = self.consumers_carts(cart_id)
        return final_cart
        # pass
