class Plugin:
    loadable = False
    
    @staticmethod
    def configure():
        options = {}
        apikey = raw_input('Enter Google API Key: ')
        while not apikey:
            apikey = raw_input('Enter Google API Key: ')
        options['api-key'] = apikey
        return options