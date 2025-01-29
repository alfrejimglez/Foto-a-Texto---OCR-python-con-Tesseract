import pytesseract
from PIL import Image

def extract_text(image_path, output_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="spa")
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)
        print(f"Texto extraído y guardado en {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    image_path = input("Introduce la ruta de la imagen: ")
    output_path = "texto_extraido.txt"
    extract_text(image_path, output_path)
