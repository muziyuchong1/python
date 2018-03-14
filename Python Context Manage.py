class A:
    def __init__(self,tag):
        self.tag = tag
        print('A [{}]'.format(tag))
    
    def __enter__(self):
        print('[Enter {}]:分配A资源'.format(self.tag))
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('[Exit {}]:免费资源'.format(self.tag))
        if exc_tb is None:
            print('[Exit {}]:退出没有例外'.self.tag)
        else:
            print('[Exit {}]:异常推出了'.self.tag)
            return False
        
A(tag)
