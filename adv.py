from room import Room
from player import Player
from world import World


import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# --- Fill this out with directions to walk ---
# traversal_path = ['n', 'n']
traversal_path = []
seen = {}

reversed_directions = {'n':'s','s':'n','e':'w','w':'e'}
reversed_path = []


#start with current room and get its exits
seen[player.current_room.id] = player.current_room.get_exits()

# traverse the graph while the rooms seen are less than graph
while len(seen) < len(room_graph) -1:
	if player.current_room.id not in seen:
		
		seen[player.current_room.id] = player.current_room.get_exits()
		seen[player.current_room.id].remove(reversed_path[-1]) 
	
	
    # while the room has no more exits 
	while len(seen[player.current_room.id]) == 0:
		reversed = reversed_path.pop()
		traversal_path.append(reversed)
		player.travel(reversed)
	
	#go to first available exit
	movement = seen[player.current_room.id].pop()

	#update the path 
	traversal_path.append(movement)
	#update the reversed path 
	reversed_path.append(reversed_directions[movement])
	#update player movement
	player.travel(movement)

'''
def bfs(self, starting_vertex, destination_vertex):
    queue = Queue()
    # make a set for visited
    visited = set()
    # enqueue a path to the starting vertex 
    queue.enqueue([starting_vertex])
    # while the queue isnt empty
    while queue.size() > 0:
        # dequeue the next path
        current_path = queue.dequeue()
        # current_node is the last thing in the path
        current_node = current_path[-1]
        if current_node == destination_vertex:
            return current_path
        else:
            if current_node not in visited:
                visited.add(current_node)
                edges = self.get_neighbors(current_node)
                for edge in edges:
                    path_copy = list(current_path)
                    path_copy.append(edge)
                    queue.enqueue(path_copy)
'''

# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
