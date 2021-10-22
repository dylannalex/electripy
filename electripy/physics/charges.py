from numpy import array, ndarray
from numpy.linalg import norm
from electripy.physics import constants
from typing import Union


class PointCharge:
    def __init__(
        self,
        charge: Union[float, int],
        position: ndarray,
    ) -> None:
        """
        charge: electric charge in coulomb
        position: two-dimensional vector in meters
        """
        self.charge = charge
        self.position = array(position)

    def electric_field(self, point: ndarray) -> ndarray:
        """
        Returns the electric field at the specified point.
        """
        r_vector = array(self.position - point)
        r_norm = norm(r_vector)
        return (
            constants.COULOMB_CONST * array(r_vector * (self.charge / r_norm ** 3)) * -1
        )


class ChargesSet:
    """
    A ChargesSet instance is a group of charges. The electric
    field at a given point can be calculated as the sum of each
    electric field at that point for every charge in the charge
    set.
    """

    def __init__(self, charges: list[PointCharge]) -> None:
        self.charges = charges

    def electric_field(self, point: ndarray) -> ndarray:
        """
        Returns the electric field at the specified point.
        """
        ef = array([0.0, 0.0])
        for charge in self.charges:
            ef += charge.electric_field(point)
        return ef

    def electric_force(self, charge: PointCharge) -> ndarray:
        """
        Returns the force of the electric field exerted
        on the charge.
        """
        ef = self.electric_field(charge.position)
        return ef * charge.charge


class Electron(PointCharge):
    """
    An Electron instance is a PointCharge object which charge
    is -e, where e is the elementary charge (1.60218e-19).
    """

    def __init__(self, position: ndarray) -> None:
        self.charge = constants.ELEMENTARY_CHARGE * -1
        self.position = array(position)


class Proton(PointCharge):
    """
    A Proton instance is a PointCharge object which the charge
    is e, where e is the elementary charge (1.60218e-19).
    """

    def __init__(self, position: ndarray) -> None:
        self.charge = constants.ELEMENTARY_CHARGE
        self.position = array(position)
