from solutions.problem_08_friend_circles import FriendCircles


def make_circles():
    fc = FriendCircles()
    fc.add_friendship("alice", "bob")
    fc.add_friendship("bob", "carol")
    fc.add_friendship("dave", "erin")
    return fc


def test_transitive_connection():
    fc = make_circles()
    assert fc.are_connected("alice", "carol") is True


def test_separate_circles_not_connected():
    fc = make_circles()
    assert fc.are_connected("alice", "dave") is False


def test_self_connected():
    fc = make_circles()
    assert fc.are_connected("alice", "alice") is True


def test_circle_size():
    fc = make_circles()
    assert fc.circle_size("alice") == 3
    assert fc.circle_size("dave") == 2
