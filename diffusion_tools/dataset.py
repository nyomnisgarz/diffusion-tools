from pathlib import Path

def prepare_dataset(image_dir, caption_file=None):
    """Prepare dataset for diffusion model training."""
    images = list(Path(image_dir).glob('*.jpg')) + list(Path(image_dir).glob('*.png'))
    return {'images': len(images), 'captions': caption_file}
