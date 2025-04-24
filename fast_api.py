import gradio as gr
from PIL import Image, ImageOps
from transparent_background import Remover
import os
from datetime import datetime

remover = Remover()

def remove_bg(input_img):
    os.makedirs("done", exist_ok=True)
    img = ImageOps.exif_transpose(input_img).convert("RGB")
    if img.width > 1500:
        img = img.resize((img.width // 2, img.height // 2))

    out = remover.process(img)
    return out

interface = gr.Interface(
    fn=remove_bg,
    inputs=gr.Image(type="pil"),
    outputs=gr.Image(type="pil"),
    title="Background Remover",
    description="Upload an image and remove its background!"
    
)

interface.launch(share=True)
