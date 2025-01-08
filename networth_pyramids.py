#!/bin/env python3

from datetime import datetime
from typing import NamedTuple

oldest_pyramid = -2667  # https://www.oldest.org/structures/pyramids/
hourly_rate = 250


class Person(NamedTuple):
    name: str
    networth: int


person = Person(
    "Elon Musk",
    429_800_000_000,  # December 2024 https://www.wiwo.de/erfolg/trends/forbes-liste-2024-das-sind-die-reichsten-menschen-der-welt-im-aktuellen-ranking-/26281100.html
)
now = datetime.now()
years = now.year - oldest_pyramid
days = years * 365.2425 + now.timetuple().tm_yday
hours = days * 24 + now.hour
income = hours * hourly_rate
percentage = income / person.networth

print(
    f"Wenn du seit bestehen der ersten Pyramide ({abs(oldest_pyramid)} v. Chr.) jede Stunde {hourly_rate} $ bekommen "
    f"hättest ohne je was davon auszugeben, dann besäßest du jetzt {percentage *100:.1f} % vom Vermögen von {person.name}."
)

twitter_cost = 44_000_000_000
print(
    f"Und dir würden noch {(twitter_cost - income) // 1_000_000_000} Mrd $ fehlen um Twitter zu kaufen "
    f"(Elon Musk hat Oktober 2022 {twitter_cost // 1_000_000_000} Mrd $ bezahlt)"
)
