def sort(width, height, length, mass) -> str:
    large_volume_threshold = 1_000_000
    large_dimension_threshold = 150
    heavy_weight_threshold = 20

    has_large_volume = width * length * height >= large_volume_threshold
    has_large_dimension = max(width, height, length) >= large_dimension_threshold
    is_bulky = has_large_volume or has_large_dimension

    is_heavy = mass >= heavy_weight_threshold

    if is_bulky and is_heavy:
        classification = "REJECTED"
    elif is_bulky or is_heavy:
        classification = "SPECIAL"
    else:
        classification = "STANDARD"

    return classification


def test():
    # not heavy or bulky
    assert sort(1, 1, 1, 1) == "STANDARD"

    # bulky due to volume, not heavy
    assert sort(100, 100, 100, 10) == "SPECIAL"

    # bulky due to dimension, not heavy
    assert sort(150, 10, 10, 1) == "SPECIAL"
    assert sort(10, 150, 10, 1) == "SPECIAL"
    assert sort(10, 10, 150, 1) == "SPECIAL"

    assert sort(1000, 10, 10, 1) == "SPECIAL"
    assert sort(10, 1000, 10, 1) == "SPECIAL"
    assert sort(10, 10, 1000, 1) == "SPECIAL"

    # heavy, not bulky
    assert sort(1, 1, 1, 10000) == "SPECIAL"
    assert sort(1, 1, 1, 20) == "SPECIAL"

    # heavy and bulky
    assert sort(100, 100, 100, 20) == "REJECTED"

    # air
    assert sort(0, 0, 0, 0) == "STANDARD"


test()
