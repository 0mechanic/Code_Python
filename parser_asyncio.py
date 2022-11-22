import asyncio                 # Даст нам async/await
import aiohttp                 # Для асинхронного выполнения HTTP запросов
import aiofiles                # Дла асинхронного выполнения операций с файлами
import concurrent.futures      # Позволяет создать новый процесс
from multiprocessing import cpu_count # Вернет количество ядер процессора
from bs4 import BeautifulSoup  # Для скрапинга страниц
from math import floor         # Поможет разделить запросы между ядрами CPU

async def get_and_scrape_pages(num_pages: int, output_file: str):
    async with \
    aiohttp.ClientSession() as client, \
    aiofiles.open(output_file, "a+", encoding="utf-8") as f:

        for _ in range(num_pages):
            async with client.get(
                    'https://en.wikipedia.org/wiki/Special:Random'
                ) as response:
                if response.status > 399:
                    response.raise_for_status()

                page = await response.text()
                soup = BeautifulSoup(page, features="html.parser")
                title = soup.find("h1").text

                await f.write(title + "\t")

        await f.write("\n")
