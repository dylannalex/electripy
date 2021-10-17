from numpy import ndarray
from electripy.physics.charges import ChargesSet, PointCharge


class ChargeNetwork:
    def __init__(self):
        """
        There is one group for each charge in charges.
        Each group is a two dimensional vector. The first element is
        a charge, and the second element is the ChargeSet instance
        containing all charges in charges except the charge itself.
        """
        self.charges = []
        self.groups = []
        self.charges_set = ChargesSet([])

    def add_charge(self, charge: PointCharge) -> None:
        self.charges.append(charge)
        self.charges_set.charges = self.charges
        self._update_groups()

    def _update_groups(self) -> None:
        self.groups = []
        for charge in self.charges:
            self.groups.append(
                [
                    charge,
                    ChargesSet([c for c in self.charges if c is not charge]),
                ]
            )

    def get_electric_forces(self) -> list:
        """
        Returns a list of electric forces. There is one electric force for
        each charge in charges. Each electric force is a two dimensional
        vector. The first element is the charge and the second element is
        the electric force the other charges make on it.
        """
        electric_forces = []
        for group in self.groups:
            electric_forces.append([group[0], group[1].electric_force(group[0])])
        return electric_forces

    def get_electric_field(self, possition: ndarray):
        """
        Returns the electric force array at the given point.
        """
        return self.charges_set.electric_field(possition)

    def __len__(self):
        return len(self.charges)
