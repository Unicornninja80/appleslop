from __future__ import annotations

import random
import re

FUNNY_PREFIXES = [
    "Galactic",
    "Saucy",
    "Quantum",
    "Hyper",
    "Sassy",
    "Moody",
    "Sneaky",
    "Turbo",
    "Retro",
]

FUNNY_SUFFIXES = [
    "Apple Tickle",
    "Fruit Loop",
    "Core Memory",
    "Pie Bomb",
    "Peel Pal",
    "Scriptlet",
    "Crunch Byte",
    "Stem Sprint",
    "Juice Drop",
]


def funny_name(seed: int) -> str:
    rng = random.Random(seed)
    return f"{rng.choice(FUNNY_PREFIXES)} {rng.choice(FUNNY_SUFFIXES)}"


def funny_slug(seed: int) -> str:
    name = funny_name(seed).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", name).strip("-")
    return slug
