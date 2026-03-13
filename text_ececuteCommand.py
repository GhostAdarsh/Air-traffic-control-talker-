class VoiceControl:
    
    def __init__(self, pathfinder, holding_points):

        # pathfinder object from your simulator
        self.pathfinder = pathfinder

        # holding points dictionary
        self.valid_holding_points = holding_points


    # ----------------------------------------------------
    # MAIN CONTROL FUNCTION
    # ----------------------------------------------------
    def process_voice(self, planes):

        # temporary test input (replace with real voice later)
        text = "speedbird one two three taxi horka"

        print("Input text:", text)

        command = self.parse_command(text)

        print("Parsed command:", command)

        self.execute_command(command, planes)


    # ----------------------------------------------------
    # PARSE SPEECH INTO COMMAND
    # ----------------------------------------------------
    def parse_command(self, text):

        number_map = {
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }

        text = text.lower().strip()
        words = text.split()

        command = {
            "callsign": None,
            "action": None,
            "destination": None,
            "runway": None
        }

        # -----------------------
        # CALLSIGN PARSING
        # -----------------------
        for i, word in enumerate(words):

            if word == "speedbird":

                number = ""
                j = i + 1

                while j < len(words) and words[j] in number_map:
                    number += number_map[words[j]]
                    j += 1

                if number != "":
                    command["callsign"] = "speedbird" + number
                    break


        # -----------------------
        # ACTION PARSING
        # -----------------------
        if "taxi" in words:
            command["action"] = "taxi"

        elif "takeoff" in words:
            command["action"] = "takeoff"

        elif "hold" in words:
            command["action"] = "hold"


        # -----------------------
        # RUNWAY PARSING
        # -----------------------
        if "runway" in words:

            index = words.index("runway")

            if index + 2 < len(words):

                first = words[index + 1]
                second = words[index + 2]

                if first in number_map and second in number_map:

                    command["runway"] = number_map[first] + number_map[second]


        # -----------------------
        # HOLDING POINT / DESTINATION
        # -----------------------
        for point, coords in self.valid_holding_points.items():

            if point.lower() in words:

                command["destination"] = coords
                break


        return command


    # ----------------------------------------------------
    # EXECUTE COMMAND
    # ----------------------------------------------------
    def execute_command(self, command, planes):

        callsign = command["callsign"]
        action = command["action"]

        if callsign is None or action is None:
            print("Invalid command")
            return


        for plane in planes:

            if plane.callsign != callsign:
                continue


            print("Plane matched:", plane.callsign)


            # -----------------------
            # TAXI COMMAND
            # -----------------------
            if action == "taxi":

                destination = command["destination"]

                if destination is None:
                    print("No destination found")
                    return


            # -----------------------
            # TAKEOFF COMMAND
            # -----------------------
            elif action == "takeoff":

                runway_coords = {
                    "27": (41, 38),
                    "09": (68, 43)
                }

                runway = command["runway"]

                if runway is None:
                    runway = "27"

                destination = runway_coords.get(runway)


            else:
                print("Unknown action")
                return


            # -----------------------
            # CREATE PATH
            # -----------------------
            path = self.pathfinder.create_path(
                plane.grid_position,
                destination
            )


            if not path:
                print("No path found")
                return


            # -----------------------
            # SET PLANE PATH
            # -----------------------
            plane.set_path(path)

            print("Path assigned:", path)

holding_points = {}
pathfinder = None 

voice = VoiceControl(pathfinder, holding_points)
planes = ["speedbird123", (0,0)]
voice.process_voice()