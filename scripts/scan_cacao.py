import openfoodfacts
import time

def scan_cacao():
    api = openfoodfacts.API(user_agent="MongoProject/1.0")
    
    # 1. On cherche d'abord combien il y a de produits au total
    keyword = "cacao"
    print(f"🔍 Initialisation de la recherche pour '{keyword}'...")
    
    # Une première requête pour avoir le compteur total ("count")
    first_result = api.product.text_search(keyword, page=1, page_size=1)
    total_products = first_result["count"]
    print(f"📦 Total de produits trouvés : {total_products}")
    
    products_collected = []
    page_size = 50  # On en prend 50 par page
    max_products = 200 # 🛑 LIMITATION VOLONTAIRE POUR LE TEST (mettez 0 pour tout prendre)
    
    # Si max_products est 0 ou non défini, on prend tout
    target_count = max_products if max_products > 0 else total_products
    
    page = 1
    while len(products_collected) < target_count:
        print(f"   📄 Chargement page {page}...")
        
        try:
            result = api.product.text_search(keyword, page=page, page_size=page_size)
            products = result["products"]
            
            if not products:
                break # Plus de produits
                
            for p in products:
                # On ne garde que l'essentiel
                info = {
                    "code": p.get("code"),
                    "name": p.get("product_name", "Inconnu"),
                    "brands": p.get("brands", ""),
                    "ingredients": p.get("ingredients_text", "")[:100] + "..." # On coupe pour l'affichage
                }
                products_collected.append(info)
                
                if len(products_collected) >= target_count:
                    break
            
            page += 1
            time.sleep(0.5) # Petite pause pour être gentil avec l'API
            
        except Exception as e:
            print(f"❌ Erreur: {e}")
            break

    # Affichage des résultats
    print(f"\n✅ Récolte terminée : {len(products_collected)} produits récupérés sur {total_products} existants.")
    print("-" * 50)
    for p in products_collected[:10]: # Affiche les 10 premiers
        print(f"[{p['code']}] {p['name']} ({p['brands']})")

if __name__ == "__main__":
    scan_cacao()
