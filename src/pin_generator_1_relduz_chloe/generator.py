import time
import random

from .validity import is_valid

generated_pins: dict[int, bool]


def generate_pin() -> str:
    randint = random.randint(0, 9999)
    # add 0 padding
    pin = f"{randint:04d}"

    if randint not in generated_pins:
        # store invalid pins too so we don't need to validate again
        generated_pins[randint] = True
        if is_valid(pin):
            return pin

    return generate_pin()


def batch_generate_pin(batch_size: int = 1000, log: bool = False) -> list[str]:
    """
    Generate [batch_size] 4 digit pins where:
    * 2 consecutive digits should not be the same
    * 3 consecutive digits should not be incremental.
    :param batch_size: number of pins generated
    :param log: log process time tracked
    :return: list of 4 digits pins as string
    """
    start = time.time()

    if batch_size < 1 or batch_size > 7153:
        raise ValueError(
            "Invalid batch_size, must be positive interger not "
            "greater than 7152 (max number of unique valid pins)."
        )

    global generated_pins
    generated_pins = {}
    pins = []
    for _ in range(batch_size):
        pins.append(generate_pin())

    if log:
        generating_time = (time.time() - start) * 1000
        print(f"Generated {batch_size} pins in {generating_time:.4f} ms", end=", ")
        print(f"rate at {generating_time/batch_size:.4f} ms per pin")

    return pins
