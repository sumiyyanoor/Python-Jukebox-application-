from library_item import LibraryItem


def test_name_is_stored():
    item = LibraryItem("Song A", "Artist A", 4)
    assert item.name == "Song A"


def test_artist_is_stored():
    item = LibraryItem("Song B", "Artist B", 3)
    assert item.artist == "Artist B"


def test_default_play_count_is_zero():
    item = LibraryItem("Song C", "Artist C", 2)
    assert item.play_count == 0


def test_stars_returns_correct_number_of_stars():
    item = LibraryItem("Song D", "Artist D", 5)
    assert item.stars() == "*****"


def test_info_returns_expected_format():
    item = LibraryItem("Song E", "Artist E", 3)
    assert item.info() == "Song E - Artist E ***"
