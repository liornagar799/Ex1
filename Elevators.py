import json

class Elevator():
 def _init_(self ,_id: int=0,_speed: int=0, _minFloor:int=0,_maxFloor:int=0,_closeTime: int=0, _openTime: int=0,_startTime: int=0, _stopTime: int=0)->None:
        self._id=_id
        self._speed=_speed
        self._minFloor=_minFloor
        self._maxFloor=_maxFloor
        self._closeTime=_closeTime
        self._openTime=_openTime
        self._startTime=_startTime
        self._stopTime=_stopTime



 def from_json(self, file_name):
      with open(file_name, "r") as fp:
        elev = json.load(fp)

      self._id = elev["_id"]
      self._speed = elev["_speed"]
      self._minFloor = elev["_minFloor"]
      self._maxFloor = elev["_maxFloor"]
      self._closeTime = elev["_closeTime"]
      self._openTime = elev["_openTime"]
      self._startTime = elev["_startTime"]
      self._stopTime = elev["_stopTime"]


