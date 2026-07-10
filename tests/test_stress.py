import unittest

from app.core.stress import (
    effective_stress_mpa,
    hydrostatic_pore_pressure_mpa,
    vertical_stress_mpa,
)
from app.core.validation import ValidationError


class StressTests(unittest.TestCase):
    def test_vertical_stress_constant_density_benchmark(self):
        depth = [0.0, 1000.0, 2000.0, 3000.0, 4000.0]
        density = [2.30, 2.30, 2.30, 2.30, 2.30]

        sv = vertical_stress_mpa(depth, density)

        self.assertAlmostEqual(sv[-1], 90.22118, places=4)

    def test_hydrostatic_pore_pressure_benchmark(self):
        depth = [0.0, 1000.0, 2000.0, 3000.0, 4000.0]

        pp = hydrostatic_pore_pressure_mpa(depth, fluid_density_kg_m3=1000.0)

        self.assertAlmostEqual(pp[-1], 39.2266, places=4)

    def test_effective_stress_uses_biot_coefficient(self):
        result = effective_stress_mpa([90.0], [40.0], biot_alpha=1.0)

        self.assertEqual(result, [50.0])

    def test_vertical_stress_rejects_non_monotonic_depth(self):
        with self.assertRaises(ValidationError):
            vertical_stress_mpa([0.0, 1000.0, 900.0], [2.3, 2.3, 2.3])

    def test_vertical_stress_rejects_invalid_density(self):
        with self.assertRaises(ValidationError):
            vertical_stress_mpa([0.0, 1000.0], [2.3, 0.0])


if __name__ == "__main__":
    unittest.main()

