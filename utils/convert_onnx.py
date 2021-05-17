import fire
from pathlib import Path
from typing import Optional

from transformers.convert_graph_to_onnx import convert, quantize


def convert_model(model: str, path: Optional[str] = None):
    if not path:
        folder_name = Path(".").resolve().name
        path = Path("onnx") / f"{folder_name}.onnx"
    convert(
        framework="pt",
        model=str(Path(model).resolve()),
        output=Path(path),
        opset=11,
        pipeline_name="sentiment-analysis",  # needed for classification tasks
    )
    quantize(Path(path))


if __name__ == "__main__":
    fire.Fire()

