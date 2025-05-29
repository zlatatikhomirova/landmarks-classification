from PIL import Image
import io
import base64

def base64_to_pil_image(image_base64: str) -> Image:
    return Image.open(io.BytesIO(base64.decodebytes(bytes(image_base64, \
                                                          "utf-8")))).convert('RGB')
