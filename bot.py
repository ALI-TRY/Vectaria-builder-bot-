# 🏰 Vectaria Castle Builder Bot

castle = {
    "name": "القصر الملكي",
    "width": 40,
    "length": 32,
    "height": 10
}

blocks = []


def place_block(x, y, z, block):
    blocks.append({
        "x": x,
        "y": y,
        "z": z,
        "block": block
    })


def build_castle():

    print("🏰 بدأ تجهيز القصر")

    # الأرضية
    for x in range(castle["width"]):
        for z in range(castle["length"]):
            place_block(x,0,z,"حجر")

    # الجدران
    for y in range(1, castle["height"]):

        for x in range(castle["width"]):
            place_block(x,y,0,"حجر")
            place_block(x,y,castle["length"],"حجر")

        for z in range(castle["length"]):
            place_block(0,y,z,"حجر")
            place_block(castle["width"],y,z,"حجر")


    print("🗼 إضافة الأبراج")

    towers = [
        (0,0),
        (40,0),
        (0,32),
        (40,32)
    ]

    for x,z in towers:
        for y in range(1,15):
            place_block(x,y,z,"برج")


    print("✅ القصر جاهز")
    print("عدد البلوكات:", len(blocks))


build_castle()
