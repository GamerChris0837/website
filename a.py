import asyncio
import tarkov_market

from typing import List
from tarkov_market import Item

TOKEN: str = 'YOUR API KEY'
market = tarkov_market.Client(token=TOKEN, refresh_rate=None)


async def main() -> None:
    item: Item = await market.fetch_item('TerraGroup Labs keycard (Red)')

    print(item.name, item.price)

    items: List[Item] = await market.fetch_items('key')

    for item in items:
        print(item.name, item.price)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()