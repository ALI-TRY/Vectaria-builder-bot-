# Vectaria Builder Bot - Castle Planner

def build_castle(width, height):
    print("🏰 بدء بناء القصر...")
    
    for floor in range(height):
        print(f"بناء الطابق {floor+1}")
        
    print("🛡️ تم الانتهاء من القصر!")

def build_big_city():
    print("🏙️ بناء مدينة كبيرة...")
    
    buildings = [
        "قصر ملكي",
        "برج عالي",
        "بيت كبير",
        "سور المدينة"
    ]

    for b in buildings:
        print("يبني:", b)

    print("✅ انتهى البناء")

build_castle(50, 10)
build_big_city()
