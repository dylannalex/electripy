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

    def add_charge(self, charge: PointCharge):
        self.charges.append(charge)
        self._update_groups()

    def _update_groups(self):
        self.groups = []
        for charge in self.charges:
            self.groups.append(
                [
                    charge,
                    ChargesSet([c for c in self.charges if c is not charge]),
                ]
            )

    def get_electric_forces(self):
        """
        Returns a list of electric forces. There is one electric force for
        each charge in charges. Each electric force is a two dimensional
        vector. The first element is the charge and the second element is
        the electric force the other charges make on it.
        """
        electric_fields = []
        for group in self.groups:
            electric_fields.append(
                [
                    group[0],
                    group[1].electric_field(group[0].possition) * group[0].charge,
                ]
            )
        return electric_fields

    def __len__(self):
        return len(self.charges)
