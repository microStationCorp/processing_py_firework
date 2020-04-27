angle = [0, 10, 20, 40, 60, 80, 100, 120, 140, 160,
         180, 200, 220, 240, 260, 280, 300, 320, 340]
stars = []

class Star:

    def __init__(self, pos, color_, velocity):
        self.pos = pos
        self.color_ = color_
        self.velocity = velocity
        self.len_ = velocity
        self.sub_star = []

    def show(self):
        self.sub_star = self.manipulate()
        for p in self.sub_star:
            strokeWeight(self.velocity / 2)
            stroke(self.color_[0], self.color_[1], self.color_[2])
            point(p[0], p[1])

    def manipulate(self):
        sub_star = []
        for i in range(len(angle)):
            x = self.pos[0] + self.len_ * cos(radians(angle[i]))
            y = self.pos[1] + self.len_ * sin(radians(angle[i]))
            sub_star.append([x, y])
        self.len_ += self.velocity
        self.velocity -= 1
        return sub_star

def setup():
    size(600, 600)
    frameRate(10)

def draw():
    global star, stars
    background(51)
    if len(stars) != 0:
        for star in stars:
            if star.velocity != 0:
                star.show()
            if star.velocity == 10 or star.velocity == 5:
                stars.append(
                    Star([random(100, width - 100), random(100, height - 100)], [random(200, 255), random(100, 200), random(100, 200)], 15))

    if len(stars) > 10:
        del stars[:-4]

def mousePressed():
    global stars
    stars.append(
        Star([random(100, width - 100), random(100, height - 100)], [random(100, 255), random(0, 100), random(100, 200)], 15))
