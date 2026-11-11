import unittest  #imports unittest module to run the tests

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover("tests", top_level_dir=".")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
    #devuelve true si todos los tests pasaron, false si alguno fallo.