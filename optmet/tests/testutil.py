def assertAlmostEqualMatrices(tst, m1, m2, places, msg=None):
    tst.assertEqual(len(m1), len(m2))
    for i, _ in enumerate(m1):
        tst.assertEqual(len(m1[i]), len(m2[i]))
        for j, _ in enumerate(m1[i]):
            tst.assertAlmostEqual(m1[i][j], m2[i][j], places, msg)
