import sys
sys.path.append('../')
import time
from CQRobot_ADS1115 import ADS1115
ADS1115_REG_CONFIG_PGA_6_144V        = 0x00 # 6.144V range = Gain 2/3
ADS1115_REG_CONFIG_PGA_4_096V        = 0x02 # 4.096V range = Gain 1
ADS1115_REG_CONFIG_PGA_2_048V        = 0x04 # 2.048V range = Gain 2 (default)
ADS1115_REG_CONFIG_PGA_1_024V        = 0x06 # 1.024V range = Gain 4
ADS1115_REG_CONFIG_PGA_0_512V        = 0x08 # 0.512V range = Gain 8
ADS1115_REG_CONFIG_PGA_0_256V        = 0x0A # 0.256V range = Gain 16
ads1115 = ADS1115()
#Set the IIC address
ads1115.setAddr_ADS1115(0x48)
#Sets the gain and input voltage range.
ads1115.setGain(ADS1115_REG_CONFIG_PGA_6_144V)

VREF = 5.0
analogBuffer = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
analogBufferTemp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
analogBufferIndex = 0
copyIndex = 0
averageVoltage = 0
tdsValue = 0
temperature = 25

def getMedianNum(iFilterLen):
	global analogBufferTemp
	bTemp = 0.0
	for j in range(iFilterLen-1):
		for i in range(iFilterLen-j-1):
			if analogBufferTemp[i] > analogBufferTemp[i+1]:
				bTemp = analogBufferTemp[i]
				analogBufferTemp[i] = analogBufferTemp[i+1]
				analogBufferTemp[i+1] = bTemp
	if iFilterLen & 1 > 0:
		bTemp = analogBufferTemp[(iFilterLen - 1)/2]
	else:
		bTemp = (analogBufferTemp[iFilterLen / 2] + analogBufferTemp[iFilterLen / 2 - 1]) / 2
	return float(bTemp)

analogSampleTimepoint = time.time()
printTimepoint = time.time()
while True :
	if time.time() - analogSampleTimepoint > 0.04:
		#print(" test.......... ")
		analogSampleTimepoint = time.time()
		analogBuffer[analogBufferIndex] = ads1115.readVoltage(1)['r']
		analogBufferIndex = analogBufferIndex + 1
		if analogBufferIndex == 30:
			analogBufferIndex = 0

	if time.time()-printTimepoint > 0.8:
		#print(" test ")
		printTimepoint = time.time()
		for copyIndex in range(30):
			analogBufferTemp[copyIndex] = ads1115.readVoltage(1)['r']
		print(" A1:%dmV "%getMedianNum(30))
		averageVoltage = getMedianNum(30) * (VREF / 1024.0)
		compensationCoefficient = 1.0 + 0.02 * (temperature - 25.0)
		compensationVolatge = averageVoltage / compensationCoefficient
		tdsValue = (133.42 * compensationVolatge * compensationVolatge * compensationVolatge - 255.86 * compensationVolatge * compensationVolatge + 857.39 * compensationVolatge) * 0.5
		print(" A1:%dppm "%tdsValue)
