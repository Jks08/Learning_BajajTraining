# Monkey patching means changing output at runtime by reassigning the method of original class with a new implementation. 

import test
def monkey_patch_func(self):
    print("Haha you have been monkey patched")

test.Test.func = monkey_patch_func
obj = test.Test()
obj.func()
