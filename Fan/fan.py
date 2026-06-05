from fan_run import Fan

if __name__ == '__main__':

    fan1 = Fan()
    fan1.speed = Fan.FAST
    fan1.radius = 10.0
    fan1.color = "yellow"
    fan1.on = True

    fan2 = Fan()
    fan2.speed = Fan.MEDIUM
    fan2.radius = 5.0