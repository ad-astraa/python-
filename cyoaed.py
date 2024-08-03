class Room:
  def __init__(self, name, desc):
      self.name = name
      self.description = desc
      self.exits = {}
      self.items = []

  def set_exit(self, direction, room):
      self.exits[direction] = room

  def add_item(self, item):
      self.items.append(item)

  def remove_item(self, item):
      self.items.remove(item)

  def get_details(self):
      details = f"{self.name}\n\n{self.description}\n"
      details += "Exits: " + ", ".join(self.exits.keys()) + "\n"
      if self.items:
          details += "Items in the room: " + ", ".join([item.name for item in self.items]) + "\n"
      return details

class Item:
  def __init__(self, name, description, is_puzzle=False, required_item=None):
      self.name = name
      self.description = description
      self.is_puzzle = is_puzzle
      self.required_item = required_item

  def use(self, item):
      if self.is_puzzle and item.name == self.required_item:
          return True
      return False

class Player:
  def __init__(self):
      self.inventory = []

  def pick_up(self, item):
      self.inventory.append(item)

  def drop(self, item):
      self.inventory.remove(item)

  def has_item(self, item_name):
      return any(item.name == item_name for item in self.inventory)

  def get_inventory(self):
      if not self.inventory:
          return "You have no items in your inventory."
      return "Inventory: " + ", ".join([item.name for item in self.inventory])

class Game:
  def __init__(self):
      self.create_world()
      self.current_room = self.rooms["entrance"]
      self.player = Player()

  def create_world(self):
      self.rooms = {
          "entrance": Room("Entrance", "You are standing at the entrance of a dark cave."),
          "hall": Room("Hall", "A large hall with torches on the walls."),
          "chamber": Room("Chamber", "A mysterious chamber with strange inscriptions."),
          "treasure_room": Room("Treasure Room", "A room filled with gold and jewels.")
      }
      self.rooms["entrance"].set_exit("north", self.rooms["hall"])
      self.rooms["hall"].set_exit("south", self.rooms["entrance"])
      self.rooms["hall"].set_exit("east", self.rooms["chamber"])
      self.rooms["chamber"].set_exit("west", self.rooms["hall"])
      self.rooms["chamber"].set_exit("north", self.rooms["treasure_room"])
      self.rooms["treasue_room"].set_exit("south", self.rooms["chamber"])

      key = Item("key", "A small rusty key.")
      torch = Item("torch", "A burning torch.")
      puzzle_box = Item("puzzle box", "A box with intricate designs.", is_puzzle=True, required_item="key")

      self.rooms["entrance"].add_item(torch)
      self.rooms["hall"].add_item(puzzle_box)
      self.rooms["chamber"].add_item(key)

  def start(self):
      print("welcome hehe")
      print("Type 'help' for a list of commands.\n")
      while True:
          print(self.current_room.get_details())
          command = input("> ").strip().lower()
          if command in ["quit", "exit"]:
              print("ok bye.")
              break
          self.process_command(command)

  def process_command(self, command):
      if command == "help":
          self.show_help()
      elif command == "inventory":
          print(self.player.get_inventory())
      elif command.startswith("go "):
          self.move(command[3:])
      elif command.startswith("take "):
          self.take_item(command[5:])
      elif command.startswith("drop "):
          self.drop_item(command[5:])
      elif command.startswith("use "):
          self.use_item(command[4:])
      else:
          print("whats that")

  def show_help(self):
      print("Commands:")
      print("  go [direction] - Move in the specified direction (north, south, east, west).")
      print("  take [item] - PICK IT UP.")
      print("  drop [item] - DROP IT?.")
      print("  use [item] - USE??!.")
      print("  inventory - show invv.")
      print("  quit, exit - quit :P .")

  def move(self, directioon):
      if direction in self.current_room.exits:
          self.current_room = self.current_room.exits[direction]}
      else:
          print("not that wayy!!.")

  def   take_item(self, item_name)):
      item = next((item for item in self.current_room.items if item.name == item_name), None)
      if item:
          self.current_room.remove_item(item)
          self.player.pick_up(item)
          print(f"YOU PICKED UP {item_name}."
      else:
          print(f"THERES NO {item_name} SMH")

  def drop_item(self, item_name):
      item = next((ittem foritem in self.player.inventory if item.name == item_name), None)
      if item:
          self.player.drop(item)
          self.current_room.add_item(item
          print(f"You dropped the {item_name}.")
      else:
        
          print((f"You don't have a {item_name}.")

  def use_iitem(self, item_name):
      item = next((item for item in self.player.inventory if item.name == item_name), None)
      if item:
          puzzle = next((i for i in self.current_room.items if i.is_puzzle), None)
          if puzzle and puzzle.use(item):
              self.current_room.remove_item(puzzle)
              print(f"used {item_name} to solve it.")
          else:
              print(f"You can't use {item_name} here smh.")
      else:
          print(f"uh u domt have {item_name}.")

if __name__ == "__main__":
  game = Game(
  game.start()
