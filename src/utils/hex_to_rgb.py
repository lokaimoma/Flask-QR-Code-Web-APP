# Created by Kelvin_Clark on 3/14/22, 6:23 PM
def hex_to_rgb(hex_code: str) -> tuple[int, int, int]:
    hex_code = hex_code.strip().lower()
    if hex_code == "":
        return 0, 0, 0
    hex_code = hex_code.replace("#", "")
    hex_length = len(hex_code)
    if hex_length < 6:
        hex_code += hex_code[hex_length - 6:]
    elif hex_length > 6:
        hex_code = hex_code[:6]
    result = []
    for i in range(3):
        try:
            result.append(int(hex_code[2 * i:(i + 1) * 2], 16))
        except ValueError:
            result.append(0)
    return result[0], result[1], result[2]
