from pathlib import Path
from src.generator import Generator
from PIL import Image, ImageDraw, ImageFont

from PIL import Image

NUM_IMAGES = 20

OUTPUT_PATH = Path("assets/demo.gif")
OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)


def main():
    model = Generator()
    model_weights = list(Path("weights").iterdir())

    frames = []
    for _ in range(NUM_IMAGES):
        images = []
        for model_weight in model_weights:
            model.load_weights(model_weight)
            gen_image = model.generate()

            w, h = gen_image.size
            out = Image.new("RGB", (w, h + 80), (0, 0, 0))
            out.paste(gen_image, (0, 0))
            caption = f"Photo->{model_weight.stem}"
            draw = ImageDraw.Draw(out)
            font = ImageFont.load_default(48)
            tw, th = draw.textbbox((0, 0), caption, font=font)[2:]
            x = (w - tw) // 2
            y = h + (80 - th) // 2
            draw.text((x, y), caption, fill=(255, 255, 255), font=font)
            images.append(out)

        image_size = images[0].size
        frame = Image.new('RGB', (image_size[0] * len(images), image_size[1]))
        for i, image in enumerate(images):
            frame.paste(image, (i * image_size[0], 0))
        frames.append(frame)
    
    frame_one = frames[0]
    frame_one.save(OUTPUT_PATH, format="GIF", append_images=frames,
               save_all=True, duration=750, loop=0)
    

if __name__ == "__main__":
    main()