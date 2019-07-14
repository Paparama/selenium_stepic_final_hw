class ProductPageMessages(object):
    @staticmethod
    def eng_add(book_name):
        return book_name + " has been added to your basket."

    @staticmethod
    def eng_total_price(price):
        return "Your basket total is now " + price


class CartPageMessages(object):
    @staticmethod
    def empty_cart_text():
        return "Your basket is empty. Continue shopping"

    @staticmethod
    def cart_with_items_header_text():
        return "Items to buy now"
