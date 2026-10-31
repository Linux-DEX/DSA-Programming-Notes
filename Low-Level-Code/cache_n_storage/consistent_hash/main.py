from consistent_hash import ConsistentHashRing


def owners(ring, keys):
    return {key: ring.get_node(key) for key in keys}


def main():
    ring = ConsistentHashRing(virtual_nodes=64)
    for node in ("a", "b", "c"):
        ring.add_node(node)

    keys = [f"user-{i}" for i in range(12)]
    before = owners(ring, keys)
    print("before:", before)
    assert set(before.values()) <= {"a", "b", "c"}
    assert None not in before.values()

    ring.remove_node("b")
    after = owners(ring, keys)
    print("after removing b:", after)
    assert "b" not in after.values()

    moved = [key for key in keys if before[key] != after[key]]
    stayed = [key for key in keys if before[key] == after[key]]
    print("moved:", moved)
    print("stayed:", stayed)
    assert all(before[key] == "b" for key in moved)
    assert all(key in moved for key in keys if before[key] == "b")


if __name__ == "__main__":
    main()
