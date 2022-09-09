import datetime
import json
import pprint
import sys
from exif import Image
from pathlib import Path


def main(folder_name):
    img_files = Path(folder_name).glob('*.img')

    for img_file in img_files:
        with open(img_file, 'rb') as file_for_meta, open(f'{img_file.name}.json', 'r') as json_with_meta:
            img = Image(file_for_meta)
            print(img.list_all())  # Show all meta fields
            # img.set(attribute=attribute, value=value)  # example how to set meta
            metadata = json.load(json_with_meta)
            pprint.pprint(metadata)
            for meta in metadata:
                img.set(meta, metadata.get(meta, ''))

        # Write image with modified EXIF metadata to an image file
        with open(f'{folder_name}/modified/{img_file}', 'wb') as new_image_file:
            new_image_file.write(img.get_file())


if __name__ == '__main__':
    start = datetime.datetime.now()
    # directory = sys.argv[0]
    directory = r''
    main(directory)
    end = datetime.datetime.now()
    print(f'Total time: {start - end}')
