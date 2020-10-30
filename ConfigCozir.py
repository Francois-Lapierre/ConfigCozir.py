#!/usr/bin/python
# -*- coding: cp1252 -*-
###############################################################
# Ethera
# Cozir Config
###############################################################

BAUD_RATE = 9600
DATA_BITS = 8
PARITY = 'N'
STOP_BITS = 1
READ_TIMEOUT = 0.300
XONXOFF = 0
WRITE_TIMEOUT = 0
INTERCHAR_TIMEOUT = None

GET_SPAN_CALIBRATION = "s\r\n"
GET_CO2_FILTERED = "Z\r\n"
SET_CALIBRATION_FRESH_AIR = "G\r\n"

SET_FILTER_SETTING = "A #####\r\n"
SET_MODE = "K #####\r\n"
SET_SPAN_CALIBRATION = "S #####\r\n"

CRLF = "\r\n"

COMMAND_MODE = 0
STREAMING_MODE = 1
POLLING_MODE = 2
SPAN_CODE = 8495
CO2_FIELD = 4
CO2_INIT_VALUE = 700

MASK_CO2_FILTERED = '2'

REPONSE_DIX_OCTETS = 10
REPONSE_SEIZE_OCTETS = 16

SERIAL_COM = "/dev/ttyAMA0"

SIX_SECONDS = 6
HALF_SECOND = 0.5
LOOP_NUMBER_FOR_SIX_SECONDS = 11
