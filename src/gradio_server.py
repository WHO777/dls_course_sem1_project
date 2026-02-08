from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import gradio as gr
from src.generator import Generator

WEIGHTS_DIR = Path("weights")
WEIGHTS_DIR.mkdir(parents=True, exist_ok=True)


@dataclass
class AppState:
    model: Generator
    loaded_weights: Optional[str] = None


def list_weights() -> List[str]:
    return sorted([p.stem for p in WEIGHTS_DIR.iterdir() if p.is_file()])


def ensure_state(state: Optional[AppState]) -> AppState:
    return state or AppState(model=Generator())


def on_weights_change(weights_name: str, state: Optional[AppState]) -> AppState:
    state = ensure_state(state)
    if not weights_name:
        return state

    if state.loaded_weights == weights_name:
        return state

    weights_path = WEIGHTS_DIR / weights_name

    state.model.load_weights(weights_path)
    state.loaded_weights = weights_name
    return state


def generate(weights_name: str):
    global LOADED_WEIGHTS

    if not weights_name:
        raise gr.Error("Выбери веса")

    weights_path = WEIGHTS_DIR / f"{weights_name}.pth"
    if not weights_path.is_file():
        raise gr.Error(f"Файл весов не найден: {weights_path}")

    if LOADED_WEIGHTS != weights_path:
        MODEL.load_weights_inplace(weights_path)
        LOADED_WEIGHTS = weights_path
    return MODEL.sample()


css = """
.centered { max-width: 520px; margin: 0 auto !important; }
.centered .gr-image { margin: 0 auto !important; }
"""


MODEL = Generator()
LOADED_WEIGHTS = None


with gr.Blocks(css=css, title="Minimal Generator") as demo:
    with gr.Column(elem_classes=["centered"]):
        weights = gr.Dropdown(label="Weights", choices=list_weights(), interactive=True)
        out = gr.Image(label="", type="pil", height=512)
        btn = gr.Button("Generate", variant="primary")

    btn.click(fn=generate, inputs=weights, outputs=out)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
