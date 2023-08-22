import json
import re

def extract_specification_codes(text):
    # Buscar códigos de especificación en el texto
    pattern = r'ESPECIFICACION:(\d{3,5})'
    codes = re.findall(pattern, text)
    return codes

def process_annotations(annotation_list):
    processed_annotations = []
    for idx, annotation in enumerate(annotation_list, start=1):
        annotation_text = annotation.get("textoAnotaciones", "")
        spec_codes = extract_specification_codes(annotation_text)
        for code in spec_codes:
            processed_annotations.append({
                "numero": idx,
                "codigo_especificacion": code
            })
    return processed_annotations

def main(input_file, output_file):
    with open(input_file, "r") as f:
        data = json.load(f)
    
    fmi = data.get("fmi", "")
    annotations = data.get("anotaciones", [])
    
    processed_annotations = process_annotations(annotations)
    
    result = {
        "fmi": fmi,
        "anotaciones": processed_annotations
    }
    
    with open(output_file, "w") as f:
        json.dump(result, f, indent=4)

if __name__ == "__main__":
    input_file = "input.json"  # Cambia esto al nombre de tu archivo JSON de entrada
    output_file = "output.json"  # Nombre deseado para el archivo JSON de salida
    main(input_file, output_file)