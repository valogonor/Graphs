import random


def fisher_yates_shuffle(l):
        for i in range(0, len(l) - 2):
            random_index = random.randint(i, len(l) - 1)
            swap = l[random_index]
            l[random_index] = l[i]
            l[i] = swap


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        if numUsers <= avgFriendships:
            print("WARNING: The average number of friendships must be less than the number of users.")
        # Add users
        else:
            users = [i for i in range(1, numUsers+1)]
            for user in users:
                self.addUser(user)
            # Create friendships
            friendships = []
            for user in users:
                for user2 in users:
                    if user < user2 and user != user2:
                        friendships.append((user, user2))
            fisher_yates_shuffle(friendships)
            for i in range(numUsers * avgFriendships // 2):
                self.addFriendship(friendships[i][0], friendships[i][1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = []
        q.append([userID])
        while len(q) > 0:
            path = q.pop(0)
            v = path[-1]
            if v not in visited:
                visited[v] = path
                for friend in self.friendships[v]:
                    path_copy = [*path]
                    path_copy.append(friend)
                    q.append(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
