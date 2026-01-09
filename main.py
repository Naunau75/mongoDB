
import openfoodfacts

def main():
    # User-Agent est obligatoire
    api = openfoodfacts.API(user_agent="MongoProject/1.0")

    # Exemple : Récupérer des infos sur le Nutella
    code = "3017620422003"
    product = api.product.get(code, fields=["code", "product_name", "ingredients_text", "nutriments"])
    
    print(f"Produit : {product.get('product_name')}")
    print(f"Ingrédients : {product.get('ingredients_text')}")
    print(f"Nutriments : {product.get('nutriments')}")

    # Exemple : Recherche textuelle
    print("\nRecherche de 'mineral water'...")
    search_result = api.product.text_search("mineral water", page=1, page_size=2)
    for p in search_result["products"]:
        print(f"- {p.get('product_name')} ({p.get('code')})")

if __name__ == "__main__":
    main()
