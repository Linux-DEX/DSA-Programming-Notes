from load_balancer import LoadBalancer, Server


def main():
    servers = [Server("a", 1), Server("b", 3)]
    balancer = LoadBalancer(servers)

    robin = [balancer.pick("round_robin").name for _ in range(4)]
    weighted = [balancer.pick("weighted").name for _ in range(4)]
    print("round robin:", robin)
    print("weighted:", weighted)
    assert robin == ["a", "b", "a", "b"]
    assert weighted == ["a", "b", "b", "b"]

    first = balancer.acquire("least_connections")
    second = balancer.acquire("least_connections")
    print("least connections:", first.name, second.name)
    print("counts:", [(server.name, server.connections) for server in servers])
    assert first.name == "a"
    assert second.name == "b"
    balancer.release(first)
    again = balancer.acquire("least_connections")
    print("after release:", again.name)
    assert again.name == "a"


if __name__ == "__main__":
    main()
