from typing import Optional


class Valve:
    def __init__(self, line: str):
        self.name: Optional[str] = None
        self.flow_rate: Optional[int] = None
        self.neighbors: Optional[dict] = None
        self._from_string(line)

    def _from_string(self, line):
        first_str, second_str = line.split('; ')
        valve_str, flow_rate_str = first_str.split(' has ')
        self.name = valve_str.split()[1]
        self.flow_rate = int(flow_rate_str.split('=')[1])

        tunnel_str = second_str.split(' valve')[1]
        if tunnel_str[0] == 's':
            tunnel_str = tunnel_str[2:]
        else:
            tunnel_str = tunnel_str[1:]
        neighbors = tunnel_str.split(', ')
        self.neighbors = {neighbor: 1 for neighbor in neighbors}
