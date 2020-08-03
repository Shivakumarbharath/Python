from abc import abstractmethod,ABC


class TouchScreen(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def Scroll(self):
        pass

    @abstractmethod
    def Click(self):
        pass


class Dell(TouchScreen):
    def __init__(self):
        TouchScreen.__init__(self)
        pass


    @abstractmethod
    def Scroll(self):
        pass

    def Click(self):
        pass


class HP(TouchScreen):
    def __init__(self):
        TouchScreen.__init__(self)
        pass

    @abstractmethod
    def Scroll(self):
        pass

    def Click(self):
        pass

class DellNote(Dell):
    def __init__(self):
        Dell.__init__(self)
        pass

    def Scroll(self):
        print(" Dell Scrolling")

    def Click(self):
        print(" Dell Button Clicked")


class HPNote(Dell):
    def __init__(self):
        HP.__init__(self)
        pass

    def Scroll(self):
        print(" HP Scrolling")

    def Click(self):
        print(" HP Button Clicked")




hp=HPNote()

dl=DellNote()


hp.Click()

hp.Scroll()

dl.Scroll()

dl.Click()