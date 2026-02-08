from pathlib import Path
import numpy as np
import torch
from PIL import Image
from model import Generator as StyleGANGenerator


class Generator:
    def __init__(self, image_size=1024, latent_size=512, n_mlp=8, device="cuda"):
        model = StyleGANGenerator(size=image_size, style_dim=latent_size, n_mlp=n_mlp).to(device)
        model = model.eval()
        self.latent_size = latent_size
        self.model = model
        self.device = device

    def load_weights(self, weights_path: Path) -> None:
        state_dict = torch.load(weights_path, map_location=self.device)
        self.model.load_state_dict(state_dict)

    @torch.no_grad()
    def generate(self) -> Image.Image:
        z = torch.randn(1, self.latent_size, device=self.device)
        generated_image, _ = self.model([z])
        generated_image = (generated_image + 1) / 2.0 * 255.0
        generated_image = generated_image[0].permute(1, 2, 0).cpu().numpy().astype(np.uint8)
        generated_image = Image.fromarray(generated_image)
        return generated_image

