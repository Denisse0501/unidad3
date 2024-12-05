# Representación simple del árbol genealógico
familia = {
    "Abuelos": ["Margarita", "José"],
    "Hijos de los abuelos": {
        "Citlali (Mamá)": {
            "Pareja": "Salvador",
            "Hijos": ["Brenda Denisse", "Brian Alejandro"]
        },
        "Lidia (Tía)": [],
        "Rosendo (Tío)": []
    }
}

# Función simple para imprimir el árbol genealógico
def imprimir_arbol_simple(estructura, nivel=0):
    if isinstance(estructura, dict):
        for clave, valor in estructura.items():
            print("  " * nivel + f"- {clave}")
            imprimir_arbol_simple(valor, nivel + 1)
    elif isinstance(estructura, list):
        for item in estructura:
            print("  " * nivel + f"- {item}")
    elif isinstance(estructura, str):
        print("  " * nivel + f"- {estructura}")

# Imprime el árbol genealógico
imprimir_arbol_simple(familia)
