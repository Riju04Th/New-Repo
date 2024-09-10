from PIL import Image, ImageEnhance
def enhance_image(input_image_path, output_image_path, brightness_factor=1.2, contrast_factor=1.3, sharpness_factor=2.0):
    with Image.open(input_image_path) as img:
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(brightness_factor)
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast_factor)
        enhancer = ImageEnhance.Sharpness(img)
        img = enhancer.enhance(sharpness_factor)
        img.save(output_image_path)
input_image_path = 'input.jpg'
output_image_path = 'enhanced_image.jpg'
enhance_image(input_image_path, output_image_path)