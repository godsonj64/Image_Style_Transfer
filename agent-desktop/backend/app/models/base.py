from __future__ import annotations

from typing import Protocol


class ModelAdapter(Protocol):
    name: str

    async def generate(self, prompt: str) -> dict: ...

    async def embed(self, texts: list[str]) -> list[list[float]]: ...
