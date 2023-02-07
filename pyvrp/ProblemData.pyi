from typing import Any, List, Tuple

class Client:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def demand(self) -> int: ...
    @property
    def release_time(self) -> int: ...
    @property
    def serv_dur(self) -> int: ...
    @property
    def tw_early(self) -> int: ...
    @property
    def tw_late(self) -> int: ...
    @property
    def x(self) -> int: ...
    @property
    def y(self) -> int: ...

class ProblemData:
    def __init__(
        self,
        coords: List[Tuple[int, int]],
        demands: List[int],
        nb_vehicles: int,
        vehicle_cap: int,
        time_windows: List[Tuple[int, int]],
        service_durations: List[int],
        duration_matrix: List[List[int]],
        release_times: List[int],
    ) -> None: ...
    def client(self, client: int) -> Client: ...
    def depot(self) -> Client: ...
    def dist(self, first: int, second: int) -> int: ...
    def distance_matrix(self, *args, **kwargs) -> Any: ...
    @staticmethod
    def from_file(where: str) -> ProblemData: ...
    @property
    def num_clients(self) -> int: ...
    @property
    def num_vehicles(self) -> int: ...
    @property
    def vehicle_capacity(self) -> int: ...