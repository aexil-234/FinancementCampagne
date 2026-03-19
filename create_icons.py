from PIL import Image, ImageDraw, ImageFont
import os

def create_icon(size):
    img = Image.new('RGB', (size, size), color='#1C1C1E')
    draw = ImageDraw.Draw(img)
    
    center_x = size // 2
    center_y = size // 2
    radius = int(size * 0.35)
    
    draw.ellipse(
        [(center_x - radius, center_y - radius), 
         (center_x + radius, center_y + radius)],
        fill='#34C759',
        outline='rgba(255, 255, 255, 0.2)',
        width=int(size * 0.02)
    )
    
    try:
        font_size = int(size * 0.4)
        font = ImageFont.truetype("/System/Library/Fonts/Apple Color Emoji.ttc", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "💰"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    text_x = center_x - text_width // 2
    text_y = center_y - text_height // 2
    
    draw.text((text_x, text_y), text, fill='white', font=font)
    
    filename = f'icon-{size}.png'
    img.save(filename)
    print(f'Created {filename}')

if __name__ == '__main__':
    create_icon(192)
    create_icon(512)
    print('Icons created successfully!')
