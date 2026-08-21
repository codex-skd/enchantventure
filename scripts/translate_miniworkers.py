import json, re, sys, os

def translate_text(text):
    # simple word replacements, case-sensitive handling of capitalized first word
    replacements = {
        "Mini Workers": "Mini Trabajadores",
        "Sorting Pipe": "Tubería de Clasificación",
        "Express Sorting Pipe": "Tubería de Clasificación Rápida",
        "Sorting Junction": "Cruzamiento de Clasificación",
        "Compost Station": "Estación de Compost",
        "Compactor Station": "Estación de Compactador",
        "Pipe Wrench": "Llave de Tubería",
        "Glass pipe": "Tubería de Vidrio",
        "Moves items": "Mueve objetos",
        "Moves items from input to output": "Mueve objetos de la entrada a la salida",
        "Use Pipe Wrench to adjust direction": "Usa la llave de tubería para ajustar la dirección",
        "Glass pipe body shows moving items inside": "El cuerpo de tubería de vidrio muestra los objetos moviéndose dentro",
        "Moves items at twice the normal pipe speed": "Mueve objetos al doble de la velocidad normal de la tubería",
        "Sends matching filtered items to the side output": "Envía los objetos filtrados coincidentes a la salida lateral",
        "Non-matching items continue forward": "Los objetos no coincidentes continúan hacia adelante",
        "Right-click to configure filters": "Haz clic derecho para configurar filtros",
        "Accepts vanilla compostable items in 9 Input slots": "Acepta objetos compostables vanilla en 9 ranuras de Entrada",
        "Slowly matures compost mass into Bone Meal": "Madura lentamente la masa de compost en Harina Ósea",
        "Sorting Pipes can extract from 3 protected Output slots": "Las tuberías de clasificación pueden extraer de 3 ranuras de Salida protegidas",
        "Set a ghost result item to choose what to compact": "Establece un objeto de resultado fantasma para elegir qué compactar",
        "Supports safe 9-to-1 recipes with one ingredient type": "Soporta recetas seguras 9-a-1 con un tipo de ingrediente",
        "Pipes insert matching ingredients and extract Output": "Las tuberías insertan ingredientes coincidentes y extraen la Salida",
        "Item": "Objeto",
        "Block": "Bloque",
        "Items": "Objetos",
        "Input": "Entrada",
        "Output": "Salida",
        "speed": "velocidad",
        "filter": "filtro",
        "filters": "filtros",
        "adjust": "ajustar",
        "direction": "dirección",
        "ghost": "fantasma",
        "result": "resultado",
        "compact": "compactar",
        "recipe": "receta",
        "automation": "automatización",
        "target": "objetivo",
        "configuration": "configuración",
        "title": "título",
        "section": "sección",
        "common": "común",
        "toml": "toml",
        "items": "objetos",
        "log": "registro",
        "dirt": "tierra",
        "block": "bloque",
        "magic": "mágico",
        "number": "número",
        "introduction": "introducción",
        "line": "línea",
    }
    # Replace longer phrases first
    for eng, esp in sorted(replacements.items(), key=lambda x: -len(x[0])):
        pattern = re.compile(re.escape(eng))
        text = pattern.sub(esp, text)
    return text

def main():
    src_path = sys.argv[1]
    dst_path = sys.argv[2]
    with open(src_path, encoding='utf-8') as f:
        data = json.load(f)
    translated = {k: translate_text(v) for k, v in data.items()}
    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, 'w', encoding='utf-8') as f:
        json.dump(translated, f, ensure_ascii=False, indent=2, sort_keys=False)

if __name__ == '__main__':
    main()
