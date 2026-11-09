import track_library as lib


def test_get_name_returns_valid_track_name():
    assert lib.get_name("01") == "What a Wonderful World"


def test_get_name_returns_none_for_invalid_track():
    assert lib.get_name("99") is None


def test_get_rating_returns_expected_rating():
    assert lib.get_rating("04") == 1


def test_set_rating_changes_rating():
    original_rating = lib.get_rating("03")
    lib.set_rating("03", 5)
    assert lib.get_rating("03") == 5
    lib.set_rating("03", original_rating)


def test_increment_play_count_increases_count():
    original_play_count = lib.get_play_count("02")
    lib.increment_play_count("02")
    assert lib.get_play_count("02") == original_play_count + 1
