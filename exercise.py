from PIL import Image, ImageDraw
import numpy as np
from math import dist

happy_colors = [
    (255, 255, 0),   # Yellow
    (255, 165, 0),   # Orange
    (255, 0, 0),     # Red
    (255, 192, 203)  # Pink
]

def is_happy_color(rgb):
    for color in happy_colors:
        if dist(rgb, color) < 100:
            return True
    return False

def verify_badge(image_path):
    # Open the image
    img = Image.open(image_path).convert("RGBA")
    
    if img.size != (512, 512):
        return False, "Image is not 512x512 pixels"

    width, height = img.size
    radius = width // 2
    
    pixels = np.array(img)
    badge_pixel_count = 0
    happy_pixel_count = 0
    for y in range(height):
        for x in range(width):
            # Calculate distance from center
            dist = int(((x - radius)**2 + (y - radius)**2)**0.5)

            if dist > radius:
                # Check if non transparent pixels are outside of the badge
                if pixels[y, x][3] != 0:
                    return False, "Non-transparent pixels found outside the circle"
            else:
                # Count the numbers of happy pixel and non transparent pixel
                if pixels[y, x][3] != 0:
                    badge_pixel_count += 1
                    if is_happy_color(pixels[y, x][:3]):
                        happy_pixel_count += 1
    
    # Get the percentage of happy color
    happy_percentage = (happy_pixel_count / badge_pixel_count) * 100
    print("happy percentage : ", happy_percentage)
    if happy_percentage < 50:
        return False, "Colors do not give a happy feeling"
    
    return True, "Badge is valid"

def convert_to_badge(image_path, output_path):

    img = Image.open(image_path).convert("RGBA")
    img = img.resize((512, 512), Image.LANCZOS)
    
    # Create an RGBA mask with a transparent background
    mask = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    draw = ImageDraw.Draw(mask)
    
    # Draw a white circle on the mask
    draw.ellipse((0, 0, 512, 512), fill=(255, 255, 255, 255))
    
    # Create a new image with a transparent background
    result = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
    
    # Apply mask and save
    result = Image.composite(img, result, mask)
    result.save(output_path, format='PNG')


# Test
#convert_to_badge("test.png", "badge.png")
#is_valid, message = verify_badge("badge.png")