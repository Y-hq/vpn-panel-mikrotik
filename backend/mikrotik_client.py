class MikrotikClient:
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def is_configured(self):
        return all([self.host, self.port, self.username, self.password])

    def create_vpn_user(self, username, password):
        print(f"[Mikrotik] create user {username}")
        return True

    def disable_vpn_user(self, username):
        print(f"[Mikrotik] disable user {username}")
        return True

    def delete_vpn_user(self, username):
        print(f"[Mikrotik] delete user {username}")
        return True
