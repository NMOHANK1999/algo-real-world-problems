from solutions.problem_07_trending_topics import TrendingTracker


def test_top_k_at_creation_time():
    tt = TrendingTracker(decay_half_life_seconds=60)
    tt.record_event("python", 0)
    tt.record_event("python", 0)
    tt.record_event("rust", 0)
    assert tt.top_k(2, now=0) == ["python", "rust"]


def test_decay_preserves_order():
    tt = TrendingTracker(decay_half_life_seconds=60)
    tt.record_event("python", 0)
    tt.record_event("python", 0)
    tt.record_event("rust", 0)
    assert tt.top_k(2, now=60) == ["python", "rust"]


def test_decay_can_flip_order():
    tt = TrendingTracker(decay_half_life_seconds=60)
    tt.record_event("old_topic", 0)
    tt.record_event("old_topic", 0)
    tt.record_event("old_topic", 0)
    tt.record_event("new_topic", 120)
    # old_topic: 3 events decayed 2 half-lives by now=120 -> weight 3*0.25=0.75
    # new_topic: 1 fresh event -> weight 1.0
    assert tt.top_k(1, now=120) == ["new_topic"]


def test_alphabetical_tiebreak():
    tt = TrendingTracker(decay_half_life_seconds=60)
    tt.record_event("zeta", 0)
    tt.record_event("alpha", 0)
    assert tt.top_k(2, now=0) == ["alpha", "zeta"]
