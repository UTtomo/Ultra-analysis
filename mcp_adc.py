import wiringpi as pi
import struct

class mcp3002:
    def __init__( self, ss, speed, vref ):
        self.ss = ss
        self.speed = speed
        self.vref = vref
        
        pi.wiringPiSPISetup( self.ss, self.speed )
        
    def get_value( self, ch ):
        senddata = 0x6800 |  ( 0x1800 * ch ) 
        buffer = struct.pack( '>h', senddata )
        pi.wiringPiSPIDataRW( self.ss , buffer )
        value = ( buffer[0] * 256 + buffer[1] ) & 0x3ff
        return value

    def get_volt( self, value ):
        return value * self.vref / float( 1023 )


class mcp3008:
    def __init__( self, ss, speed, vref ):
        self.ss = ss
        self.speed = speed
        self.vref = vref
        
        pi.wiringPiSPISetup( self.ss, self.speed )
        
    def get_value( self, ch ):
        cmd = 0xc0 | ( ch << 3 )
        buffer = cmd << 16
        buffer = buffer.to_bytes( 3, byteorder='big' )
        pi.wiringPiSPIDataRW( self.ss, buffer )
        value = (  buffer[0] << 16 | buffer[1] << 8 | buffer[2] )  >> 7
        return value

    def get_volt( self, value ):
        return value * self.vref / float( 1023 )


class mcp3204:
    def __init__( self, ss, speed, vref ):
        self.ss = ss
        self.speed = speed
        self.vref = vref
        
        pi.wiringPiSPISetup( self.ss, self.speed )
        
    def get_value( self, ch ):
        cmd = 0xc0 | ( ch << 3 )
        buffer = cmd << 24
        buffer = buffer.to_bytes( 4, byteorder='big' )
        pi.wiringPiSPIDataRW( self.ss, buffer )
        value = (  buffer[0] << 24 | buffer[1] << 16 | buffer[2] << 8 | buffer[2] )  >> 13
        return value

    def get_volt( self, value ):
        return value * self.vref / float( 4095 )


class mcp3208:
    def __init__( self, ss, speed, vref ):
        self.ss = ss
        self.speed = speed
        self.vref = vref
        
        pi.wiringPiSPISetup( self.ss, self.speed )
        
    def get_value( self, ch ):
        cmd = 0xc0 | ( ch << 3 )
        buffer = cmd << 24
        buffer = buffer.to_bytes( 4, byteorder='big' )
        pi.wiringPiSPIDataRW( self.ss, buffer )
        value = (  buffer[0] << 24 | buffer[1] << 16 | buffer[2] << 8 | buffer[2] )  >> 13
        return value

    def get_volt( self, value ):
        return value * self.vref / float( 4095 )

