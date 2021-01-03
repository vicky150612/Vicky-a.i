import requests

def control_lights(state):
    requests.post(f"https://maker.ifttt.com/trigger/{state}/with/key/dNyMD-LXunh3XyaEvFPsnet6FCdmE1mkOHijHcP5hwv")
s = input('on or off : ')
if s=='on':
    z = 'camera_on'
    control_lights(z)
else:
    z = 'camera_off'
    control_lights(z)