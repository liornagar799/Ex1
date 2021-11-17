class Call:

    def __init__(self,str="",time:float=0,srcFloor:int=0,destFloor:int=0,status:int=0,assign:int=0) -> None:
        self.str=str
        self.time=time
        self.srcFloor=srcFloor
        self.destFloor=destFloor
        self.status=status
        self.assign=assign


    def __str__(self) -> str:
        return f"{self.str},{self.time},{self.srcFloor},{self.destFloor},{self.status},{self.assign}"
