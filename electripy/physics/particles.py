from numpy import array, ndarray
from numpy.linalg import norm
from electripy.physics.constants import COULOMB_CONST
from typing import Union


class PointParticle:
    def __init__(
        self,
        charge: Union[float, int],
        possition: ndarray,
    ):
        """
        charge: particle charge in coulomb.
        possition: particle two-dimensional vector in meters.
        """
        self.charge = charge
        self.possition = array(possition)

    def electric_field(self, point: ndarray):
        r_vector = array(self.possition - point)
        r_norm = norm(r_vector)
        return COULOMB_CONST * array(r_vector * (self.charge / r_norm ** 3)) * -1


class ParticleSet:
    def __init__(self, particles: list[PointParticle]):
        self.particles = particles

    def electric_field(self, point: ndarray):
        """
        Returns the electric field at the specified point.
        """
        ef = array([0.0, 0.0])
        for particle in self.particles:
            ef += particle.electric_field(point)
        return ef

    def force(self, particle: PointParticle):
        """
        Returns the force of the electric field exerted
        on the particle.
        """
        ef = self.electric_field(particle.possition)
        return ef * particle.charge
