from PIL import Image
import random

chars = "`^\",:;Il!i~+_-?][}{1)(|tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
reset_ansi = "\033[0m"

used_idx = set()

def rgb_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

for _ in range(10):  # Loop to repeat the process
    img_idx = random.randint(1, 10)
    while img_idx in used_idx:
        img_idx = random.randint(1, 10)
    img = Image.open((''.join('img' + str(img_idx) + '.jpg'))).convert('RGB')
    used_idx.add(img_idx)
    
    width, height = img.size
    max_width = 440
    w_percent = max_width / img.width
    new_height = int(img.height * w_percent)
    img = img.resize((max_width, new_height))
    final_image = []
   
    for y in range(img.size[1]):
        line = ''
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x, y))
            brightness = (max(r, g, b)) + (min(r, g, b)) / 2
            idx = int(brightness / 255 * (len(chars) - 1))
            char = chars[min((len(chars) - 1), idx)]
            line += f"{rgb_ansi(r, g, b)}{char * 3}{reset_ansi}"
        final_image.append(line)
    print("\n".join(final_image))
