def assertAlmostEqualMatrices(tst, m1, m2, places, msg=None):
    tst.assertEqual(len(list(m1)), len(list(m2)))
    for i, _ in enumerate(m1):
        tst.assertEqual(len(list(m1)[i]), len(list(m2)[i]))
        for j, _ in enumerate(m1[i]):
            tst.assertAlmostEqual(m1[i][j], m2[i][j],
                                  places, '{0},{1}: {2}'.format(i, j, msg or 'no extra info'))
