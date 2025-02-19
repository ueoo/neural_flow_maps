import taichi as ti


ti.init()

a = 1


@ti.kernel
def test():
    print(a)


@ti.kernel
def test_template(a: ti.template()):
    print(a)


test()  # will print 1
test_template(a)  # will also print 1
a = 2
test()  # will still print 1
test_template(a)  # will print 2

v = ti.Vector.field(8, float, shape=(4, 4, 8))
print(v.shape)
