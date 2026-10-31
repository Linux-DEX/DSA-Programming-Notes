from pub_sub import PubSub


def main():
    bus = PubSub()
    seen = []

    def remember(message):
        seen.append(("orders", message))

    def ignore(message):
        seen.append(("other", message))

    bus.subscribe("orders", remember)
    bus.subscribe("billing", ignore)
    bus.publish("orders", {"id": 7})
    bus.unsubscribe("orders", remember)
    bus.publish("orders", {"id": 8})
    bus.publish("billing", {"id": 9})

    print("seen:", seen)
    assert seen == [("orders", {"id": 7}), ("other", {"id": 9})]


if __name__ == "__main__":
    main()
