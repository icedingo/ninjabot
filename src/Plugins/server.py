class Plugin:
    loadable = False
    
    @staticmethod
    def configure():
        options = {}
        host = raw_input('Enter IRC server address: ')
        while not host:
            host = raw_input('Enter IRC server address: ')
        options['host'] = host
        
        while not False:
            port = raw_input('Enter IRC server port: ')
            try:
                port = int(port)
            except ValueError:
                continue
            break
        options['port'] = int(port)

        channel = raw_input('Enter IRC channel: ')
        while not channel:
            channel = raw_input('Enter IRC channel: ')
        options['channel'] = channel
        return options