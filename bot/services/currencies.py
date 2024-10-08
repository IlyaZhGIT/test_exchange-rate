import aiohttp
import xml.etree.ElementTree as ET

from core.logger import logger


async def get_exchange_rate(char_code_currency: str) -> str | None:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.cbr.ru/scripts/XML_daily.asp") as response:
            root = ET.fromstring(await response.text())
            try:
                return root.find(
                    f"./Valute[CharCode='{char_code_currency}']/Value"
                ).text  # type: ignore
            except Exception as e:
                logger.warning(
                    f"Ошибка при выполнении запроса! error={e}; {response=}; {char_code_currency=}; "
                )
                return None
