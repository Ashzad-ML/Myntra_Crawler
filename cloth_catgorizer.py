import os
import shutil

def men_categorize_images():
    # Keywords for categorization
    tshirt_keywords = ["t-shirt", "polo"]
    formal_shirt_keywords = ["formal-shirt"]
    casual_shirt_keywords = ["casual-shirt", "casual-sustainable-shirt"]
    sweatshirt_keywords = ["sweatshirt","hoodie"]
    mensweater_keywords = ["pullover"]
    mensjacket_keywords = ["jacket","bomber"]
    mensblazer_keywords = ["formal-blazer","blazer"]
    mensuits_keywords = ["formal-suit", "three-piece-formal-suit", "suits","tuxedo","formal-2-piece-suit"]
    menkurta_keywords = ["kurta"]
    menranjackets_keywords = ["rain-jacket", "reversible-hooded-rain-jacket"]
    menSherwani_keywords = ["sherwani-set", "sherwani-with-churidar"]
    mennehrujacket_keywords = ["nehru-jacket"]
    mendhoti_keywords = ["dhoti"]
    menjeans_keywords = ["jeans"]
    mentrousers_keywords = ["trousers", "cargos-trousers", "formal-trousers","trouser","cargos"]
    menshorts_keywords = ["chino-shorts", "sports-shorts", "cotton-shorts", "shorts"]
    mentrackpants_keywords = ["trackpants", "joggers","track-pants"]

    # Categorize folders
    categorized_folders = {
        "Men-T-Shirt": [],
        "Men-Formal Shirt": [],
        "Men-Casual Shirt": [],
        "Men-Sweat Shirt": [],
        "Men-Sweater": [],
        "Men-Jacket": [],
        "Men-Blazer": [],
        "Men-Suits": [],
        "Men-Rain-Jackets": [],
        "Men-Kurta": [],
        "Men-Sherwani": [],
        "Men-Nehru-Jacket": [],
        "Men-Dhoti": [],
        "Men-Jeans": [],
        "Men-Trousers": [],
        "Men-Shorts": [],
        "Men-Trackpants": []
    }

    # Get the Men-Categories directory
    current_directory = os.getcwd()
    men_categories_directory = os.path.join(current_directory, 'Men-Categories')

    # Ensure the Men-Categories directory exists
    if not os.path.exists(men_categories_directory):
        print("Men-Categories directory does not exist.")
        return

    # Get all folders in the Men-Categories directory
    folders = [f for f in os.listdir(men_categories_directory) if os.path.isfile(os.path.join(men_categories_directory, f))]

    for folder in folders:
        if any(keyword in folder for keyword in tshirt_keywords):
            categorized_folders["Men-T-Shirt"].append(folder)
        elif any(keyword in folder for keyword in formal_shirt_keywords):
            categorized_folders["Men-Formal Shirt"].append(folder)
        elif any(keyword in folder for keyword in casual_shirt_keywords):
            categorized_folders["Men-Casual Shirt"].append(folder)
        elif any(keyword in folder for keyword in sweatshirt_keywords):
            categorized_folders["Men-Sweat Shirt"].append(folder)
        elif any(keyword in folder for keyword in mensweater_keywords):
            categorized_folders["Men-Sweater"].append(folder)
        elif any(keyword in folder for keyword in mennehrujacket_keywords):
            categorized_folders["Men-Nehru-Jacket"].append(folder)
        elif any(keyword in folder for keyword in menranjackets_keywords):
            categorized_folders["Men-Rain-Jackets"].append(folder)
        elif any(keyword in folder for keyword in mensjacket_keywords):
            categorized_folders["Men-Jacket"].append(folder)   
        elif any(keyword in folder for keyword in mensblazer_keywords):
            categorized_folders["Men-Blazer"].append(folder) 
        elif any(keyword in folder for keyword in mensuits_keywords):
            categorized_folders["Men-Suits"].append(folder)
        elif any(keyword in folder for keyword in menkurta_keywords):
            categorized_folders["Men-Kurta"].append(folder)
        elif any(keyword in folder for keyword in menSherwani_keywords):
            categorized_folders["Men-Sherwani"].append(folder)
        elif any(keyword in folder for keyword in mendhoti_keywords):
            categorized_folders["Men-Dhoti"].append(folder)
        elif any(keyword in folder for keyword in menjeans_keywords):
            categorized_folders["Men-Jeans"].append(folder)
        elif any(keyword in folder for keyword in mentrousers_keywords):
            categorized_folders["Men-Trousers"].append(folder)
        elif any(keyword in folder for keyword in menshorts_keywords):
            categorized_folders["Men-Shorts"].append(folder)
        elif any(keyword in folder for keyword in mentrackpants_keywords):
            categorized_folders["Men-Trackpants"].append(folder)

    # Create directories for each category and move folders
    for category, items in categorized_folders.items():
        category_path = os.path.join(men_categories_directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        for item in items:
            shutil.move(os.path.join(men_categories_directory, item), os.path.join(category_path, item))

    # Print the result
    for category, items in categorized_folders.items():
        print(f"{category}:")
        for item in items:
            print(f"  - {item}")


def women_categorize_images():
    # Keywords for categorization
    krtansuits_keywords = ["kurta", "kurta-with-palazzos","kurta-with-trousers--dupatta"]
    kurti_tunic_keywords = ["tunic","kurti"]
    saree_keywords = ["saree"]
    nightsuits_keywords = ["night-shirt-and-trousers","night-suit","co-ords","co-ord"]
    leggings_salwar_keywords = ["leggings","salwar"]
    skirt_keywords = ["skirt","plazzos","palazzos"]
    dressmaterial_keywords = ["dress-materia"]
    lehenga_keywords = ["lehenga"]
    dupattanshawl_keywords = ["shawl","dupatta"]
    womenjackets_keywords = ["jacket", "gilet"]
    dresses_keywords =[ "dress", "dresses"]
    tshirt_keywords = ["t-shirt"]
    top_keywords = ["top"]
    womenjeans_keywords = ["jeans"]
    womentrousers_keywords = ["trousers", "cargos", "trouser"]
    shorts_keywords = ["skorts","shorts"]
    playsuit_keywords = ["jumpsuit", "playsuit"]
    shrug_keywords = ["shrug"]
    overcoat_keywords = ["trench-coat","overcoat"]
    blazer_keywords = ["blazer","waistcoat"]
    sweater_keywords = ["hoodie","sweatshirt","cardigan","sweaters","sweater","pullover"]
    
    

    # Categorize folders
    categorized_folders = {
        "Women-Kurta-Suits": [],
        "Women-Kurti-Tunic": [],
        "Women-Saree": [],
        "Women-Night-Suit": [],
        "Women-Legging-Salwar": [],
        "Women-Skirt-Plazzos": [],
        "Women-DressMaterials": [],
        "Women-Lehenga": [],
        "Women-Dupatta-Shawl": [],
        "Women-Jackets": [],
        "Women-Dresses": [],
        "Women-Top": [],
        "Women-Tshirt": [],
        "Women-Jeans": [],
        "Women-Trousers": [],
        "Women-Shorts": [],
        "Women-Playsuit": [],
        "Women-Shrug": [],
        "Women-Sweater": [],
        "Women-Overcoat": [],
        "Women-Blazer": []
    }

    current_directory = os.getcwd()
    women_categories_directory = os.path.join(current_directory, 'Women-Categories')

    if not os.path.exists(women_categories_directory):
        print("Men-Categories directory does not exist.")
        return

    folders = [f for f in os.listdir(women_categories_directory) if os.path.isfile(os.path.join(women_categories_directory, f))]

    for folder in folders:
        if any(keyword in folder for keyword in krtansuits_keywords):
            categorized_folders["Women-Kurta-Suits"].append(folder)
        elif any(keyword in folder for keyword in kurti_tunic_keywords):
            categorized_folders["Women-Kurti-Tunic"].append(folder)
        elif any(keyword in folder for keyword in saree_keywords):
            categorized_folders["Women-Saree"].append(folder)
        elif any(keyword in folder for keyword in nightsuits_keywords):
            categorized_folders["Women-Night-Suit"].append(folder)
        elif any(keyword in folder for keyword in leggings_salwar_keywords):
            categorized_folders["Women-Legging-Salwar"].append(folder)
        elif any(keyword in folder for keyword in skirt_keywords):
            categorized_folders["Women-Skirt-Plazzos"].append(folder)   
        elif any(keyword in folder for keyword in dressmaterial_keywords):
            categorized_folders["Women-DressMaterials"].append(folder) 
        elif any(keyword in folder for keyword in lehenga_keywords):
            categorized_folders["Women-Lehenga"].append(folder)
        elif any(keyword in folder for keyword in dupattanshawl_keywords):
            categorized_folders["Women-Dupatta-Shawl"].append(folder)
        elif any(keyword in folder for keyword in womenjackets_keywords):
            categorized_folders["Women-Jackets"].append(folder)
        elif any(keyword in folder for keyword in dresses_keywords):
            categorized_folders["Women-Dresses"].append(folder)
        elif any(keyword in folder for keyword in top_keywords):
            categorized_folders["Women-Top"].append(folder)
        elif any(keyword in folder for keyword in tshirt_keywords):
            categorized_folders["Women-Tshirt"].append(folder)
        elif any(keyword in folder for keyword in womenjeans_keywords):
            categorized_folders["Women-Jeans"].append(folder)
        elif any(keyword in folder for keyword in womentrousers_keywords):
            categorized_folders["Women-Trousers"].append(folder)
        elif any(keyword in folder for keyword in shorts_keywords):
            categorized_folders["Women-Shorts"].append(folder)
        elif any(keyword in folder for keyword in playsuit_keywords):
            categorized_folders["Women-Playsuit"].append(folder)
        elif any(keyword in folder for keyword in shrug_keywords):
            categorized_folders["Women-Shrug"].append(folder)
        elif any(keyword in folder for keyword in sweater_keywords):
            categorized_folders["Women-Sweater"].append(folder)
        elif any(keyword in folder for keyword in overcoat_keywords):
            categorized_folders["Women-Overcoat"].append(folder)
        elif any(keyword in folder for keyword in blazer_keywords):
            categorized_folders["Women-Blazer"].append(folder)

    # Create directories for each category and move folders
    for category, items in categorized_folders.items():
        category_path = os.path.join(women_categories_directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
        for item in items:
            shutil.move(os.path.join(women_categories_directory, item), os.path.join(category_path, item))

    # Print the result
    for category, items in categorized_folders.items():
        print(f"{category}:")
        for item in items:
            print(f"  - {item}")
# Call the function
# categorize_images()
# women_categorize_images()
# men_categorize_images()