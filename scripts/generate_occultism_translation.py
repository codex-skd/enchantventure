import json, re, sys, os

def load_json(path):
    with open(path, encoding='utf-8') as f:
        return json.load(f)

def simple_translate(text):
    # Basic word replacements for Minecraft terms
    word_map = {
        'Use': 'Usar',
        'the': 'el',
        'Black': 'Negro',
        'Blue': 'Azul',
        'Brown': 'Marrón',
        'Cyan': 'Cian',
        'Gray': 'Gris',
        'Green': 'Verde',
        'Light': 'Claro',
        'Lime': 'Lima',
        'Magenta': 'Magenta',
        'Orange': 'Naranja',
        'Pink': 'Rosa',
        'Purple': 'Morado',
        'Rainbow': 'Arcoíris',
        'Red': 'Rojo',
        'Void': 'Vacío',
        'White': 'Blanco',
        'Yellow': 'Amarillo',
        'Chalk': 'Tiza',
        'Chalk Glyph': 'Glifo de Tiza',
        'Foundation': 'Fundación',
        'Tier': 'Nivel',
        'Bait': 'Cebo',
        'for': 'para',
        'what?': '¿qué?',
        'Ancient': 'Antiguo',
        'Knowledge': 'Conocimiento',
        'Third': 'Tercero',
        'Second': 'Segundo',
        'Wild': 'Salvaje',
        'Stabilizer': 'Estabilizador',
        'Attraction': 'Atracción',
        'Power': 'Poder',
        'Dragon': 'Dragón',
        '...': '…',
        'First': 'Primero',
        'Occultism:': 'Occultismo:',
        'Chalks': 'Tizas',
        'Chalks.': 'Tizas.',
        'Chalks': 'Tizas',
        'Chalks': 'Tizas',
        'Chalks': 'Tizas',
        'Chalks': 'Tizas',
    }
    # Replace words case-sensitively preserving capitalization
    def repl(match):
        w = match.group(0)
        key = w
        if w in word_map:
            return word_map[w]
        # lower case fallback
        lower = w.lower()
        if lower in word_map:
            return word_map[lower]
        return w
    # Tokenize by word boundaries
    result = re.sub(r'\b\w+\b', repl, text)
    # Fix double spaces
    result = re.sub(r'\s+', ' ', result).strip()
    return result

def main():
    en_path = sys.argv[1]
    orig_path = sys.argv[2]
    out_path = sys.argv[3]
    en = load_json(en_path)
    orig = load_json(orig_path)
    out = {}
    for k, eng_val in en.items():
        orig_val = orig.get(k)
        if orig_val and orig_val != eng_val:
            out[k] = orig_val
        else:
            out[k] = simple_translate(eng_val)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
