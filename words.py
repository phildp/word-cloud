import json

class Word():
	def __init__(self, text, size):
		self.text = text
		self.size = size

	def dump(self):
		return {'text': self.text,
				'size': self.size}

	# def toJSON(self):
	# 	return json.dumps([o.dump() for o in ])
		