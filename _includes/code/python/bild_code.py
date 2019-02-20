from random import randint

__author__ = 'Mark Weinreuter'


message = "Hallo Welt"

from PIL import Image
COLORS = [(255, 0,0), (0, 255, 0), (0,0,255)]
w_img = 60
h_img = 20

c2d = lambda c: ord(c) - ord('a') if ord('a') <= ord(c) <= ord('z') else print("Nur a-z ist erlaubt!!")
i2ba = lambda i: list(map(int, bin(i)[2:]))
flatten = lambda l: [item for sublist in l for item in sublist]



msg_data = list(flatten(map(i2ba, (map(ord, "hallowelta")))))
rem3 = len(msg_data)  // 3
msg_data += [0] * rem3
pad = 0#randint(0, w_img * h_img - len(msg_data))
print(msg_data)

im = Image.new("RGB", (w_img, h_img))
off = 0
data = []
for h in range(h_img):
    i = randint(1, 6)
    w_line = w_img//i
    print(i)
    for w in range(i):
        data += [COLORS[randint(0,len(COLORS)-1)]] * w_line
print(len(data))
img_idx = 0
mod = lambda i, c: i +c if i < 128 else i -c
for idx in range(0, len(msg_data),3):
    old = data[pad+img_idx]
    data[pad+img_idx] = (mod(old[0] , msg_data[idx+1]), mod(old[1],  msg_data[idx+1]), mod(old[2] , msg_data[idx+2]))
    img_idx+=1
im.putdata(data)

print(im.getpixel((0,0)))
im.save(open("test.bmp", "wb"))