```bash
视频教程地址：
哔哩哔哩bilibili：树莓派爱好者基地、玩派VLOG
```

## 一、概述

上一期用PICO点亮了LED灯，这一期准备用按键来控制LED灯的点亮。为了更有趣一些，所以准备用三种方式来实现按键控制LED。
编程语言： micropython。

PICO接口图
![在这里插入图片描述](https://img-blog.csdnimg.cn/08367390ddb541af9775aea0261e0644.png#pic_center)
按键图和原理图
![在这里插入图片描述](https://img-blog.csdnimg.cn/72c69ee015d7440a9bdd0249cd1dcbb2.png#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/36d6e32fe2e54cfdbf307dfc2691b87c.png#pic_center)
## 二、开始
### 1、方式1（按键控制电路闭合）
最朴实无华的方式，LED正极连接PICO的GP0口，接口给高电平，通过按键控制电路是否闭合，闭合时点亮LED。
![在这里插入图片描述](https://img-blog.csdnimg.cn/c1f5ce4b83904c65b47a31c538777410.png#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/45da490b2a854318b609ca5283fcb369.png#pic_center)

### 2、方式2（按键逻辑控制点灯）
先看看原理图
![在这里插入图片描述](https://img-blog.csdnimg.cn/cb01fde9fec94385b1bd3e81c88dc749.png#pic_center)
再看看程序

```python
from machine import Pin
import time

led=Pin(0,Pin.OUT)
switch=Pin(1,Pin.IN,Pin.PULL_UP)

while True:
	if switch.value()==0:
		led.value(1)
	else:
		led.value(0)

```

这里GP0口依然与LED正极相连。按键一端和GP1口相连，一端和GND相连。GP1给一个上拉电阻，一直保持高电平状态，当按键按下时，电平变为低电平，触发条件，给GP0高电平，点亮LED。
![在这里插入图片描述](https://img-blog.csdnimg.cn/e5a7e4d901be429ea19f42738115ba21.png#pic_center)
![在这里插入图片描述](https://img-blog.csdnimg.cn/22c256692af4486ea1920fcb4185caf9.png#pic_center)

### 3、方式3（按键逻辑控制点灯+外部中断）
在方式2的基上做了一些改良，把while True循环检测改成了外部中断。电路连接完全不变。外部中断触发条件设置为下降沿触发，按键按下，GP1由高电平变为低电平，触发中断，点亮LED
看一下程序

```python
from machine import Pin
import time

led=Pin(0,Pin.OUT)
switch=Pin(1,Pin.IN,Pin.PULL_UP)
led.off()


def on_led(switch):
    led.on()
    time.sleep(5)
    led.off()
 
switch.irq(on_led,Pin.IRQ_FALLING)

```
![在这里插入图片描述](https://img-blog.csdnimg.cn/68d0c14f99c74194923e355181161bf8.png#pic_center)
