#!/usr/bin/python
# -*- coding: cp1252 -*-
#################################################################
# Ethera
#Cozir Test Communication
#################################################################

import serial
import sys
import time
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),"../.."))

from CozirConfig import *
from GenericTools import *
from datetime import date
class CozirPortCom:
  def __init__(self, PortName = SERIAL_COM):
    try:
      self.portCom = serial.Serial()
      self.portCom.port = PortName
      self.portCom.baudrate = BAUD_RATE
      self.portCom.bytesize = DATA_BITS
      self.portCom.parity = PARITY
      self.portCom.stopbits = STOP_BITS
      self.portCom.xonxoff = XONXOFF
      self.portCom.timeout = READ_TIMEOUT
      self.portCom.WriteTimeout = WRITE_TIMEOUT
      self.portCom.interCharTimeout = INTERCHAR_TIMEOUT
      self.portCom.open()

    except KeyboardInterrupt:
      raise
    except Exception as MyExcept:
      raise GenericTools_Exception(MyExcept)

 def close(self):
  try:
    print("FTDI.close()")
    self.portCom.close()

    except KeyboardInterrupt:
      raise

    except Exception as MyExcept:
      raise GenericTools_Exception(MyExcept)
 
 def command(self, parameter, number=""):
  try:
    back=""
    if number!="":
      self.portCom.write(parameter[0:2]+str(number)+CRLF)
       back=self.portCom.read(REPONSE_DIX_OCTETS)
       print(back[0:8])
       return(back[3:8])
       else:
        self.portCom.write(parameter)
        back=self.portCom.read(REPONSE_DIX_OCTETS)
        print(back[0:8])
        return(back[3:8])
       except KeyboardInterrupt:
        raise

      except Exception as MyExcept:
        raise GenericTools_Exception(MyExcept)
 
 def commandNoPrint(self, parameter, number=""):
  try:
    back=""
    if number!="":
      self.portCom.write(parameter[0:2]+str(number)+CRLF)
      back=self.portCom.read(REPONSE_DIX_OCTETS)
      print(back[0:8])
      return(back[3:8])
     else:
      self.portCom.write(parameter)
      back=self.portCom.read(REPONSE_DIX_OCTETS)
      return(back[3:8])

    except KeyboardInterrupt:
      raise

    except Exception as MyExcept:
      raise GenericTools_Exception(MyExcept)

  def noZero (self, before):
    try:
      i=0
      for character in before:
        if character =='0':
          i+=1
        else:
          after=before[i:]
          return(after)
    except KeyboardInterrupt:
      raise

    except Exception as MyExcept:
      raise GenericTools_Exception(MyExcept)

if __name__=="__main__":
 try:
  com=CozirPortCom()
  nameDataFile=raw_input("Please give a name to your data file :")
  nameDataFile+=".csv"
  data=open(nameDataFile, "wb")
  com.command(SET_MODE, POLLING_MODE)
  filterCoef=input("Please give the digital filter value :")
  com.command(SET_FILTER_SETTING, filterCoef)
  data.write(time.strftime("%A %d %B %Y\n"))
  data.write("Valeurs mesurées par le capteur Cozir :\n")

  spentTime=0
  i=LOOP_NUMBER_FOR_SIX_SECONDS
  beghalf = time.time()
  beg = time.time()
  print("Blow in the Cozir sensor in :")
  while(spentTime <=SIX_SECONDS):
    end = time.time()
    if (end-beghalf)>=HALF_SECOND:
      if((i!=0) and (i%2==0)):
        print(i//2)
      beghalf = time.time()
      i-=1
      data.write(time.strftime("%H:%M:%S;"))
      data.write(com.noZero(str(com.commandNoPrint(GET_CO2_FILTERED)))+"\n")
      spentTime = end - beg
     print ("Blow !")

     while 1:
      end = time.time()
      if (end-beghalf)>=HALF_SECOND:
        beghalf = time.time()
        data.write(time.strftime("%H:%M:%S;"))
        data.write(com.noZero(str(com.command(GET_CO2_FILTERED)))+"\n")
 
except KeyboardInterrupt:
 print("Prg interrupted by Ctrl+C")

except Exception as MyExcept:
 print GenericTools_Exception(MyExcept)
 
finally:
 if("data" in locals()) is True:
  data.close()
