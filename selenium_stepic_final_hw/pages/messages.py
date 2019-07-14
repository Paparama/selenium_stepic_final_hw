class ProductPageMessages(object):
    @staticmethod
    def eng_add(book_name):
        return book_name + " has been added to your basket."

    @staticmethod
    def eng_total_price(price):
        return "Your basket total is now " + price
