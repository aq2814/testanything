#coding=utf8

##########################################################################################
import os
import time
import multiprocessing
import ctypes

##########################################################################################
class MultiProcess(multiprocessing.Process):
    def __init__(self, mprun_break, p1, p2):
        multiprocessing.Process.__init__(self)
        self.mprun_break = mprun_break
        self.p1 = p1
        self.p2 = p2
    def run(self):
        try:
            cnt = 0
            while not self.mprun_break.value:
                print "[%s:%s] p1=%s,p2=%s" % (os.getpid(), cnt, self.p1, self.p2)
                time.sleep(1)
                cnt += 1
        finally:
            print "[%s] before terminate: p1=%s,p2=%s" % (os.getpid(), self.p1, self.p2)

##########################################################################################
def test():
    mps = list()
    mm = multiprocessing.Manager()
    mprun_break = mm.Value(ctypes.c_bool, False)
    for i in range(3):
        mp = MultiProcess(mprun_break, i,str(i))
        mp.daemon = True
        mps.append(mp)
    print ">>> in main before start!!!"
    for mp in mps:
        mp.start()

    time.sleep(3)
    # 아래의 terminate는 MultiProcess의 finally: 코드가 수행안됨
    # print ">>> in main before terminate!!!"
    # for mp in mps:
    #     mp.terminate()

    mprun_break.value = True
    print ">>> in main before join!!!"
    for mp in mps:
        mp.join()

    print ">>> Main Done!"

##########################################################################################
if __name__=='__main__':
    test()