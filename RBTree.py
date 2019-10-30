
class RBNode(object): 
	def __init__(self, word = "", key = 0, left = None, parent = None, right = None, color = -1): 
		self.word = word #added attribute 
		self.key = word
		self.left = None
		self.parent = None
		self.right = None
		self.color = -1 #colors use 1 and 0s instead of strings. 

class RedBlack(object): 
	#0 --> black
  #1 --> red.
	def __init__(self, root = None): 
		self.root = None
		
	def bstInsert(self, node):
		if (self.root == None):
			self.root = node
			node.left = None 
			node.right = None
			
		else:
			cur = self.root
			while (cur != None): 
				if (node.word < cur.word):
					if (cur.left == None):
						cur.left = node
						cur = None
					else:
						cur = cur.left
				else:
					if (cur.right == None):
						cur.right = node
						cur = None
					else:
						cur = cur.right 
						
			node.left = None 
			node.right = None 
		
	def rbInsert(self, words, key = 0): 
		node = RBNode(words, key)
		
		self.bstInsert(node)
		node.color = 1 #red 
		self.rbBalance(node)
		
	def rbBalance(self, node):
		if (node.parent == None): 
			node.color = 0 #black 
			return
		
		if (node.parent.color == 0): #black
			return

		parent = node.parent
		grandparent = self.rb_get_grandparent(node)
		uncle = self.rb_getUncle(node)
		
		if (uncle != None and uncle.color == 1): #red 
			parent.color = uncle.color = 0 #black
			grandparent.color = 1 #red 
			self.rbBalance(grandparent)
			return
			
		if (node == parent.right and parent == grandparent.left):
			self.rb_rotateLeft(parent)
			node = parent
			parent = node.parent
			
		elif (node == parent.left and parent == grandparent.right):
			self.rb_rotateRight(parent)
			node = parent
			parent = node.parent
			
		parent.color = 0 #black 
		grandparent.color = 1 #red 
		
		if (node == parent.left):
			self.rb_rotateRight(grandparent)
			
		else:
			self.rb_rotate_left(grandparent)
			
	def rb_get_grandparent(self, node): 
		if (node.parent == None):
			return None 
		
		return node.parent.parent
		
	def rb_getUncle(self, node): 
		grandparent = None 
		if (node.parent != None):
			grandparent = node.parent.parent
			
		if (grandparent == None):
			return None 
			
		if (grandparent.left == node.parent):
			return grandparent.right
			
		else:
			return grandparent.left
			
	
	def rb_rotateLeft(self, node): 
		right_left_child = node.right.left
		if (node.parent != None):
			self.rb_replaceChild(node.parent, node, node.right)
		else:
			self.root = node.right
			self.root.parent = None

		self.rb_setChild(node.right, "left", node)
		self.rb_setChild(node, "right", right_left_child)
		
	def rb_rotateRight(self, node):
		left_right_child = node.left.right
		if (node.parent != None):
			self.rb_replaceChild(node.parent, node, node.left)
		else:
			self.root = node.left
			self.root.parent = None
			
		self.rb_setChild(node.left, "right", node)
		self.rb_setChild(node, "left", left_right_child)
	
	def rb_setChild(self, parent, which_child, child): 
		if (which_child != "left" and which_child != "right"):
			return False
		
		if (which_child == "left"):
			parent.left = child
		
		else:
			parent.right = child
		
		if (child != None):
			child.parent = parent
			
		return True
		
	def rb_replaceChild(self, parent, current_child, new_child): 
		if (parent.left == current_child):
			return self.rb_setChild(parent, "left", new_child)
			
		elif (parent.right == current_child):
			return self.rb_setChild(parent, "right", new_child)
			
		return False