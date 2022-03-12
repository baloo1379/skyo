class Bar():
    label: str
    value: int

class Chart():
    title: str
    bars: list[Bar]

    def __init__(self, title: str, values: list[int]):
        self.title = title
        if(type(values[0]) is int):
            self.bars = self.histogram(values)
        elif(type(values[0]) is bool):
            self.bars = self.pie(values)

    def histogram(self, values: list[int]) -> list[Bar]:
        values.sort()
        mn = min(values)
        mx = max(values)
        step = int((mx - mn)/10)
        result = list()
        for i in range(mn, mx, step):
            bar = Bar()
            bar.label = "(" + str(i) + "," + str(i + step - 1) + ")"
            bar.value = 0
            for v in values:
                if(i < v < i + step - 1):
                    bar.value += 1
            result.append(bar)
        return result
    
    def pie(self, values: list[bool]) -> list[Bar]:
        bar1 = Bar()
        bar1.label = "true"
        bar1.value = values.count(True)
        bar2 = Bar()
        bar2.label = "false"
        bar2.value = values.count(False)
        return list([bar1, bar2])