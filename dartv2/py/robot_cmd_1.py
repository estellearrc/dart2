import dartv2b
import time


"""
Notes:
to do a turn: 2.5s
"""


def test_Q4(mybot, delta_t):
    t0 = time.time()
    while (time.time()-t0 < delta_t):
        mybot.set_speed(100, 100)
        time.sleep(1)
    delta_t_turn = 1.1
    t0 = time.time()
    while (time.time()-t0 < delta_t_turn):
        print("u tuuuuuuuuuuuuuuuuuurn")
        mybot.set_speed(100, -100)
        time.sleep(1)
    t0 = time.time()
    while (time.time()-t0 < delta_t):
        mybot.set_speed(100, 100)
        time.sleep(1)
    delta_t_turn = 0.8
    t0 = time.time()
    while (time.time()-t0 < delta_t_turn):
        mybot.set_speed(100, -100)
        time.sleep(1)


def main():
    mybot = dartv2b.DartV2()
    t0 = time.time()
    dt = 0.1
    delta_t = 5
    # while (time.time()-t0 < delta_t):
    #     mybot.set_speed(100,-100)
    #     # diff = mybot.delta_front_odometers(dt)
    #     print("time: ",time.time()-t0)
    test_Q4(mybot, delta_t)
    mybot.end()


if __name__ == "__main__":
    main()
