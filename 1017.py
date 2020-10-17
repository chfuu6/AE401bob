from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,103)


x,y,z = mc.player.getTilePos()
mc.setBlock(x+1,y,z,20)
time.sleep(1)
mc.setBlock(x+1,y,z+1,20)
time.sleep(1)
mc.setBlock(x,y,z+1,20)
time.sleep(1)
mc.setBlock(x-1,y,z+1,20)
time.sleep(1)
mc.setBlock(x-1,y,z,20)
time.sleep(1)
mc.setBlock(x-1,y,z-1,20)
time.sleep(1)
mc.setBlock(x,y,z-1,20)
time.sleep(1)
mc.setBlock(x+1,y,z-1,20)


x,y,z = mc.player.getTilePos()
mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,57)

