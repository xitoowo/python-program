import datetime
import sys
import aiofiles
import asyncio
import json
from pathlib import Path
from exif import Image


async def main(directory):
    pathlist = Path(directory).glob('*.img')

    # Iterate through all json files in the directory.
    for path in pathlist:
        # Read the contents of the json file.
        async with aiofiles.open(f'{directory}/{path.name}', mode='rb') as file_for_meta, \
                aiofiles.open(f'{directory}/{path.name}.json', mode='r') as meta_json:
            contents = await file_for_meta.read()
            meta_j = await meta_json.read()
            img = Image(contents)
            metadata = json.loads(meta_j)
            for meta in metadata:
                img.set(meta, metadata.get(meta, ''))

        async with aiofiles.open(f'{directory}/modified/{path.name}', mode='wb') as new_image_file:
            await new_image_file.write(img.get_file())

if __name__ == '__main__':
    start = datetime.datetime.now()
    # folder_name = sys.argv[0]
    folder_name = r''
    asyncio.run(main(folder_name))
    end = datetime.datetime.now()
    print(f'Total async time: {start - end}')
