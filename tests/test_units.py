import unittest

from app.core.units import (
    ft_to_m,
    g_cm3_to_kg_m3,
    kg_m3_to_g_cm3,
    m_to_ft,
    mpa_to_psi,
    ppg_to_sg,
    psi_to_mpa,
    sg_to_ppg,
)


class UnitConversionTests(unittest.TestCase):
    def test_depth_roundtrip(self):
        self.assertAlmostEqual(ft_to_m(m_to_ft(1234.5)), 1234.5)

    def test_density_roundtrip(self):
        self.assertAlmostEqual(kg_m3_to_g_cm3(g_cm3_to_kg_m3(2.35)), 2.35)

    def test_pressure_roundtrip(self):
        self.assertAlmostEqual(psi_to_mpa(mpa_to_psi(42.0)), 42.0)

    def test_mud_weight_roundtrip(self):
        self.assertAlmostEqual(ppg_to_sg(sg_to_ppg(1.2)), 1.2)


if __name__ == "__main__":
    unittest.main()

