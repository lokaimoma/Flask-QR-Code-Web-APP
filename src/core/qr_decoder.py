# Created by Kelvin_Clark on 3/22/22, 5:31 PM
from typing import List, IO

from PIL import Image
from pyzbar.pyzbar import Decoded, decode
from werkzeug.datastructures import FileStorage


def decode_qr_code(image: str | IO[bytes] | FileStorage) -> List[Decoded]:
    """
    Decodes a qr code image given its file path, or a file object
    :param image: The image file path(string) or the image file object
    :return: :obj:`list` of :obj:`Decoded`: The values decoded from the qr code.
    """
    return decode(Image.open(image))
