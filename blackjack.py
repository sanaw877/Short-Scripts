import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
'Jack', 'King', 'Queen', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
'Nine': 9, 'Ten': 10, 'Jack': 10, 'King': 10, 'Queen': 10, 'Ace': 11}

playing = True

class Card():

	def __init__(self, suit, rank):

		self.suit = suit
		self.rank = rank

	def __str__(self):
		return f"{self.rank} of {self.suit}"

class Deck():
	"""docstring for Deck"""
	def __init__(self):
		self.card_list = [ ]
		
		for suit in suits:
			for rank in ranks:
				card = Card(suit, rank)
				self.card_list.append(card)

	# def shuffle(self, cards):
	# 	for i in range(0,52):
	# 		num = random.randint(0,52)
	# 		card = cards[num]
	# 		shuffled_list.append(card)

		# return shuffled_list

	def __str__(self):
		deck = ' ,'.join(str(c) for c in self.card_list) # LOOK AT THIS LATER
		return deck

	def shuffle(self):
		random.shuffle(self.card_list)

	def deal(self):
		card = self.card_list.pop()

		return card


class Hand():
	"""docstring for Hand"""
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self, card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1

	def aces_adjustment(self):
		while self.value > 21 & self.aces > 0:
			self.aces -= 1
			self.value -= 10

class Chips():
	def __init__(self, value):
		self.value = value
		self.bet = 0 #????

		def win_bet(self):
			self.value += self.bet

		def lose_bet(self):
			self.value -= self.bet

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How much would you like to bet?"))
		except ValueError:
			"Sorry, that is not a valid integer."
		else:
			if chips.bet <= chips.value:
				break
			else:
				print("Sorry, you cannot bet more than your total.")

def take_hit(deck, hand):
		hand.value = add_card(deck.deal())
		hand.aces_adjustment()

def hit_or_stand(deck, hand):
	answer = input("Would you like to hit or stand?").lower()

	if answer == 'hit':
		take_hit(deck, hand)
	else:
		playing = False


test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())
print(str(test_player.value))

for card in test_player.cards:
	print(card)
