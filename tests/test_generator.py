import pytest

from src.pin_generator_1_relduz_chloe import batch_generate_pin, is_valid


@pytest.mark.parametrize("batch_size", [1000, 1000, 1000, 5000])
def test_generator(batch_size: int):
    result = batch_generate_pin(batch_size)
    # Check if all unique
    assert len(result) == len(set(result)) == batch_size

    result_b = batch_generate_pin(batch_size)
    # Check if random set
    assert set(result) != set(result_b)


@pytest.mark.parametrize("batch_size", [0, 7154, 9999, 999999])
def test_generator_batch_larger_than_all_unique(batch_size: int):
    with pytest.raises(Exception) as exc_info:
        batch_generate_pin(batch_size, log=True)
    assert (
        str(exc_info.value) == "Invalid batch_size, must be positive interger not "
        "greater than 7152 (max number of unique valid pins)."
    )


def test_valid():
    def test_valid(pin):
        d = [int(i) for i in pin]
        identical = d[0] == d[1] or d[1] == d[2] or d[2] == d[3]
        consecutive = (d[3] - d[2] == 1 and d[2] - d[1] == 1) or (
            d[2] - d[1] == 1 and d[1] - d[0] == 1
        )
        return not (identical or consecutive)

    valid_pins = 0
    for num in range(10000):
        pin = f"{num:04d}"
        if is_valid(pin):
            valid_pins += 1
            assert test_valid(pin)
        else:
            assert not test_valid(pin)

    assert valid_pins == 7153
