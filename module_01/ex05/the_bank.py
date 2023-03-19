class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str)
			raise AttributeError("Attribute name must be a str object.")

	def transfer(self, amount):
		self.value += amount


class Bank(object):
	def __init__(self):
		self.accounts = []

	def add(self, new_account):
		if not isinstance(new_account, Account):
			return False
		elif any(new_account.name == account.name for account in self.accounts):
			return False
		self.accounts.append(new_account)

	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
@origin: str(name) of the first account
@dest:
str(name) of the destination account
@amount: float(amount) amount to transfer
@return
True if success, False if an error occured
"""
		# ... Your code ...
		if not isinstance(origin, Account) and isinstance(dest, Account) and \
		isinstance(amount, (int, float)):
			return False

		def is_corrupted(account):
			if not len(account.__dict__) % 2:
				return True
			elif any(attribute.startswith('b') for attribute in account.__dict__):
				return True
			elif not any(attribute.startswith('zip') for attribute in account.__dict__):
				return True
			elif not any(attribute.startswith('addr') for attribute in account.__dict__):
				return True
			elif 'name' not in account.__dict__ or not isinstance(account.name, str):
				return True
			elif 'id' not in account.__dict__ or not isinstance(account.id, int):
				return True
			elif 'value' not in account.__dict__ or not isinstance(account.value, (int, float)):
				return True

		if amount < 0 or amount > origin.value:
			return False
		elif is_corrupted(origin) or is_corrupted(dest):
			return False
		if origin.name != dest.name:
			origin.value -= amount
			dest.value += amount
		return True

	def fix_account(self, name):
		""" fix account associated to name if corrupted
@name:
str(name) of the account
@return True if success, False if an error occured
"""
		# ... Your code ...
