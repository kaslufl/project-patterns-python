from project_patterns import Skeleton


def test_skeleton_clone():
    skeleton_template = Skeleton(3, 0, 100)

    skeleton1 = skeleton_template.clone()
    skeleton2 = skeleton_template.clone()

    assert not skeleton1 == skeleton2
    assert skeleton1.hit_points == skeleton2.hit_points