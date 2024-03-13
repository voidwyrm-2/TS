from scene import *
import sound
import random
import math
A = Action


drawMode = True

windratio = 384, 800


def limit(input, max):
    if input > max: return max
    return input

def limitmin(input, min):
    if input < min: return min
    return input


def reversex(num: int, max: int):
    nums = []
    for n in range(max - 1):
        if n != 0: nums.append(n)
    return -nums[limitmin(num - 1, -(len(nums) - 1))]

def reversey(num: int, max: int):
    nums = []
    for n in range(max):
        if n != 0: nums.append(n)
    #log(f'Y:{nums}')
        #print(f'{num}, {n}({max})')
    return -nums[limitmin(num - 1, -(len(nums) - 1))]



def fixY(Ycoord: int): return -Ycoord


def convertx(coord: int, ratio: int):
    hratio = (ratio // 2)
    #print(hratio)
    if coord < hratio: return reversex(-coord, hratio)
    elif coord >= hratio: return coord - hratio

def converty(coord: int, ratio: int):
    hratio = (ratio // 2)
    #print(hratio)
    if coord < hratio: return reversey(-coord, hratio) #coord // 2
    elif coord >= hratio: return coord - hratio


def instructs(wayp: list):
    out = ''
    if len(wayp) <= 0: return
    for co in wayp:
        if len(co) >= 3: ins = f'{convertx(co[0], windratio[0])},{fixY(converty(co[1], windratio[1]))},{co[2]}'
        else: ins = f'{convertx(co[0], windratio[0])},{fixY(converty(co[1], windratio[1]))}'
        out = out + f'{ins}/'
    #if out[-1] == '/': del out[-1]
    return f'{convertx(wayp[0][0], windratio[0])},{fixY(converty(wayp[0][1], windratio[1]))},white/{out.removesuffix("/")}'


class weypoint (SpriteNode):
	def __init__(self, **kwargs):
		img = 'Turt.png'
		SpriteNode.__init__(self, img, **kwargs)

class MyScene (Scene):
	def setup(self):
		self.touchesN = 0
		wayps_font = ('Futura', 40)
		self.wayps_label = LabelNode('0', wayps_font, parent=self)
		self.wayps_label.position = (self.size.w/2, self.size.h - 70)
		self.wayps_label.z_position = 1
		
		self.wps = []
	
	def did_change_size(self):
		pass
	
	def update(self):
		self.wayps_label.text = str(len(self.wps))
		if len(self.wps) > 0:
			for w in self.wps:
				weyp = weypoint(parent=self)
				weyp.position = w
	
	def touch_began(self, touch):
		tX, tY = touch.location
		#self.touchesN += 1
		#print(f'got touched!({self.touchesN})')
		#print(f'{removedecimal(tX)},{removedecimal(tY)}')
		self.wps.append((int(tX), int(tY)))
		print(f'tX:{convertx(int(tX), windratio[0])},tY:{converty(int(tY), windratio[1])}')
	
	def touch_moved(self, touch):
		tXm, tYm = touch.location
		if drawMode:
			self.wps.append((int(tXm), int(tYm)))
	
	def touch_ended(self, touch):
		with open('drawings/TSPE.txt', 'wt') as fo:
			wpsa = self.wps
			wpsa.reverse()
			fo.write(str(instructs(wpsa)) + '\n')
			print('saved current waypoints')

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
