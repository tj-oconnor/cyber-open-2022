import time
import math
import pickle
import random
import base64
import uuid


class Sweeper:

    def __init__(self,width,height,ratio):

        self.game_id = str(uuid.uuid4())
        self.width = width
        self.height = height
        self.board = [[{'mine':False,'cleared':False,'flagged':False,'nearby':0} for y in range(self.height)] for x in range(self.width)]
        self.num_mines = int(math.floor(width*height*ratio))
        self.unflagged_mines = self.num_mines
        self.flagged = 0
        self.place_mines(self.num_mines)
        self.game_over = False
        self.winner = False

    def place_mines(self,num_mines):
        #Randomly place mines on board
        for i in range(num_mines):
            #Loop until a valid position is found (with a sanity limit)
            for i in range(1000):
                x = random.choice(range(self.width))
                y = random.choice(range(self.height))
                if not self.board[x][y]["mine"]:
                    self.board[x][y]["mine"] = True
                    break

    def click_space(self,x,y):

        # If this is a mine and not flagged
        if self.board[x][y]["mine"] and not self.board[x][y]["flagged"]:
            self.game_over = True

        # Else uncover this space and recurse
        elif not self.board[x][y]["flagged"]:
            self.recursive_clear(x,y)

    def flag_space(self,x,y):
        self.board[x][y]["flagged"] = not self.board[x][y]["flagged"]

    def recursive_clear(self,x,y):

        # If this cell is already cleared
        if self.board[x][y]["cleared"]:
            return

        # Don't accidentally clear mines
        if self.board[x][y]["mine"]:
            return

        # Clear this space
        self.board[x][y]["cleared"] = True

        # If this space has no mines nearby then recurse to others
        if self.board[x][y]["nearby"] == 0:
            for dx in range(-1,2):
                    for dy in range(-1,2):
                        if x + dx < 0 or x + dx >= self.width:
                            continue
                        if y + dy < 0 or y + dy >= self.height:
                            continue
                        if dx == 0 and dy == 0:
                            continue
                        self.recursive_clear(x+dx,y+dy)

    def count_mines(self):
        
        all_mines = 0
        unflagged_mines = 0
        flagged = 0

        for x in range(self.width):
            for y in range(self.height):

                if self.board[x][y]["flagged"]:
                    flagged += 1
                
                if self.board[x][y]["mine"]:
                    if not self.board[x][y]["flagged"]:
                        unflagged_mines += 1
                    all_mines += 1
                    continue
                
                mines_adjacent = 0

                for dx in range(-1,2):
                    for dy in range(-1,2):

                        if x + dx < 0 or x + dx >= self.width:
                            continue

                        if y + dy < 0 or y + dy >= self.height:
                            continue

                        if dx == 0 and dy == 0:
                            continue

                        if self.board[x+dx][y+dy]["mine"] == True:
                            mines_adjacent += 1

                    # We only reveal nearby mines if this space is cleared
                    self.board[x][y]["nearby"] = mines_adjacent

        self.unflagged_mines = unflagged_mines
        self.num_mines = all_mines
        self.flagged = flagged

        if unflagged_mines == 0:
            self.game_over = True
            self.winner = True

    def get_game_state(self,sanitize=True):

        self.count_mines()

        if self.game_over:
            sanitize = False

        return {"game_id":self.game_id,
                "mines":self.num_mines,
                "flagged":self.flagged,
                "board":self.get_board_state(sanitize),
                "game_over":self.game_over,
                "winner":self.winner}

    def get_board_state(self,sanitize=True):

        #Show mine positions if game is over, debugging, etc
        if not sanitize:
            return self.board
        else:
            return [[{'cleared':self.board[x][y]['cleared'],
                      'flagged':self.board[x][y]['flagged'],
                      'nearby':self.board[x][y]['nearby'] if self.board[x][y]['cleared'] else 0} 
                      for y in range(self.height)] for x in range(self.width)]

    def dump_state(self):
        return base64.b64encode(pickle.dumps(self.get_game_state(False))).decode()

    def load_state(self,state):
        # Report unpickling exceptions back to user because we're nice.
        try:
            # Try to load provided pickle
            state = pickle.loads(base64.b64decode(state))
            self.game_id = state["game_id"]
            self.board = state["board"]
            self.width = len(self.board)
            self.height = len(self.board[0])
            self.game_over = state["game_over"]
            self.winner = state["winner"]

        except Exception as e:
            return "error",str(e)
        return "message","Game loaded successfully."

                
        


        

    