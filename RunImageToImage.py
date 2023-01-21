
CHECKPOINT_PATH = "v2-1_768-ema-pruned.ckpt"
CONFIG = "configs/stable-diffusion/v2-inference-v.yaml"
HEIGHT = 768
WIDTH = 768
PROMPT = "dry stone walls watercolor"

from scripts.img2img import main, parse_args

arg_dict = {
    "prompt": PROMPT,
    "ckpt": CHECKPOINT_PATH,
    "config": CONFIG,
    "H": HEIGHT,
    "W": WIDTH,
    "seed": 42,
    "n_samples": 1,
    "n_iter": 1,
    "ddim_steps": 30,
    "init_img": "input_images/castle_hill.jpg",
}

opt = parse_args()

for key, value in arg_dict.items():
    opt.__setattr__(key, value)

if __name__ == '__main__':
    main(opt)
