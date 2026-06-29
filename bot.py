# 🏰 Vectaria Castle Builder Bot

start_position = {
    "x": 9903,
    "y": 464,
    "z": 41195
}

castle = {
    "name": "القصر الملكي",
    "width": 40,
    "length": 32,
    "height": 10
}

blocks = []


def place_block(x, y, z, block):
    blocks.append({
        "block": block,
        "x": x,
        "y": y,
        "z": z
    })


def build_castle():

    print("🏰 بناء:", castle["name"])

    # الأرضية
    for x in range(castle["width"]):
        for z in range(castle["length"]):

            place_block(
                start_position["x"] + x,
                start_position["y"],
                start_position["z"] + z,
                "حجر"
            )


    # الجدران
    for y in range(1, castle["height"]):

        for x in range(castle["width"]):

            place_block(
                start_position["x"] + x,
                start_position["y"] + y,
                start_position["z"],
                "حجر"
            )


    # برج
    for y in range(1,15):

        place_block(
            start_position["x"],
            start_position["y"] + y,
            start_position["z"],
            "برج"
        )


    print("✅ القصر جاهز")
    print("عدد البلوكات:", len(blocks))


build_castle()
