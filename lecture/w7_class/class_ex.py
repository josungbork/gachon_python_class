class Ball:
	size = 0
	color = ''
	direction =''

	def bounce(self):
		if self.direction == 'down':
			self.direction = 'up'
		else:
			self.direction = 'down'

myBall = Ball()
yourBall = Ball()

myBall.color = "red"
yourBall.color ="blue"

print myBall.color, " ", yourBall.color
