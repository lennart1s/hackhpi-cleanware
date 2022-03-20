from typing import List, Any


class Algo:

    def __init__(self) -> None:
        pass

    def add_task(self, datacenter: str, value: int) -> bool:
        pass

    def delete_task(self, datacenter: str, value: int) -> bool:
        pass

    def add_datacenter(self,
                       datacenter: str,
                       kilowats: List[float],
                       racks: int,
                       ) -> bool:

        pass

    def status(self) -> List[Any]:
        pass
