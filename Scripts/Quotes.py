import random

class RandomQuote:
    def __init__(self):
        pass
    
    def get_random_quote(self):
        quotes = [
        ("Do not save what is left after spending, but spend what is left after saving.", "Warren Buffett"),
        ("Beware of little expenses; a small leak will sink a great ship.", "Benjamin Franklin"),
        ("It’s not your salary that makes you rich, it’s your spending habits.", "Charles A. Jaffe"),
        ("If you buy things you do not need, soon you will have to sell things you need.", "Warren Buffett"),
        ("Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like.", "Will Rogers"),
        ("Frugality includes all the other virtues.", "Cicero"),
        ("Balancing your money is the key to having enough.", "Elizabeth Warren"),
        ("Every time you borrow money, you’re robbing your future self.", "Nathan W. Morris"),
        ("A budget is telling your money where to go instead of wondering where it went.", "Dave Ramsey"),
        ("You must gain control over your money, or the lack of it will forever control you.", "Dave Ramsey"),
        ]
        return random.choice(quotes)
        
        