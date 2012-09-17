class Plugin:
    loadable = False

    @staticmethod
    def configure():
        options = {}

        messages = {'nick': 'Enter bot nick: ',
                    'realname': 'Enter bot realname: ',
                    'quit-message':'Enter quit message: ',
                    'trigger-prefix':'Enter trigger prefix: ',
                    'admins':'Enter admin nicks (space separated): '}

        for opt in messages:
            ans = raw_input(messages[opt])
            while not ans:
                ans = raw_input(messages[opt])
            options[opt] = ans

        return options