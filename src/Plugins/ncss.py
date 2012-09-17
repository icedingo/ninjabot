class Plugin:
    loadable = False
    
    @staticmethod
    def configure():
        options = {}
        cookie = raw_input('Enter NCSS Challenge session cookie: ')
        while not cookie:
            cookie = raw_input('Enter NCSS Challenge session cookie: ')
        options['cookie'] = cookie
        while not False:
            course = raw_input('Enter NCSS Challenge course id: ')
            try:
                course = int(course)
            except ValueError:
                continue
            break
        options['course'] = int(course)

        return options