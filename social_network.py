
class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        # Prevent duplicate friendships and self-friendships
        if friend != self and friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    def __init__(self):
        # Dictionary storing each person by name
        self.people = {}

    def add_person(self, name):
        # Prevent duplicate people
        if name in self.people:
            print(f"{name} already exists in the network!")
            return

        self.people[name] = Person(name)
        print(f"{name} added to the network.")

    def add_friendship(self, person1_name, person2_name):
        # Check if both people exist
        if person1_name not in self.people:
            print(
                f"Friendship not created. "
                f"{person1_name} doesn't exist!"
            )
            return

        if person2_name not in self.people:
            print(
                f"Friendship not created. "
                f"{person2_name} doesn't exist!"
            )
            return

        # Prevent a person from being friends with themselves
        if person1_name == person2_name:
            print("A person cannot be friends with themselves!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        # Prevent duplicate friendships
        if person2 in person1.friends:
            print(
                f"{person1_name} and {person2_name} "
                f"are already friends!"
            )
            return

        # Create a bidirectional friendship
        person1.add_friend(person2)
        person2.add_friend(person1)

        print(
            f"Friendship created between "
            f"{person1_name} and {person2_name}."
        )

    def print_network(self):
        print("\n===== SOCIAL NETWORK =====")

        if not self.people:
            print("The social network is empty.")
            return

        for person in self.people.values():
            if person.friends:
                friend_names = [
                    friend.name for friend in person.friends
                ]
                print(
                    f"{person.name} is friends with: "
                    f"{', '.join(friend_names)}"
                )
            else:
                print(f"{person.name} has no friends yet.")

        print("==========================\n")


def main():
    network = SocialNetwork()

    print("===== ADDING PEOPLE =====")

    network.add_person("Alex")
    network.add_person("Jordan")
    network.add_person("Morgan")
    network.add_person("Taylor")
    network.add_person("Casey")
    network.add_person("Riley")

    print("\n===== CREATING FRIENDSHIPS =====")

    network.add_friendship("Alex", "Jordan")
    network.add_friendship("Alex", "Morgan")
    network.add_friendship("Jordan", "Taylor")
    network.add_friendship("Morgan", "Casey")
    network.add_friendship("Taylor", "Riley")
    network.add_friendship("Casey", "Riley")
    network.add_friendship("Morgan", "Riley")
    network.add_friendship("Alex", "Taylor")

    # Print the completed network
    network.print_network()

    print("===== TESTING EDGE CASES =====")

    # Test friendship with a person who does not exist
    network.add_friendship("Jordan", "Johnny")

    # Test adding a duplicate person
    network.add_person("Alex")

    # Test adding a duplicate friendship
    network.add_friendship("Alex", "Jordan")

    # Test a person trying to befriend themselves
    network.add_friendship("Morgan", "Morgan")

    # Print the network again to confirm no unwanted changes
    network.print_network()


if __name__ == "__main__":
    main()




# Test your code here