def has_consecutive_identical(pin: str) -> bool:
    return pin[0] == pin[1] or pin[1] == pin[2] or pin[2] == pin[3]


def is_incremental(pin: int) -> bool:
    # 111 * n + 11 + 1 is incremental except when n > 7
    return pin % 111 == 12 and pin // 111 <= 7


def is_valid(pin: str) -> bool:
    incremental = is_incremental(int(pin[:3])) or is_incremental(int(pin[1:]))
    return not incremental and not has_consecutive_identical(pin)
