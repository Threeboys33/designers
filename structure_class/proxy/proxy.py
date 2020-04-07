#  代理模式
class Server:
    content = dict()

    def recv(self):
        pass

    def send(self):
        pass

    def show(self):
        pass


class InfoServer(Server):

    def recv(self, info):
        self.content = info
        return "recv OK!"

    def send(self, info):
        pass

    def show(self):
        print(f"SHOW:{self.content}")


class ServerProxy:
    pass


class InfoServerProxy(ServerProxy):
    server = None

    def __init__(self, server):
        self.server = server

    def recv(self,info):
        return self.server.recv()

    def show(self):
        self.server.show()


class WhiteInfoServerProxy(InfoServerProxy):
    white_list = []

    def recv(self, info):
        try:
            assert type(info) == dict
        except:
            return "info structure is not correct"
        addr = info.get('addr', 0)
        if not addr in self.white_list:
            return "Your address is not in the white list"
        else:
            content = info.get('content', "")
            return self.server.recv(content)

    def addWhite(self, addr):
        self.white_list.append(addr)

    def removeWhite(self, addr):
        self.white_list.remove(addr)

    def clearWhite(self):
        self.white_list=[]


if __name__ == '__main__':
    info_struct = dict()
    info_struct['addr'] = 10010
    info_struct['content'] = 'Hello World'
    info_server = InfoServer()
    info_server_proxy = WhiteInfoServerProxy(info_server)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()
    info_server_proxy.addWhite(10010)
    print(info_server_proxy.recv(info_struct))
    info_server_proxy.show()