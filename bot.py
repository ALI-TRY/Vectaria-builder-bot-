# Vectaria Castle Builder Plan

castle = {
    "name": "القصر الملكي",
    "size": "40x32",
    "floors": 2,
    "rooms": [
        "قاعة العرش",
        "غرفة النوم",
        "المكتبة",
        "غرفة الطعام"
    ],
    "towers": 4
}


def show_build_plan():

    print("🏰", castle["name"])
    print("📏 الحجم:", castle["size"])
    print("🏢 الطوابق:", castle["floors"])

    print("\n🛏️ الغرف:")

    for room in castle["rooms"]:
        print("➡️", room)

    print("\n🗼 الأبراج:", castle["towers"])

    print("\n✅ المخطط جاهز للبناء")


show_build_plan()
