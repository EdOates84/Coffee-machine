class CoffeeMachine:
    def __init__(self, input_data):
        self._n = input_data["machine"]["outlets"]
        self.BEV = input_data["machine"]["beverages"]
        self.AVAL = input_data["machine"]["total_items_quantity"]


    def _checkForOne(self):
        for key in self.BEV.keys():
            ok = True
            is_aval = True
            for bev_key in self.BEV[key]:
                if bev_key not in self.AVAL.keys():
                    print("{} cannot be prepared because {} is not available".format(key, bev_key))
                    ok = False
                    is_aval = False
                    break
                if self.BEV[key][bev_key] > self.AVAL[bev_key]:
                    ok = False
            if ok:
                for bev_key in self.BEV[key]:
                    self.AVAL[bev_key] = self.AVAL[bev_key] - self.BEV[key][bev_key]  
                print("{} is prepared".format(key))

            if (not ok) and is_aval:
                for bev_key in self.BEV[key]:
                    if self.BEV[key][bev_key] > self.AVAL[bev_key]:
                        print("{} cannot be prepared because {} is not sufficient".format(key, bev_key))
                        break


    def run(self):
        self._checkForOne()