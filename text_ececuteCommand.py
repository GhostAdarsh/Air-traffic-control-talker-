import pathfinding 

class FakePathfinder: 

    def create_path(self, start, end): 

        print("start", start)
        print("end", end)
        
        return start, end 
class Plane: 
    def __init__(self, callsign, grid_position):
        self.callsign = callsign
        self.grid_position = grid_position
        self.path = [] 

    def set_path(self, path):

        self.path = path 
        print("path set", path)

class VoiceControl: 
    def __init__(self):
        
        self.pathfinder = None

        self.holding_points = {
            "horka": (10,20)
        }
    def execute_command(self, command, planes): 

        for plane in planes: 
            if plane.callsign == command["callsign"]: 
                destination = self.holding_points[command["destination"]]

                path = self.pathfinder.create_path(
                    plane.grid_position, 
                    destination
                )
                plane.set_path(path)

# TEST DATA: 

plane = Plane("speedbird12", (0,0))
planes = [plane]

command = {
    "callsign": "speedbird12",
    "action": "taxi", 
    "destination": "horka"
}

voice = VoiceControl()
voice.pathfinder = FakePathfinder()

voice.execute_command(command, planes)
