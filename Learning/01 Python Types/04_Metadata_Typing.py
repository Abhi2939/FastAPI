from typing import Annotated

def say_hello(name: Annotated[str,"This is just a metadata"]) -> str:
    return f"Hello{name}"