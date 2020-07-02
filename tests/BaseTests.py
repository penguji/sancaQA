from library.drivers import get_driver, quit_driver


class Base:
    driver = None

    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        print("=== Setup Class")
        cls.driver = get_driver()
        cls.driver.implicitly_wait(10)
        # Install app

    @classmethod
    def teardown_class(cls):
        """ teardown any state that was previously setup with a call to
        setup_class.
        """
        print("=== Teardown Class")
        # Delete app
        quit_driver()
