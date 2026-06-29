# 🏰 Vectaria Castle Builder Bot - Full Plan

castle = {
    "name": "القصر الملكي",
    "width": 40,
    "length": 32,
    "floors": 2,
    "towers": 4
}

build_commands = []


def add_block(x, y, z, block):
    build_commands.append(
        f"ضع {block} في X:{x} Y:{y} Z:{z}"
    )


def build_foundation():
    print("🧱 بناء الأساس")

    for x in range(castle["width"]):
        for z in range(castle["length"]):
            add_block(x, 0, z, "حجر")


def build_walls():
    print("🏰 بناء الجدران")

    for y in range(1, 8):

        for x in range(castle["width"]):
            add_block(x, y, 0, "حجر")
            add_block(x, y, castle["length"], "حجر")

        for z in range(castle["length"]):
            add_block(0, y, z, "حجر")
            add_block(castle["width"], y, z, "حجر")


def build_towers():
    print("🗼 بناء الأبراج")

    places = [
        (0,0),
        (40,0),
        (0,32),
        (40,32)
    ]

    for x,z in places:
        for y in range(1,15):
            add_block(x,y,z,"برج")


def build_rooms():
    print("🛏️ تجهيز الغرف")

    rooms = [
        "قاعة العرش",
        "غرفة النوم",
        "المكتبة",
        "غرفة الطعام"
    ]

    for room in rooms:
        print("✅", room)


def start_build():
    print("👑 بدء بناء:", castle["name"])
    print("📏 الحجم:", castle["width"], "x", castle["length"])

    build_foundation()
    build_walls()
    build_towers()
    build_rooms()

    print("\n🎉 القصر جاهز كمخطط!")
    print("عدد أوامر البناء:", len(build_commands))


start_build()
